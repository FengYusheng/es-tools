# -*- coding: utf-8 -*-
import os
import csv
import unittest
import unicodedata

from runAnalyzer import *

class TestFolding(unittest.TestCase):
    def test_ar_std_with_tashkeel(self):
        csv_source = os.path.realpath(
            os.path.abspath(
                os.path.expandvars(
                    os.path.expanduser('../../data/tashkeel_folding.csv')
                )
            )
        )

        if not os.access(csv_source, os.F_OK|os.R_OK):
            raise OSError("{0} doesn't exist.".format(csv_source))

        csv_report = os.path.basename(csv_source)
        csv_report = csv_report.rpartition('.')[0] + '_report' + '.csv'
        csv_report = '../../report_repo/' + csv_report
        csv_report = os.path.realpath(
            os.path.abspath(
                os.path.expandvars(
                    os.path.expanduser(csv_report)
                )
            )
        )

        with open(csv_report, 'w') as report:
            report_writer = csv.DictWriter(report, ['word', 'folding', 'expected', 'pass'])
            report_writer.writeheader()
            with open(csv_source, 'r') as source:
                source_reader = csv.DictReader(source)
                for row in source_reader:
                    row['with tashkeel'], row['without tashkeel'] = row['with tashkeel'].strip(), row['without tashkeel'].strip()
                    response = send_request_to_elasticsearch(row['with tashkeel'], row['with tashkeel'], 'ar_std')
                    response = handle_response('ar_std', response)
                    print('{0} == {1} ? {2}'.format(
                        response[0], row['without tashkeel'],
                        unicodedata.normalize('NFKC', response[0])==unicodedata.normalize('NFKC', row['without tashkeel'])
                    ))
                    is_same = unicodedata.normalize('NFKC', response[0])==unicodedata.normalize('NFKC', row['without tashkeel'])
                    report_writer.writerow({
                        'word' : row['with tashkeel'],
                        'folding' : response[0],
                        'expected' : row['without tashkeel'],
                        'pass' : is_same
                    })




if __name__ == '__main__':
    unittest.main()
