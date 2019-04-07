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


    @unittest.skip("Skip nouns for now")
    def test_nouns_with_elasticsearch(self):
        process_inflection_in_a_csv_file('./data/nouns.csv', analyzer='elasticsearch')


    @unittest.skip("Skip punctuation for now")
    def test_punctuation_with_elasticsearch(self):
        process_inflection_in_a_csv_file('./data/punctuation.csv', analyzer='elasticsearch')


    @unittest.skip("Skip numerals for now")
    def test_numerals_with_elasticsearch(self):
        process_inflection_in_a_csv_file('./data/numerals.csv', analyzer='elasticsearch')

    @unittest.skip("Skip derivatiion for now.")
    def test_derivation_with_elasticsearch(self):
        process_inflection_in_a_csv_file('./data/derivation.csv', analyzer='elasticsearch')


    def test_word_list(self):
        process_word_list_in_a_csv_file('./data/regular_verbs.csv', analyzer='rbl_ara_folding')


if __name__ == '__main__':
    unittest.main()
