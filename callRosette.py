# -*- coding: utf-8 -*-
import os
import csv
import json


def build_word_list_from_a_csv(csv_file):
    csv_file = os.path.realpath(os.path.abspath(os.path.expandvars(os.path.expanduser(csv_file))))
    if not os.access(csv_file, os.F_OK|os.R_OK):
        raise OSError("The file {0} doesn't exist or you have no read permission.")

    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        inflections = [row['Inflection'] for row in csv_reader]

    return enumerate(inflections)



__all__ = [
    'build_word_list_from_a_csv'
]
