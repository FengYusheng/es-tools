# -*- coding: utf-8 -*-
"""
csv => json => csv
"""
import os
import json
import csv

g_words = {}


def run(csv_file):
    current_word = None
    csv_file = os.path.realpath(os.path.abspath(os.path.expandvars(os.path.expanduser(csv_file))))
    if not os.access(csv_file, os.F_OK|os.R_OK):
        raise  OSError("The file {0} doesn't exist or you have no read permission.".format(csv_file))

    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            g_words.setdefault(row['﻿Original'], {})
            current_word = row['﻿Original'] if row['﻿Original'] != current_word else current_word
            g_words[current_word].setdefault('inflections', {})
            inflection = g_words[current_word]['inflections']
            inflection.setdefault(row['Inflection'], 0)
            inflection[row['Inflection']] += 1

        print(json.dumps(g_words, indent=4, ensure_ascii=False))
        print(len(g_words))



__all__ = [
    'run'
]
