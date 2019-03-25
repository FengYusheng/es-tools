# -*- coding: utf-8 -*-
import unittest

from runAnalyzer import *


class TestMsarhan(unittest.TestCase):
    def test_access_an_nonexistent_csv(self):
        with self.assertRaises(OSError):
            process_inflection_in_a_csv_file('./data/nonexistent.csv')

    @unittest.skip("Skip irregular verbs for now")
    def test_irregular_verbs_with_msarhan(self):
        process_inflection_in_a_csv_file('./data/irregular_verbs.csv', analyzer='msarhan')


    @unittest.skip("Skip regular verbs for now")
    def test_regular_verbs_with_msarhan(self):
        process_inflection_in_a_csv_file('./data/regular_verbs.csv', analyzer='msarhan')


    @unittest.skip("Skip hamza for now")
    def test_hamza_with_msarhan(self):
        process_inflection_in_a_csv_file('./data/hamza.csv', analyzer='msarhan')


if __name__ == '__main__':
    unittest.main()
