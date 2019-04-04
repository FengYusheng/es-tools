# -*- coding: utf-8 -*-
"""
csv => json => csv
"""
import os
import json
import csv
from collections import Counter



def run(csv_file):
    csv_file = os.path.realpath(os.path.abspath(os.path.expandvars(os.path.expanduser(csv_file))))
    if not os.access(csv_file, os.F_OK|os.R_OK):
        raise  OSError("The file {0} doesn't exist or you have no read permission.".format(csv_file))



__all__ = [
    'run'
]
