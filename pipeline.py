# -*- coding: utf-8 -*-
"""
csv => json => csv
"""
import os
import json
import csv
from copy import deepcopy as copy
from collections import Counter

g_words = {}
g_record_templete = './templetes/pipeline_record_templete.json'
g_report_repo = './report_repo'
g_accuracy_format = '{0:.1f}%'


def read_token_templete():
    record = None
    if not os.access(g_record_templete, os.F_OK|os.R_OK):
        raise  OSError("The file {0} doesn't exist or you have no read permission.".format(g_record_templete))

    with open(g_record_templete, 'r') as templete_file:
        record = json.load(templete_file)

    return record


def collect_analyzer_results(csv_file, analyzer):
    records = []
    token_templete = read_token_templete()
    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        # print(repr('Original'))
        # print(repr('﻿Original'))
        token = copy(token_templete)
        for row in csv_reader:
            if row['﻿Original'] != token['token']:
                if analyzer and len(token[analyzer]):
                    token[analyzer+'_count'] = Counter(token[analyzer])
                    records.append(token)
                token = copy(token_templete)
                token['token'] = row['﻿Original']

            token['terms'].append(row['Inflection'])
            token[analyzer].append(row[analyzer])

    token[analyzer+'_count'] = Counter(token[analyzer])
    records.append(token)
    return records


def add_new_analyzer_results(records, csv_file, analyzer):
    token = read_token_templete()
    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['﻿Original'] != token['token']:
                if len(token[analyzer]):
                    token[analyzer+'_count'] = Counter(token[analyzer])
                for t in records:
                    if t['token'] == row['﻿Original']:
                        token = t
                        break
            token[analyzer].append(row[analyzer])

    token[analyzer+'_count'] = Counter(token[analyzer])
    return records


def save_report(report_name, records):
    with open(report_name, 'w') as report:
        json.dump(records, report, ensure_ascii=False, indent=4)


def generate_accuracy_csv(report_name, records):
    with open(report_name, 'w') as report:
        csv_writer = csv.DictWriter(report, fieldnames=['token', 'term', 'msarhan', 'msarhan_accuracy', 'elasticsearch', 'es_accuracy', 'rosette', 'rosette_accuracy'])
        csv_writer.writeheader()
        for token in records:
            if not len(token['terms']) == len(token['msarhan']) == len(token['elasticsearch']):
                raise TypeError('Data format error.')

            token_, terms_, msarhan_, es_, rosette_ =  token['token'], token['terms'], token['msarhan'], token['elasticsearch'], token['rosette']
            msarhan_count, es_count, rosette_count = token['msarhan_count'], token['elasticsearch_count'], token['rosette_count']
            term_count = len(terms_)
            for i in range(term_count):
                # print(g_accuracy_format.format(msarhan_count[msarhan_[i]]*100/term_count))
                # print(g_accuracy_format.format(es_count[es_[i]]*100/term_count))
                csv_writer.writerow({
                    'token' : token_,
                    'term' : terms_[i],
                    'msarhan' : msarhan_[i],
                    'msarhan_accuracy' : g_accuracy_format.format(msarhan_count[msarhan_[i]]*100/term_count),
                    'elasticsearch' : es_[i],
                    'es_accuracy' : g_accuracy_format.format(es_count[es_[i]]*100/term_count),
                    'rosette' : rosette_[i],
                    'rosette_accuracy' : g_accuracy_format.format(rosette_count[rosette_[i]]*100/term_count)
                })


def generate_vowels_list(csv_file):
    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        vowels = [row['vowel'].strip() for row in csv_reader]
        # print(len(vowels))
        vowels = [''.join(vowels)]
        # print(len(vowels[0]))

    with open('./templetes/folding_parameter.json', 'w') as f:
        json.dump({
            'unicodeSetFilter' : vowels
        }, f, ensure_ascii=False)


def run(csv_file, analyzer=None):
    csv_file = os.path.realpath(os.path.abspath(os.path.expandvars(os.path.expanduser(csv_file))))
    if not os.access(csv_file, os.F_OK|os.R_OK):
        raise  OSError("The file {0} doesn't exist or you have no read permission.".format(csv_file))

    records = collect_analyzer_results(csv_file, analyzer)
    report_name = os.path.basename(csv_file).rpartition('.')[0] + '.json'
    report_name = os.path.join(g_report_repo, report_name)
    save_report(report_name, records)



__all__ = [
    'run',
    'read_token_templete',
    'collect_analyzer_results',
    'add_new_analyzer_results',
    'generate_accuracy_csv',
    'generate_vowels_list',
    'save_report'
]
