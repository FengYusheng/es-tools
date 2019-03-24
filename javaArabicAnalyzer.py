# -*- coding: utf-8 -*-
# https://github.com/kivy/pyjnius
# https://jpype.readthedocs.io/en/latest/userguide.html
# java -cp lucene-arabic-analyzer-1.1.2.jar:arabic-analyzer.jar arabic.analyzer.Library


import subprocess
completed_process = subprocess.run(
    ' java -cp ./jars/*:arabic-analyzer.jar arabic.analyzer.Library رحم الرَّحْمَنِ ',
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=True,
    check=True,
    universal_newlines=True
)
response = completed_process.stdout
print(repr(response))
