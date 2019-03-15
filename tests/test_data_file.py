# -*- coding: utf-8 -*-
import unittest
import json

from runAnalyzer import *


def test_words(input, output):
    options = optParser(['-p', '9220', '-s', 'localhost', '-i', 'arci-test', '-a', 'ar_std_lem'])
    data = read_text(input)
    words = data['words']
    for t in words:
        request = build_request(options, text=t['text'])
        response = send_request(request)
        results = handle_response(response)
        t['result'] = results
        t['inflect'] = len(results) == 1 and t['text'] not in results

    with open(output, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


class TestDataFile(unittest.TestCase):
    def test_raise_an_oserror_if_file_not_exist(self):
        with self.assertRaises(OSError):
            read_text('../data/hamza.json')


    def test_an_existing_file(self):
        texts = read_text('./data/words_with_hamza.json')
        self.assertTrue(len(texts))


    def test_words_with_hamza(self):
        options = optParser(['-p', '9220', '-s', 'localhost', '-i', 'arci-test', '-a', 'ar_std_lem'])
        data = read_text('./data/words_with_hamza.json')
        words = data['words']
        for t in words:
            request = build_request(options, text=t['text'])
            response = send_request(request)
            results = handle_response(response)
            t['result'] = results
            t['inflect'] = len(results) == 1 and t['text'] not in results

        with open('./data/words_with_hamza_analyzer.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)


    def test_words_without_hamza(self):
        test_words('./data/words_without_hamza.json', './data/words_without_hamza_analyzer.json')


    def test_words_with_punctuation(self):
        test_words('./data/words_with_punctuation.json', './data/words_with_punctuation_analyzer.json')


    def test_verbs(self):
        test_words('./data/verbs.json', './data/verbs_analyzer.json')


    def test_adjectives(self):
        test_words('./data/adjectives.json', './data/adjectives_analyzer.json')


    def test_nouns(self):
        test_words('./data/nouns.json', './data/nouns_analyzer.json')


    def test_numbers(self):
        test_words('./data/numbers.json', './data/numbers_analyzer.json')



if __name__ == '__main__':
    unittest.main()
