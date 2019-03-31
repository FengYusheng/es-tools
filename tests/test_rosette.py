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
        inflections = build_word_list_from_a_csv('./data/regular_verbs.csv')
        result = send_request_to_rosette(' '.join(inflections))
        print(result)



if __name__ == '__main__':
    unittest.main()
