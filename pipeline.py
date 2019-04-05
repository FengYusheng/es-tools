# -*- coding: utf-8 -*-
"""
csv => json => csv
"""
import os
import json
import csv

g_words = {}
g_record_templete = './templetes/pipeline_record_templete.json'


def read_record_templete():
    record = None
    if not os.access(g_record_templete, os.F_OK|os.R_OK):
        raise  OSError("The file {0} doesn't exist or you have no read permission.".format(g_record_templete))

    with open(g_record_templete, 'r') as templete_file:
        record = json.load(templete_file)

    return record


def run(csv_file):
    current_word = None
    csv_file = os.path.realpath(os.path.abspath(os.path.expandvars(os.path.expanduser(csv_file))))
    if not os.access(csv_file, os.F_OK|os.R_OK):
        raise  OSError("The file {0} doesn't exist or you have no read permission.".format(csv_file))






__all__ = [
    'run',
    'read_record_templete'
]
