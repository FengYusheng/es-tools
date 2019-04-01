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
        params = DocumentParameters()
        params['language'] = 'ara'
        params['content'] = word_list
        try:
            respone = api.morphology(params, api.morphology_output['LEMMAS'])
        except RosetteException as e:
            respone = None
            print(e)

    return respone


def handle_rosette_morphology_lemma_response(csv_report, response, expection_list, inflection_list):
    count = succ = 0
    with open(csv_report, 'w') as csv_report:
        csv_writer = csv.DictWriter(csv_report, fieldnames=['Original', 'Inflection', 'Lemma', 'is_same'])
        csv_writer.writeheader()
        for i in range(len(expection_list)):
            expect = expection_list[i].strip()
            lemma = response['lemmas'][i].strip()
            inflect = inflection_list[i].strip()
            csv_writer.writerow({'Original':expect, 'Inflection':inflect, 'Lemma':lemma, 'is_same':expect==lemma})
            print({'Original':expect, 'Lemma':lemma, 'is_same':expect==lemma})

            count += 1
            succ = succ+1 if expect==lemma else succ

    print('count: {0}, succ: {1}'.format(count, succ))


def handle_rosette_morphology_token_response(csv_report, response, expection_list):
    with open(csv_report, 'w') as csv_report:
        csv_writer = csv.DictWriter(csv_report, fieldnames=['Input', 'Token', 'is_same'])
        csv_writer.writeheader()
        for i in range(len(expection_list)):
            expect = expection_list[i].strip()
            token = response['tokens'][i].strip()
            if expect != token:
                csv_writer.writerow({'Input':expect, 'Token':token, 'is_same':expect==token})



__all__ = [
    'build_word_list_from_a_csv',
    'build_expection_list_from_a_csv',
    'send_request_to_rosette',
    'handle_rosette_morphology_lemma_response',
    'handle_rosette_morphology_token_response'
]
