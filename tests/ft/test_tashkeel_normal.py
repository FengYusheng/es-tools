# -*- coding: utf-8 -*-
import csv
import os

from runAnalyzer import *
from pipeline import *
from commandline import optParser

def main():
    csv_file = os.path.realpath(os.path.abspath(os.path.expandvars(os.path.expanduser('./data/Alphabet with diacrtics - Alphbet with diacrtics.csv'))))
    if not os.access(csv_file, os.F_OK|os.R_OK):
        raise  OSError("The file {0} doesn't exist or you have no read permission.".format(csv_file))

    csv_report = csv_file.rpartition('.')[0] + '_report' + '.csv'
    with open(csv_report, 'w') as report:
        report_writer = csv.DictWriter(report, fieldnames=['diacritics', 'utf8', 'length', 'nfkc_cf', 'nfkc_cf_utf8', 'nfkc_cf_length'])
        report_writer.writeheader()
        with open(csv_file, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                response = send_request_to_elasticsearch(row['diacritics'], row['diacritics'], 'nfkc_cf_normal')
                response = handle_response('nfkc_cf_normal', response)
                original = row['diacritics'].strip()
                result = response[0].strip()
                print({'diacritics': original, 'utf8' : original.encode('utf-8'), 'length':len(original), 'nfkc_cf' : result, 'nfkc_cf_utf8' : result.encode('utf-8'), 'nfkc_cf_length':len(result)})
                report_writer.writerow({'diacritics': original, 'utf8' : original.encode('utf-8'), 'length':len(original), 'nfkc_cf' : result, 'nfkc_cf_utf8' : result.encode('utf-8'), 'nfkc_cf_length':len(result)})


if __name__ == '__main__':
    main()
