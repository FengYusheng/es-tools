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
        self.assertIn('es', record)
        self.assertIn('rosette', record)
        self.assertIn('root', record)
        self.assertIn('lemma', record)


    def test_save_report(self):
        save_report('test.json')


    def test_read_msarhan_results(self):
        run('./data/regular_verbs_msarhan_report.csv', 'msarhan')



if __name__ == '__main__':
    unittest.main()
