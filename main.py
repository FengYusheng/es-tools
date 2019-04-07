# -*- coding: utf-8 -*-

from runAnalyzer import *
from pipeline import *


def run():
    process_inflection_in_a_csv_file('./data/regular_verbs.csv', analyzer='rbl_ara')
    process_inflection_in_a_csv_file('./data/regular_verbs.csv', analyzer='rbl_ara_folding')
    process_inflection_in_a_csv_file('./data/regular_verbs.csv', analyzer='ar_std_lem_folding1')
    process_inflection_in_a_csv_file('./data/regular_verbs.csv', analyzer='ar_std_lem_folding2')
    process_inflection_in_a_csv_file('./data/regular_verbs.csv', analyzer='msarhan')
    records = collect_analyzer_results('./data/regular_verbs_rbl_ara_report.csv', 'rbl_ara')
    records = add_new_analyzer_results(records, './data/regular_verbs_rbl_ara_folding_report.csv', 'rbl_ara_folding')
    records = add_new_analyzer_results(records, './data/regular_verbs_ar_std_lem_folding1_report.csv', 'ar_std_lem_folding1')
    records = add_new_analyzer_results(records, './data/regular_verbs_ar_std_lem_folding2_report.csv', 'ar_std_lem_folding2')
    records = add_new_analyzer_results(records, './data/regular_verbs_msarhan_report.csv', 'msarhan')
    save_report('./report_repo/regular_verbs.json', records)
    generate_accuracy_csv('./report_repo/regular_verbs.csv', records)



if __name__ == '__main__':
    run()
