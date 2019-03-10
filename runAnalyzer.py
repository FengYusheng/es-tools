# -*- coding: utf-8 -*-
import argparse
import subprocess
import json
import sys

def optParser(*args):
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

    options = parser.parse_args(args=args)
    return vars(options)


def build_request(options, method='GET'):
    request = 'curl -s -X{0} http://{1}:{2}'.format(method, options['server'], options['port'])
    return request


def send_request(request):
    completed_process = subprocess.run(request, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, check=True, universal_newlines=True)
    response = completed_process.stdout if completed_process.stderr == '' else completed_process.stderr
    return json.loads(response, encoding='utf-8')


__all__ = [
    'optParser'
]


if __name__ == '__main__':
    options = optParser()
    request = build_request(options)
    send_request(request)
