# -*- coding: utf-8 -*-
# https://github.com/kivy/pyjnius
# https://jpype.readthedocs.io/en/latest/userguide.html
# java -cp lucene-arabic-analyzer-1.1.2.jar:arabic-analyzer.jar arabic.analyzer.Library "الرَّحْمَنِ"
#
# CLASSPATH = os.path.realpath(os.path.expanduser(os.path.expandvars(os.path.abspath('lucene-arabic-analyzer-1.1.2.jar'))))
#
# from jpype import *
#
# startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % CLASSPATH)
# # https://hustleplay.wordpress.com/2010/02/18/jpype-tutorial/
# msarhan = JPackage('com').github.msarhan.lucene
# ArabicRootExtractorStemmer = JClass("com.github.msarhan.lucene.ArabicRootExtractorStemmer")
# stemmer = ArabicRootExtractorStemmer()
# jString = java.lang.String("الرَّحْمَنِ")
# stemmer.stem(jString)
# shutdownJVM()
import subprocess
completed_process = subprocess.run(
    'java -cp lucene-arabic-analyzer-1.1.2.jar:arabic-analyzer.jar arabic.analyzer.Library "الرَّحْم"',
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=True,
    check=True,
    universal_newlines=True
)
response = completed_process.stdout
print(response)
