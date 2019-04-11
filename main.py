# -*- coding: utf-8 -*-

from runAnalyzer import *
from pipeline import *

def regular_verbs():
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


def irregular_verbs():
    process_inflection_in_a_csv_file('./data/irregular_verbs.csv', analyzer='rbl_ara')
    process_inflection_in_a_csv_file('./data/irregular_verbs.csv', analyzer='rbl_ara_folding')
    process_inflection_in_a_csv_file('./data/irregular_verbs.csv', analyzer='ar_std_lem_folding1')
    process_inflection_in_a_csv_file('./data/irregular_verbs.csv', analyzer='ar_std_lem_folding2')
    process_inflection_in_a_csv_file('./data/irregular_verbs.csv', analyzer='msarhan')
    records = collect_analyzer_results('./data/irregular_verbs_rbl_ara_report.csv', 'rbl_ara')
    records = add_new_analyzer_results(records, './data/irregular_verbs_rbl_ara_folding_report.csv', 'rbl_ara_folding')
    records = add_new_analyzer_results(records, './data/irregular_verbs_ar_std_lem_folding1_report.csv', 'ar_std_lem_folding1')
    records = add_new_analyzer_results(records, './data/irregular_verbs_ar_std_lem_folding2_report.csv', 'ar_std_lem_folding2')
    records = add_new_analyzer_results(records, './data/irregular_verbs_msarhan_report.csv', 'msarhan')
    save_report('./report_repo/irregular_verbs.json', records)
    generate_accuracy_csv('./report_repo/irregular_verbs.csv', records)


def nouns():
    process_inflection_in_a_csv_file('./data/nouns.csv', analyzer='rbl_ara')
    process_inflection_in_a_csv_file('./data/nouns.csv', analyzer='rbl_ara_folding')
    process_inflection_in_a_csv_file('./data/nouns.csv', analyzer='ar_std_lem_folding1')
    process_inflection_in_a_csv_file('./data/nouns.csv', analyzer='ar_std_lem_folding2')
    process_inflection_in_a_csv_file('./data/nouns.csv', analyzer='msarhan')
    records = collect_analyzer_results('./data/nouns_rbl_ara_report.csv', 'rbl_ara')
    records = add_new_analyzer_results(records, './data/nouns_rbl_ara_folding_report.csv', 'rbl_ara_folding')
    records = add_new_analyzer_results(records, './data/nouns_ar_std_lem_folding1_report.csv', 'ar_std_lem_folding1')
    records = add_new_analyzer_results(records, './data/nouns_ar_std_lem_folding2_report.csv', 'ar_std_lem_folding2')
    records = add_new_analyzer_results(records, './data/nouns_msarhan_report.csv', 'msarhan')
    save_report('./report_repo/nouns.json', records)
    generate_accuracy_csv('./report_repo/nouns.csv', records)


def numerals():
    process_inflection_in_a_csv_file('./data/numerals.csv', analyzer='rbl_ara')
    process_inflection_in_a_csv_file('./data/numerals.csv', analyzer='rbl_ara_folding')
    process_inflection_in_a_csv_file('./data/numerals.csv', analyzer='ar_std_lem_folding1')
    process_inflection_in_a_csv_file('./data/numerals.csv', analyzer='ar_std_lem_folding2')
    process_inflection_in_a_csv_file('./data/numerals.csv', analyzer='msarhan')
    records = collect_analyzer_results('./data/numerals_rbl_ara_report.csv', 'rbl_ara')
    records = add_new_analyzer_results(records, './data/numerals_rbl_ara_folding_report.csv', 'rbl_ara_folding')
    records = add_new_analyzer_results(records, './data/numerals_ar_std_lem_folding1_report.csv', 'ar_std_lem_folding1')
    records = add_new_analyzer_results(records, './data/numerals_ar_std_lem_folding2_report.csv', 'ar_std_lem_folding2')
    records = add_new_analyzer_results(records, './data/numerals_msarhan_report.csv', 'msarhan')
    save_report('./report_repo/numerals.json', records)
    generate_accuracy_csv('./report_repo/numerals.csv', records)


def derivation():
    process_inflection_in_a_csv_file('./data/derivation.csv', analyzer='rbl_ara')
    process_inflection_in_a_csv_file('./data/derivation.csv', analyzer='rbl_ara_folding')
    process_inflection_in_a_csv_file('./data/derivation.csv', analyzer='ar_std_lem_folding1')
    process_inflection_in_a_csv_file('./data/derivation.csv', analyzer='ar_std_lem_folding2')
    process_inflection_in_a_csv_file('./data/derivation.csv', analyzer='msarhan')
    records = collect_analyzer_results('./data/derivation_rbl_ara_report.csv', 'rbl_ara')
    records = add_new_analyzer_results(records, './data/derivation_rbl_ara_folding_report.csv', 'rbl_ara_folding')
    records = add_new_analyzer_results(records, './data/derivation_ar_std_lem_folding1_report.csv', 'ar_std_lem_folding1')
    records = add_new_analyzer_results(records, './data/derivation_ar_std_lem_folding2_report.csv', 'ar_std_lem_folding2')
    records = add_new_analyzer_results(records, './data/derivation_msarhan_report.csv', 'msarhan')
    save_report('./report_repo/derivation.json', records)
    generate_accuracy_csv('./report_repo/derivation.csv', records)


def run():
    regular_verbs()
    irregular_verbs()
    nouns()
    numerals()
    derivation()



if __name__ == '__main__':
    run()
