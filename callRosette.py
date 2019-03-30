# -*- coding: utf-8 -*-
import os
import csv


def build_request_from_a_csv(csv_file):
    csv_file = os.path.realpath(os.path.abspath(os.path.expandvars(os.path.expanduser(csv_file))))
    if not os.access(csv_file, os.F_OK):
        raise OSError("The file {0} doesn't exist or you have no read permission.")



__all__ = [
    'build_request_from_a_csv'
]
