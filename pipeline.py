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
        token = copy(token_templete)
        for row in csv_reader:
            if row['Original'] != token['token']:
                if analyzer and len(token[analyzer]):
                    token[analyzer+'_count'] = Counter(token[analyzer])
                    records.append(token)
                token = copy(token_templete)
                token['token'] = row['Original']

            token['terms'].append(row['Inflection'])
            token[analyzer].append(row[analyzer])

    token[analyzer+'_count'] = Counter(token[analyzer])
    records.append(token)
    return records


def calculate_hunspell_token_count(ara_hunspell_count):
    new_ara_hunspell_count = copy(ara_hunspell_count)
    for key in ara_hunspell_count:
        count_ = 0
        key_list = key.split(' ')

        for key2 in ara_hunspell_count:
            key2_list = key2.split(' ')
            for k in key_list:
                if k in key2_list:
                    count_ += ara_hunspell_count[key2]
                    break

        new_ara_hunspell_count[key] = count_

    return new_ara_hunspell_count


def add_new_analyzer_results(records, csv_file, analyzer):
    token = read_token_templete()
    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['Original'] != token['token']:
                if len(token[analyzer]):
                    token[analyzer+'_count'] = Counter(token[analyzer])
                for t in records:
                    if t['token'] == row['Original']:
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
        csv_writer = csv.DictWriter(report, fieldnames=[
            'token', 'term', 'msarhan', 'msarhan_accuracy', 'rbl_ara', 'rbl_ara_accuracy', 'rbl_ara_folding', 'rbl_ara_folding_accuracy', 'ar_std_lem_folding1', 'ar_std_lem_folding1_accuracy', 'ar_std_lem_folding2', 'ar_std_lem_folding2_accuracy', 'ara_hunspell', 'ara_hunspell_accuracy'
            ])
        csv_writer.writeheader()

        for token in records:
            if not len(token['terms']) \
            == len(token['msarhan']) \
            == len(token['rbl_ara']) \
            == len(token['rbl_ara_folding']) \
            == len(token['ar_std_lem_folding1']) \
            == len(token['ar_std_lem_folding2']) \
            == len(token['ara_hunspell']):
                raise TypeError('Data format error about "{0}".'.format(token['token']))

            token_, terms_, msarhan_, rbl_ara_, rbl_ara_folding_, ar_std_lem_folding1_, ar_std_lem_folding2_, ara_hunspell_ =  token['token'], token['terms'], token['msarhan'], token['rbl_ara'], token['rbl_ara_folding'], token['ar_std_lem_folding1'], token['ar_std_lem_folding2'], token['ara_hunspell']

            msarhan_count, rbl_ara_count, rbl_ara_folding_count, ar_std_lem_folding1_count, ar_std_lem_folding2_count, ara_hunspell_count = token['msarhan_count'], token['rbl_ara_count'], token['rbl_ara_folding_count'], token['ar_std_lem_folding1_count'], token['ar_std_lem_folding2_count'], token['ara_hunspell_count']

            ara_hunspell_count = calculate_hunspell_token_count(ara_hunspell_count)

            term_count = len(terms_)
            for i in range(term_count):
                csv_writer.writerow({
                    'token' : token_,
                    'term' : terms_[i],
                    'msarhan' : msarhan_[i],
                    'msarhan_accuracy' : g_accuracy_format.format(msarhan_count[msarhan_[i]]*100/term_count),
                    'rbl_ara' : rbl_ara_[i],
                    'rbl_ara_accuracy' : g_accuracy_format.format(rbl_ara_count[rbl_ara_[i]]*100/term_count),
                    'rbl_ara_folding' : rbl_ara_folding_[i],
                    'rbl_ara_folding_accuracy' : g_accuracy_format.format(rbl_ara_folding_count[rbl_ara_folding_[i]]*100/term_count),
                    'ar_std_lem_folding1' : ar_std_lem_folding1_[i],
                    'ar_std_lem_folding1_accuracy' : g_accuracy_format.format(ar_std_lem_folding1_count[ar_std_lem_folding1_[i]]*100/term_count),
                    'ar_std_lem_folding2' : ar_std_lem_folding2_[i],
                    'ar_std_lem_folding2_accuracy' : g_accuracy_format.format(ar_std_lem_folding2_count[ar_std_lem_folding2_[i]]*100/term_count),
                    'ara_hunspell' : ara_hunspell_[i],
                    'ara_hunspell_accuracy' : g_accuracy_format.format(ara_hunspell_count[ara_hunspell_[i]]*100/term_count)
                })


def generate_vowels_list(csv_file):
    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        vowels = [row['vowel'].strip() for row in csv_reader]
        vowels = [''.join(vowels)]

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
