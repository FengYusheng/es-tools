# -*- coding: utf-8 -*-
import os
import csv
import json

from rosette.api import API, DocumentParameters, RosetteException


def build_word_list_from_a_csv(csv_file):
    csv_file = os.path.realpath(os.path.abspath(os.path.expandvars(os.path.expanduser(csv_file))))
    if not os.access(csv_file, os.F_OK|os.R_OK):
        raise OSError("The file {0} doesn't exist or you have no read permission.")

    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        inflections = [row['Inflection'].strip() for row in csv_reader]

    return inflections


def build_expection_list_from_a_csv(csv_file):
    csv_file = os.path.realpath(os.path.abspath(os.path.expandvars(os.path.expanduser(csv_file))))
    if not os.access(csv_file, os.F_OK|os.R_OK):
        raise OSError("The file {0} doesn't exist or you have no read permission.")

    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        expection = [row['﻿Original'].strip() for row in csv_reader]

    return expection



def send_request_to_rosette(word_list=None):
    api = API(user_key='d710f6b45bc1a291f43cd3310312160b')

    if not word_list:
        respone = api.ping()
    else:
        # Specify language.
        # api.set_option('language', 'ara')
        # api.set_option('content', word_list)
        params = DocumentParameters()
        params['language'] = 'ara'
        params['content'] = word_list
        try:
            respone = api.morphology(params, api.morphology_output['LEMMAS'])
        except RosetteException as e:
            respone = None
            print(e)

    return respone


def handle_rosette_lemma_response(respone):
    pass



__all__ = [
    'build_word_list_from_a_csv',
    'build_expection_list_from_a_csv',
    'send_request_to_rosette',
    'handle_rosette_lemma_response'
]
