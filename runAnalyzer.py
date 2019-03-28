# -*- coding: utf-8 -*-
import argparse
import subprocess
import json
import time
import csv
import sys
import os

diff = count = succ = 0

def handle_msarhan_response(response, original, inflection, report_writer=None):
    global count, succ
    response = response.split('\n')
    original, root, result = original.strip(), response[0].strip(), response[1].strip()
    print({'Original':original, 'Inflection':inflection, 'msarhan':result, 'is_same':original==result})
    report_writer and report_writer.writerow({'Original':original, 'Inflection':inflection, 'msarhan':result, 'is_same':original==result})

    count += 1
    succ = succ + 1 if original==result else succ


def handle_response(response):
    if 'tokens' in response:
        return [t['token'] for t in response['tokens']]
    else:
        raise(TypeError('Error response'))


def handle_elasticsearch_response(response, original, inflection, report_writer=None):
    global count, succ
    response = handle_response(response)
    original = original.strip()
    results = [i.strip() for i in response]
    print({'Original': original, 'Inflection' : inflection, 'elasticsearch' : response, 'is_same' : original in results})
    report_writer and report_writer.writerow({'Original':original, 'Inflection':inflection, 'elasticsearch':' '.join(results), 'is_same':original in results})

    count += 1
    succ = succ + 1 if original in results else succ


def optParser(args=[]):
    kwargs = {
        "prog" : "runAnalyzer",
        "description" : '''Call ES Analyzer API''',
        "formatter_class" : argparse.RawDescriptionHelpFormatter,
        "argument_default" : argparse.SUPPRESS,
        "conflict_handler" : "error"
    }

    parser = argparse.ArgumentParser(**kwargs)
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
    parser.add_argument('-s', '--server', action='store', type=str, required=False, default='localhost', help='the address of your elasticesearch server.', dest='server', metavar='Server')
    parser.add_argument('-p', '--port', action='store', type=str, required=False, default='9220', help='the port number which your elasticsearch is listening on', dest='port', metavar='Port')
    parser.add_argument('-i', '--index', action='store', type=str, required=False, default=None, help='the index which you want handle', dest='index', metavar='Index')
    parser.add_argument('-a', '--analyzer', action='store', type=str, required=False, default=None, help='the analyzer which you want to call', dest='analyzer', metavar='Analyzer')

    options = parser.parse_args(args=args)
    return vars(options)


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
    curl -s -H "Content-Type:application/json;charset=utf-8" -XPOST https://demo.rosette.com/api/index.php/algorithms/morphological_analysis?demo_id=-1 -d '{"content":"نشتري"}'
    '''
    request = 'curl -s -H "Content-Type:application/json;charset=utf-8" '
    request += '-XPOST '
    request += 'https://demo.rosette.com/api/index.php/algorithms/morphological_analysis?demo_id=-1'
    request += ' -d \'{"content":'
    request += '"' + text + '"'
    request += '}\''
    return request


def send_request(request):
    completed_process = subprocess.run(request, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, check=True, universal_newlines=True)
    response = completed_process.stdout if completed_process.stderr == '' else completed_process.stderr
    return json.loads(response, encoding='utf-8')


def read_text(csv_file):
    csv_file = os.path.realpath(os.path.abspath(os.path.expandvars(os.path.expanduser(csv_file))))
    if not os.access(csv_file, os.F_OK|os.R_OK):
        raise OSError("The file {0} doesn't exist or you have no read permission.".format(csv_file))

    # TODO: Read data from a csv
    with open(csv_file, 'r') as f:
        pass

    return data



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



def send_request_to_elasticsearch(root, inflection):
    options = optParser(['-p', '9220', '-s', 'localhost', '-i', 'arci-test', '-a', 'ar_std_lem'])
    # Just folding
    # options = optParser(['-p', '9220', '-s', 'localhost', '-i', 'arci-test', '-a', 'ar_std'])
    request = build_request(options, text=inflection)
    response = send_request(request)
    return response


def send_request_to_rosette(root, inflection):
    request = build_rosette_request(inflection)


def process_inflection_in_a_csv_file(csv_file, analyzer='msarhan'):
    global count, succ
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
                elif analyzer == 'elasticsearch':
                    response = send_request_to_elasticsearch(row['﻿Original'], row['Inflection'])
                    handle_elasticsearch_response(response, row['﻿Original'], row['Inflection'], report_writer)
                elif analyzer == 'rosette':
                    send_request_to_rosette(row['﻿Original'], row['Inflection'])

            print('Count: {0} Succ: {1}'.format(count, succ))



__all__ = [
    'optParser',
    'read_text',
    'build_request',
    'send_request',
    'handle_response',
    'process_inflection_in_a_csv_file',
    'send_request_to_msarhan',
    'handle_msarhan_response',
    'send_request_to_rosette'
]


if __name__ == '__main__':
    options = optParser(['-p', '9220', '-s', 'localhost', '-i', 'arci-test', '-a', 'ar_std_lem'])
    data = read_text('./data/words_with_hamza.json')
    for t in data:
        request = build_request(options, text=t['text'])
        response = send_request(request)
        results = handle_response(response)
        t['result'] = results
        t['inflect'] = len(results) == 1 and t['text'] not in results

    with open('./data/words_with_hamza_analyzer.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
