# -*- coding: utf-8 -*-
import unittest

from commandline import *


class TestCommandLines(unittest.TestCase):
    def test_server_option(self):
        options = optParser(['-s', '192.168.0.1'])
        self.assertEqual(options['server'], '192.168.0.1')

        options = optParser(['--server', '192.168.0.1'])
        self.assertEqual(options['server'], '192.168.0.1')

        options = optParser(['--s', '192.168.0.1'])
        self.assertEqual(options['server'], '192.168.0.1')


    def test_port_option(self):
        options = optParser(['-p', '9200'])
        self.assertEqual(options['port'], '9200')

        options = optParser(['--port', '9210'])
        self.assertEqual(options['port'], '9210')


    def test_index_option(self):
        options = optParser(['-i', 'arci'])
        self.assertEqual(options['index'], 'arci')

        options = optParser(['--index', 'arci'])
        self.assertEqual(options['index'], 'arci')


    def test_analyzer_option(self):
        options = optParser(['-a', 'ar_std'])
        self.assertEqual(options['analyzer'], 'ar_std')

        options = optParser(['--analyzer', 'ar_std'])
        self.assertEqual(options['analyzer'], 'ar_std')


    def test_raise_an_expection_if_no_file_supplied(self):
        with self.assertRaises(TypeError):
            readConf(optParser())


    def test_read_options_from_a_nonexistent_json_file(self):
        options = optParser(['-c', './templetes/nonexistent.json'])
        self.fail('read a nonexistent json file')



if __name__ == '__main__':
    unittest.main()
