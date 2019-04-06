# -*- coding: utf-8 -*-

import unittest

from pipeline import *


class TestPipeline(unittest.TestCase):
    def test_access_an_nonexistent_csv(self):
        with self.assertRaises(OSError):
            run('./data/nonexistent.csv')


    def test_read_record_templete_from_a_json_file(self):
        record = read_token_templete()
        self.assertIn('token', record)
        self.assertIn('terms', record)
        self.assertIn('msarhan', record)
        self.assertIn('elasticsearch', record)
        self.assertIn('rosette', record)
        self.assertIn('root', record)
        self.assertIn('lemma', record)


    def test_collect_analzyer_results(self):
        records = collect_analyzer_results('./data/regular_verbs_msarhan_report.csv', 'msarhan')
        self.assertEqual(len(records), 22)
        self.assertEqual(records[-1]['token'], 'نتج')
        self.assertEqual(records[0]['token'], 'نقل')
        self.assertIn('منع', records[2]['msarhan'])


    def test_add_a_new_analyzer_report_to_records(self):
        records = collect_analyzer_results('./data/regular_verbs_msarhan_report.csv', 'msarhan')
        records = add_new_analyzer_results(records, './data/regular_verbs_elasticsearch_report.csv', 'elasticsearch')
        self.assertEqual(len(records), 22)
        self.assertEqual(records[-1]['token'], 'نتج')
        self.assertEqual(records[0]['token'], 'نقل')
        self.assertIn('امنع', records[2]['elasticsearch'])
        save_report('./report_repo/regular_verbs.json', records)


    def test_gernerate_accuracy_csv(self):
        records = collect_analyzer_results('./data/regular_verbs_msarhan_report.csv', 'msarhan')
        records = add_new_analyzer_results(records, './data/regular_verbs_elasticsearch_report.csv', 'elasticsearch')
        records = add_new_analyzer_results(records, './data/regular_verbs_rosette_lemma_report.csv', 'rosette')
        generate_accuracy_csv('./report_repo/regular_verbs.csv', records)


    def test_gernerate_vowel_list(self):
        generate_vowels_list('./data/letters_with_punctuation.csv')


    @unittest.skip('Skip save.')
    def test_save_report(self):
        records = collect_analyzer_results('./data/regular_verbs_msarhan_report.csv', 'msarhan')
        save_report('./report_repo/regular_verbs_msarhan_report.json', records)


    @unittest.skip('Skip test run.')
    def test_run(self):
        run('./data/regular_verbs_msarhan_report.csv', 'msarhan')



if __name__ == '__main__':
    unittest.main()
