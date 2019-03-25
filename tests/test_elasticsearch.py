# -*- coding: utf-8 -*-
import unittest

from runAnalyzer import *

class TestElastisearch(unittest.TestCase):
    @unittest.skip("Skip irregular verbs for now")
    def test_irregular_verbs(self):
        process_inflection_in_a_csv_file('./data/irregular_verbs.csv', analyzer='elasticsearch')


    @unittest.skip("Skip regular verbs for now")
    def test_regular_verbs_with_elasticsearch(self):
        process_inflection_in_a_csv_file('./data/regular_verbs.csv', analyzer='elasticsearch')


    @unittest.skip("Skip hamza for now")
    def test_hamza_with_elasticsearch(self):
        process_inflection_in_a_csv_file('./data/hamza.csv', analyzer='elasticsearch')


if __name__ == '__main__':
    unittest.main()
