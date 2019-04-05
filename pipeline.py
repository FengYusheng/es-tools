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


def read_token_templete():
    record = None
    if not os.access(g_record_templete, os.F_OK|os.R_OK):
        raise  OSError("The file {0} doesn't exist or you have no read permission.".format(g_record_templete))

    with open(g_record_templete, 'r') as templete_file:
        record = json.load(templete_file)

    return record


def save_report(report_name, records=[]):
    dest = os.path.join(g_report_repo, report_name)



def run(csv_file, analyzer=None):
    current_word = None
    records = []
    token_templete = read_token_templete()
    csv_file = os.path.realpath(os.path.abspath(os.path.expandvars(os.path.expanduser(csv_file))))
    if not os.access(csv_file, os.F_OK|os.R_OK):
        raise  OSError("The file {0} doesn't exist or you have no read permission.".format(csv_file))

    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        # print(repr('Original'))
        # print(repr('﻿Original'))
        token = copy(token_templete)
        for row in csv_reader:
            if row['﻿Original'] != token['token']:
                if analyzer and len(token[analyzer]):
                    token[analyzer] = Counter(token[analyzer])
                    records.append(token)
                token = copy(token_templete)
                token['token'] = row['﻿Original']
            token['terms'].append(row['Inflection'])
            if analyzer:
                token[analyzer].append(row[analyzer])


    




__all__ = [
    'run',
    'read_token_templete',
    'save_report'
]
