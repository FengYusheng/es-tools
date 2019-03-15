# -*- coding: utf-8 -*-
import argparse
import subprocess
import json
import time
import sys
import os


def optParser(args=[]):
    kwargs = {
        "prog" : "runAnalyzer",
        "description" : '''Call ES Analyzer API''',
        "formatter_class" : argparse.RawDescriptionHelpFormatter,
        "argument_default" : argparse.SUPPRESS,
        "conflict_handler" : "error"
    }

    parser = argparse.ArgumentParser(**kwargs)
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
    parser.add_argument('-s', '--server', action='store', type=str, required=False, default='localhost', help='the address of your elasticesearch server.', dest='server', metavar='Server')
    parser.add_argument('-p', '--port', action='store', type=str, required=False, default='9220', help='the port number which your elasticsearch is listening on', dest='port', metavar='Port')
    parser.add_argument('-i', '--index', action='store', type=str, required=False, default=None, help='the index which you want handle', dest='index', metavar='Index')
    parser.add_argument('-a', '--analyzer', action='store', type=str, required=False, default=None, help='the analyzer which you want to call', dest='analyzer', metavar='Analyzer')

    options = parser.parse_args(args=args)
    return vars(options)


def build_request(options, method='POST', text='returnning'):
    request = 'curl -s -H "Content-type: application/json" -X{0} http://{1}:{2}/{3}'.format(method, options['server'], options['port'], options['index'])
    request += '/_analyze?pretty'
    request += ' -d \'{"analyzer":'
    request += '"' + options['analyzer'] + '",'
    request += '"text":'
    request += '"' + text + '"'
    request += '}\''

    return request


def send_request(request):
    completed_process = subprocess.run(request, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, check=True, universal_newlines=True)
    response = completed_process.stdout if completed_process.stderr == '' else completed_process.stderr
    return json.loads(response, encoding='utf-8')


def read_text(data_file):
    data_file = os.path.realpath(os.path.abspath(os.path.expandvars(os.path.expanduser(data_file))))
    if not os.access(data_file, os.F_OK|os.R_OK):
        raise OSError("The file {0} doesn't exist or you have no read permission.".format(data_file))

    # TODO: JSON iterator
    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        texts = data['words']

    return data


def handle_response(response):
    if 'tokens' in response:
        return [t['token'] for t in response['tokens']]
    else:
        raise(TypeError('Error response'))



__all__ = [
    'optParser',
    'read_text',
    'build_request',
    'send_request',
    'handle_response'
]


if __name__ == '__main__':
    options = optParser(['-p', '9220', '-s', 'localhost', '-i', 'arci-test', '-a', 'ar_std_lem'])
    data = read_text('./data/words_with_hamza.json')
    for t in data:
        request = build_request(options, text=t['text'])
        response = send_request(request)
        results = handle_response(response)
        t['result'] = results
        t['inflect'] = len(results) == 1 and t['text'] not in results

    with open('./data/words_with_hamza_analyzer.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
