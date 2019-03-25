# -*- coding: utf-8 -*-
import unittest

from runAnalyzer import *

class TestElastisearch(unittest.TestCase):
    @unittest.skip("Skip verbs for now")
    def test_irregular_verbs(self):
        process_inflection_in_a_csv_file('./data/irregular_verbs.csv', analyzer='elasticsearch')


    def test_hamza_with_elasticsearch(self):
        process_inflection_in_a_csv_file('./data/hamza.csv', analyzer='elasticsearch')


if __name__ == '__main__':
    unittest.main()
