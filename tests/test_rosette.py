# -*- coding: utf-8 -*-
import unittest

from callRosette import *


class TestRosette(unittest.TestCase):
    def test_raise_an_exception_when_read_an_nonexistent_csv_file(self):
        with self.assertRaises(OSError):
            build_word_list_from_a_csv('./data/nonexistent.csv')


    def test_build_regular_verb_list(self):
        inflections = build_word_list_from_a_csv('./data/regular_verbs.csv')
        self.assertEqual(inflections[0], 'نقل')


    def test_build_regular_verb_expection_list(self):
        expection = build_expection_list_from_a_csv('./data/regular_verbs.csv')
        self.assertEqual(expection[0], 'نقل')


    @unittest.skip('Skip rosette call for now')
    def test_rosette_api_is_available(self):
        result = send_request_to_rosette()
        self.assertIn('message', result)
        self.assertEqual('Rosette at your service', result['message'])


    def test_send_regular_verb_list_to_rosette_morphology_lemmas(self):
        token_report = './data/regular_verbs_rosette_token_report.csv'
        lemma_report = './data/regular_verbs_rosette_lemma_report.csv'
        inflections = build_word_list_from_a_csv('./data/regular_verbs.csv')
        expection_list = build_expection_list_from_a_csv('./data/regular_verbs.csv')
        response = send_request_to_rosette(' '.join(inflections))
        handle_rosette_morphology_token_response(token_report, response, inflections)
        handle_rosette_morphology_lemma_response(lemma_report, response, expection_list)
        # self.maxDiff = None
        # self.assertEquals(inflections, result['tokens'])
        self.assertEqual(len(response['tokens']), len(expection_list))
        self.assertEqual(len(response['tokens']), len(inflections))



if __name__ == '__main__':
    unittest.main()
