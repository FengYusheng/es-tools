# -*- coding: utf-8 -*-
import argparse
import subprocess
import json
import time
import csv
import sys
import os

from callRosette import build_word_list_from_a_csv, build_expection_list_from_a_csv
from commandline import optParser

diff = count = succ = 0

def handle_msarhan_response(response, original, inflection, report_writer=None):
    global count, succ
    response = response.split('\n')
    original, root, result = original.strip(), response[0].strip(), response[1].strip()
    print({'Original':original, 'Inflection':inflection, 'msarhan':result, 'is_same':original==result})
    report_writer and report_writer.writerow({'Original':original, 'Inflection':inflection, 'msarhan':result, 'is_same':original==result})

    count += 1
    succ = succ + 1 if original==result else succ


def handle_response(analyzer, response):
    if 'tokens' in response:
        tokens_ = [t['token'] for t in response['tokens'] if t['type'] == '<LEMMA>'] if 'rbl_ara' in analyzer else [t['token'] for t in response['tokens']]
        return sorted(tokens_)
    else:
        print(response)
        raise(TypeError('Error response'))


def handle_elasticsearch_response(analyzer, response, original, inflection, report_writer=None):
    global count, succ
    response = handle_response(analyzer, response)
    original = original.strip()
    results = [i.strip() for i in response]
    print({'Original': original, 'Inflection' : inflection, analyzer : response, 'is_same' : original in results})
    report_writer and report_writer.writerow({'Original':original, 'Inflection':inflection, analyzer:' '.join(results), 'is_same':original in results})

    count += 1
    succ = succ + 1 if original in results else succ


def handle_word_list_elasticsearch_response(analyzer, response, expection_list, inflection_list, report_writer=None):
    global count, succ
    print(len(response['tokens']), len(expection_list), len(inflection_list))
    if not int(len(response['tokens'])/2) \
    == len(expection_list) \
    == len(inflection_list):
        raise TypeError('Data format error.')

    term_count = len(inflection_list)
    tokens = handle_response(analyzer, response)
    for i in range(term_count):
        is_same = expection_list[i] == inflection_list[i]
        print({'Original': expection_list[i], 'Inflection' : inflection_list[i], analyzer+'_word_list' : tokens[i]['token'], 'is_same' : is_same})
        report_writer and report_writer.writerow({'Original':expection_list[i], 'Inflection':inflection_list[i], analyzer+'_word_list':tokens[i]['token'], 'is_same':is_same})

        count += 1
        succ = succ + 1 if is_same else succ


def handle_rosette_response(response, original, inflection, report_writer=None):
    global count, succ
    if not ('result' in response and 'lemmas' in response['result']):
        print(response)
        raise(TypeError('Connection Broken!'))

    print('original : {0}'.format(original))
    print('inflection : {0}'.format(inflection))
    print('result : {0}'.format(response['result']['lemmas']))
    results = response['result']['lemmas']
    results = [i.strip() for i in results if i is not None]
    is_same = original in results
    print({'Original': original, 'Inflection' : inflection, 'rosette' : response['result']['lemmas'], 'is_same' : is_same})
    report_writer and report_writer.writerow({'Original':original, 'Inflection':inflection, 'rosette':' '.join(results), 'is_same':original in results})

    count += 1
    succ = succ + 1 if is_same else succ


def build_request(options, method='POST', text='returnning'):
    request = 'curl -s -H "Content-type: application/json" -X{0} http://{1}:{2}/{3}'.format(method, options['server'], options['port'], options['index'])
    request += '/_analyze?pretty'
    request += ' -d \'{"analyzer":'
    request += '"' + options['analyzer'] + '",'
    request += '"text":'
    request += '"' + text + '"'
    request += '}\''

    return request


def build_rosette_request(text):
    '''
    curl -s -H "Content-Type:application/json;charset=utf-8" -XPOST http://demo.rosette.com/api/index.php/algorithms/morphological_analysis?demo_id=-1 -d '{"content":"نشتري"}'
    '''
    request = 'curl -s -H "Content-Type:application/json;charset=utf-8" '
    request += '-XPOST '
    request += 'https://demo.rosette.com/api/index.php/algorithms/morphological_analysis?demo_id=-1'
    request += ' -d \'{"content":'
    request += '"' + text + '"'
    request += '}\''
    return request


def send_request(request):
    retry = True
    while retry:
        try:
            completed_process = subprocess.run(request, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, check=True, universal_newlines=True)
            retry = False
        except Exception as e:
            retry = True
    # completed_process = subprocess.run(request, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, check=True, universal_newlines=True)
    response = completed_process.stdout if completed_process.stderr == '' else completed_process.stderr
    return json.loads(response, encoding='utf-8')



def send_request_to_msarhan(root, inflection):
    completed_process = subprocess.run(
        ' java -cp ./jars/*:arabic-analyzer.jar arabic.analyzer.Library {0} {1}'\
        .format(root, inflection),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        check=True,
        universal_newlines=True
    )
    response = completed_process.stdout if completed_process.stderr == '' else completed_process.stderr
    return response



def send_request_to_elasticsearch(root, inflection, analyzer='ar_std_lem'):
    options = optParser(['-p', '9200', '-s', 'localhost', '-i', 'arci-custom-test', '-a', analyzer])
    request = build_request(options, text=inflection)
    response = send_request(request)
    return response


def send_request_to_rosette(root, inflection):
    request = build_rosette_request(inflection)
    response = send_request(request)
    return response


def process_inflection_in_a_csv_file(csv_file, analyzer='msarhan'):
    global count, succ
    count = succ = 0
    csv_file = os.path.realpath(os.path.abspath(os.path.expandvars(os.path.expanduser(csv_file))))
    if not os.access(csv_file, os.F_OK|os.R_OK):
        raise  OSError("The file {0} doesn't exist or you have no read permission.".format(csv_file))

    csv_report = csv_file.rpartition('.')[0] + '_{0}_report'.format(analyzer) + '.csv'
    with open(csv_report, 'w') as report:
        report_writer = csv.DictWriter(report, fieldnames=['Original', 'Inflection', analyzer, 'is_same'])
        report_writer.writeheader()
        with open(csv_file, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if analyzer == 'msarhan':
                    response = send_request_to_msarhan(row['﻿Original'], row['Inflection'])
                    handle_msarhan_response(response, row['﻿Original'], row['Inflection'], report_writer)
                else:
                    response = send_request_to_elasticsearch(row['﻿Original'], row['Inflection'], analyzer)
                    handle_elasticsearch_response(analyzer, response, row['﻿Original'], row['Inflection'], report_writer)

            print('Count: {0} Succ: {1}'.format(count, succ))


def process_word_list_in_a_csv_file(csv_file, analyzer='rbl_ara_folding'):
    global count, succ
    count = succ = 0
    csv_file = os.path.realpath(os.path.abspath(os.path.expandvars(os.path.expanduser(csv_file))))
    if not os.access(csv_file, os.F_OK|os.R_OK):
        raise  OSError("The file {0} doesn't exist or you have no read permission.".format(csv_file))

    csv_report = csv_file.rpartition('.')[0] + '_{0}_word_list_report'.format(analyzer) + '.csv'
    inflection_list = build_word_list_from_a_csv(csv_file)
    expection_list = build_expection_list_from_a_csv(csv_file)
    with open(csv_report, 'w') as csv_report:
        report_writer = csv.DictWriter(csv_report, fieldnames=['Original', 'Inflection', analyzer+'_word_list', 'is_same'])
        report_writer.writeheader()
        response = send_request_to_elasticsearch(' '.join(expection_list), ' '.join(inflection_list), 'rbl_ara_folding')
        handle_word_list_elasticsearch_response(analyzer, response, expection_list, inflection_list, report_writer)

    print('Count: {0} Succ: {1}'.format(count, succ))



__all__ = [
    'build_request',
    'send_request',
    'handle_response',
    'process_inflection_in_a_csv_file',
    'process_word_list_in_a_csv_file',
    'send_request_to_msarhan',
    'handle_msarhan_response',
    'send_request_to_rosette',
    'send_request_to_elasticsearch'
]
