# -*- coding: utf-8 -*-

from runAnalyzer import *
from pipeline import *

def regular_verbs():
    # process_inflection_in_a_csv_file('./data/regular_verbs.csv', analyzer='rbl_ara')
    # process_inflection_in_a_csv_file('./data/regular_verbs.csv', analyzer='rbl_ara_folding')
    # process_inflection_in_a_csv_file('./data/regular_verbs.csv', analyzer='ar_std_lem_folding1')
    # process_inflection_in_a_csv_file('./data/regular_verbs.csv', analyzer='ar_std_lem_folding2')
    process_inflection_in_a_csv_file('./data/regular_verbs.csv', analyzer='ar_std_lem')
    # process_inflection_in_a_csv_file('./data/regular_verbs.csv', analyzer='msarhan')
    records = collect_analyzer_results('./data/regular_verbs_ar_std_lem_report.csv', 'ar_std_lem')
    # records = add_new_analyzer_results(records, './data/regular_verbs_rbl_ara_folding_report.csv', 'rbl_ara_folding')
    # records = add_new_analyzer_results(records, './data/regular_verbs_ar_std_lem_folding1_report.csv', 'ar_std_lem_folding1')
    # records = add_new_analyzer_results(records, './data/regular_verbs_ar_std_lem_folding2_report.csv', 'ar_std_lem_folding2')
    # records = add_new_analyzer_results(records, './data/regular_verbs_msarhan_report.csv', 'msarhan')
    # records = add_new_analyzer_results(records, './data/regular_verbs_ara_hunspell_report.csv', 'ara_hunspell')
    save_report('./report_repo/regular_verbs.json', records)
    generate_accuracy_csv('./report_repo/regular_verbs.csv', records)


def irregular_verbs():
    # process_inflection_in_a_csv_file('./data/irregular_verbs.csv', analyzer='rbl_ara')
    # process_inflection_in_a_csv_file('./data/irregular_verbs.csv', analyzer='rbl_ara_folding')
    # process_inflection_in_a_csv_file('./data/irregular_verbs.csv', analyzer='ar_std_lem_folding1')
    # process_inflection_in_a_csv_file('./data/irregular_verbs.csv', analyzer='ar_std_lem_folding2')
    process_inflection_in_a_csv_file('./data/irregular_verbs.csv', analyzer='ar_std_lem')
    # process_inflection_in_a_csv_file('./data/irregular_verbs.csv', analyzer='msarhan')
    records = collect_analyzer_results('./data/irregular_verbs_ar_std_lem_report.csv', 'ar_std_lem')
    # records = add_new_analyzer_results(records, './data/irregular_verbs_rbl_ara_folding_report.csv', 'rbl_ara_folding')
    # records = add_new_analyzer_results(records, './data/irregular_verbs_ar_std_lem_folding1_report.csv', 'ar_std_lem_folding1')
    # records = add_new_analyzer_results(records, './data/irregular_verbs_ar_std_lem_folding2_report.csv', 'ar_std_lem_folding2')
    # records = add_new_analyzer_results(records, './data/irregular_verbs_msarhan_report.csv', 'msarhan')
    # records = add_new_analyzer_results(records, './data/irregular_verbs_ara_hunspell_report.csv', 'ara_hunspell')
    save_report('./report_repo/irregular_verbs.json', records)
    generate_accuracy_csv('./report_repo/irregular_verbs.csv', records)


def nouns():
    # process_inflection_in_a_csv_file('./data/nouns.csv', analyzer='rbl_ara')
    # process_inflection_in_a_csv_file('./data/nouns.csv', analyzer='rbl_ara_folding')
    # process_inflection_in_a_csv_file('./data/nouns.csv', analyzer='ar_std_lem_folding1')
    # process_inflection_in_a_csv_file('./data/nouns.csv', analyzer='ar_std_lem_folding2')
    process_inflection_in_a_csv_file('./data/nouns.csv', analyzer='ar_std_lem')
    # process_inflection_in_a_csv_file('./data/nouns.csv', analyzer='msarhan')
    records = collect_analyzer_results('./data/nouns_ar_std_lem_report.csv', 'ar_std_lem')
    # records = add_new_analyzer_results(records, './data/nouns_rbl_ara_folding_report.csv', 'rbl_ara_folding')
    # records = add_new_analyzer_results(records, './data/nouns_ar_std_lem_folding1_report.csv', 'ar_std_lem_folding1')
    # records = add_new_analyzer_results(records, './data/nouns_ar_std_lem_folding2_report.csv', 'ar_std_lem_folding2')
    # records = add_new_analyzer_results(records, './data/nouns_msarhan_report.csv', 'msarhan')
    # records = add_new_analyzer_results(records, './data/nouns_ara_hunspell_report.csv', 'ara_hunspell')
    save_report('./report_repo/nouns.json', records)
    generate_accuracy_csv('./report_repo/nouns.csv', records)


def numerals():
    # process_inflection_in_a_csv_file('./data/numerals.csv', analyzer='rbl_ara')
    # process_inflection_in_a_csv_file('./data/numerals.csv', analyzer='rbl_ara_folding')
    # process_inflection_in_a_csv_file('./data/numerals.csv', analyzer='ar_std_lem_folding1')
    # process_inflection_in_a_csv_file('./data/numerals.csv', analyzer='ar_std_lem_folding2')
    process_inflection_in_a_csv_file('./data/numerals.csv', analyzer='ar_std_lem')
    # process_inflection_in_a_csv_file('./data/numerals.csv', analyzer='msarhan')
    records = collect_analyzer_results('./data/numerals_ar_std_lem_report.csv', 'ar_std_lem')
    # records = add_new_analyzer_results(records, './data/numerals_rbl_ara_folding_report.csv', 'rbl_ara_folding')
    # records = add_new_analyzer_results(records, './data/numerals_ar_std_lem_folding1_report.csv', 'ar_std_lem_folding1')
    # records = add_new_analyzer_results(records, './data/numerals_ar_std_lem_folding2_report.csv', 'ar_std_lem_folding2')
    # records = add_new_analyzer_results(records, './data/numerals_msarhan_report.csv', 'msarhan')
    # records = add_new_analyzer_results(records, './data/numerals_ara_hunspell_report.csv', 'ara_hunspell')
    save_report('./report_repo/numerals.json', records)
    generate_accuracy_csv('./report_repo/numerals.csv', records)


def derivation():
    # process_inflection_in_a_csv_file('./data/derivation.csv', analyzer='rbl_ara')
    # process_inflection_in_a_csv_file('./data/derivation.csv', analyzer='rbl_ara_folding')
    # process_inflection_in_a_csv_file('./data/derivation.csv', analyzer='ar_std_lem_folding1')
    # process_inflection_in_a_csv_file('./data/derivation.csv', analyzer='ar_std_lem_folding2')
    process_inflection_in_a_csv_file('./data/derivation.csv', analyzer='ar_std_lem')
    # process_inflection_in_a_csv_file('./data/derivation.csv', analyzer='msarhan')
    records = collect_analyzer_results('./data/derivation_ar_std_lem_report.csv', 'ar_std_lem')
    # records = add_new_analyzer_results(records, './data/derivation_rbl_ara_folding_report.csv', 'rbl_ara_folding')
    # records = add_new_analyzer_results(records, './data/derivation_ar_std_lem_folding1_report.csv', 'ar_std_lem_folding1')
    # records = add_new_analyzer_results(records, './data/derivation_ar_std_lem_folding2_report.csv', 'ar_std_lem_folding2')
    # records = add_new_analyzer_results(records, './data/derivation_msarhan_report.csv', 'msarhan')
    # records = add_new_analyzer_results(records, './data/derivation_ara_hunspell_report.csv', 'ara_hunspell')
    save_report('./report_repo/derivation.json', records)
    generate_accuracy_csv('./report_repo/derivation.csv', records)


def derivation_for_inaccuracy():
    # process_inflection_in_a_csv_file('./data/derivation2.csv', analyzer='rbl_ara')
    # process_inflection_in_a_csv_file('./data/derivation2.csv', analyzer='rbl_ara_folding')
    # process_inflection_in_a_csv_file('./data/derivation2.csv', analyzer='ar_std_lem_folding1')
    # process_inflection_in_a_csv_file('./data/derivation2.csv', analyzer='ar_std_lem_folding2')
    process_inflection_in_a_csv_file('./data/derivation2.csv', analyzer='ar_std_lem')
    # process_inflection_in_a_csv_file('./data/derivation2.csv', analyzer='msarhan')
    records = collect_analyzer_results('./data/derivation2_ar_std_lem_report.csv', 'ar_std_lem')
    # records = add_new_analyzer_results(records, './data/derivation2_rbl_ara_folding_report.csv', 'rbl_ara_folding')
    # records = add_new_analyzer_results(records, './data/derivation2_ar_std_lem_folding1_report.csv', 'ar_std_lem_folding1')
    # records = add_new_analyzer_results(records, './data/derivation2_ar_std_lem_folding2_report.csv', 'ar_std_lem_folding2')
    # records = add_new_analyzer_results(records, './data/derivation2_msarhan_report.csv', 'msarhan')
    # records = add_new_analyzer_results(records, './data/derivation2_ara_hunspell_report.csv', 'ara_hunspell')
    save_report('./report_repo/derivation2.json', records)
    generate_accuracy_csv('./report_repo/derivation2.csv', records)


def verbs_imperative():
    process_inflection_in_a_csv_file('./data/verbs_imperative_form.csv', analyzer='ar_std_lem')
    process_inflection_in_a_csv_file('./data/verbs_imperative_form.csv', analyzer='rbl_ara')
    process_inflection_in_a_csv_file('./data/verbs_imperative_form.csv', analyzer='rbl_ara_folding')
    records = collect_analyzer_results('./data/verbs_imperative_form_ar_std_lem_report.csv', 'ar_std_lem')
    records = add_new_analyzer_results(records, './data/verbs_imperative_form_rbl_ara_report.csv', 'rbl_ara')
    records = add_new_analyzer_results(records, './data/verbs_imperative_form_rbl_ara_folding_report.csv', 'rbl_ara_folding')
    save_report('./report_repo/verbs_imperative_form.json', records)
    generate_accuracy_csv('./report_repo/verbs_imperative_form.csv', records)


def verbs_past_tense():
    process_inflection_in_a_csv_file('./data/verbs_past_tense.csv', analyzer='ar_std_lem')
    process_inflection_in_a_csv_file('./data/verbs_past_tense.csv', analyzer='rbl_ara')
    process_inflection_in_a_csv_file('./data/verbs_past_tense.csv', analyzer='rbl_ara_folding')
    records = collect_analyzer_results('./data/verbs_past_tense_ar_std_lem_report.csv', 'ar_std_lem')
    records = add_new_analyzer_results(records, './data/verbs_past_tense_rbl_ara_report.csv', 'rbl_ara')
    records = add_new_analyzer_results(records, './data/verbs_past_tense_rbl_ara_folding_report.csv', 'rbl_ara_folding')
    save_report('./report_repo/verbs_past_tense.json', records)
    generate_accuracy_csv('./report_repo/verbs_past_tense.csv', records)


def verbs_present_tense():
    process_inflection_in_a_csv_file('./data/verbs_present_tense.csv', analyzer='ar_std_lem')
    process_inflection_in_a_csv_file('./data/verbs_present_tense.csv', analyzer='rbl_ara')
    process_inflection_in_a_csv_file('./data/verbs_present_tense.csv', analyzer='rbl_ara_folding')
    records = collect_analyzer_results('./data/verbs_present_tense_ar_std_lem_report.csv', 'ar_std_lem')
    records = add_new_analyzer_results(records, './data/verbs_present_tense_rbl_ara_report.csv', 'rbl_ara')
    records = add_new_analyzer_results(records, './data/verbs_present_tense_rbl_ara_folding_report.csv', 'rbl_ara_folding')
    save_report('./report_repo/verbs_present_tense.json', records)
    generate_accuracy_csv('./report_repo/verbs_present_tense.csv', records)


def nouns_combined_wiz_possessive_pronoun():
    process_inflection_in_a_csv_file('./data/nouns_combined_wiz_possessive_pronoun.csv', analyzer='ar_std_lem')
    process_inflection_in_a_csv_file('./data/nouns_combined_wiz_possessive_pronoun.csv', analyzer='rbl_ara')
    process_inflection_in_a_csv_file('./data/nouns_combined_wiz_possessive_pronoun.csv', analyzer='rbl_ara_folding')
    records = collect_analyzer_results('./data/nouns_combined_wiz_possessive_pronoun_ar_std_lem_report.csv', 'ar_std_lem')
    records = add_new_analyzer_results(records, './data/nouns_combined_wiz_possessive_pronoun_rbl_ara_report.csv', 'rbl_ara')
    records = add_new_analyzer_results(records, './data/nouns_combined_wiz_possessive_pronoun_rbl_ara_folding_report.csv', 'rbl_ara_folding')
    save_report('./report_repo/nouns_combined_wiz_possessive_pronoun.json', records)
    generate_accuracy_csv('./report_repo/nouns_combined_wiz_possessive_pronoun.csv', records)


def nouns_with_pronouns():
    process_inflection_in_a_csv_file('./data/nouns_with_pronouns.csv', analyzer='ar_std_lem')
    process_inflection_in_a_csv_file('./data/nouns_with_pronouns.csv', analyzer='rbl_ara')
    process_inflection_in_a_csv_file('./data/nouns_with_pronouns.csv', analyzer='rbl_ara_folding')
    records = collect_analyzer_results('./data/nouns_with_pronouns_ar_std_lem_report.csv', 'ar_std_lem')
    records = add_new_analyzer_results(records, './data/nouns_with_pronouns_rbl_ara_report.csv', 'rbl_ara')
    records = add_new_analyzer_results(records, './data/nouns_with_pronouns_rbl_ara_folding_report.csv', 'rbl_ara_folding')
    save_report('./report_repo/nouns_with_pronouns.json', records)
    generate_accuracy_csv('./report_repo/nouns_with_pronouns.csv', records)



def nouns_singular_form():
    process_inflection_in_a_csv_file('./data/nouns_singular_form.csv', analyzer='ar_std_lem')
    process_inflection_in_a_csv_file('./data/nouns_singular_form.csv', analyzer='rbl_ara')
    process_inflection_in_a_csv_file('./data/nouns_singular_form.csv', analyzer='rbl_ara_folding')
    records = collect_analyzer_results('./data/nouns_singular_form_ar_std_lem_report.csv', 'ar_std_lem')
    records = add_new_analyzer_results(records, './data/nouns_singular_form_rbl_ara_report.csv', 'rbl_ara')
    records = add_new_analyzer_results(records, './data/nouns_singular_form_rbl_ara_folding_report.csv', 'rbl_ara_folding')
    save_report('./report_repo/nouns_singular_form.json', records)
    generate_accuracy_csv('./report_repo/nouns_singular_form.csv', records)


def nouns_pluarl_form():
    process_inflection_in_a_csv_file('./data/nouns_pluarl_form.csv', analyzer='ar_std_lem')
    process_inflection_in_a_csv_file('./data/nouns_pluarl_form.csv', analyzer='rbl_ara')
    process_inflection_in_a_csv_file('./data/nouns_pluarl_form.csv', analyzer='rbl_ara_folding')
    records = collect_analyzer_results('./data/nouns_pluarl_form_ar_std_lem_report.csv', 'ar_std_lem')
    records = add_new_analyzer_results(records, './data/nouns_pluarl_form_rbl_ara_report.csv', 'rbl_ara')
    records = add_new_analyzer_results(records, './data/nouns_pluarl_form_rbl_ara_folding_report.csv', 'rbl_ara_folding')
    save_report('./report_repo/nouns_pluarl_form.json', records)
    generate_accuracy_csv('./report_repo/nouns_pluarl_form.csv', records)


def nouns_with_article():
    process_inflection_in_a_csv_file('./data/nouns_with_article.csv', analyzer='ar_std_lem')
    process_inflection_in_a_csv_file('./data/nouns_with_article.csv', analyzer='rbl_ara')
    records = collect_analyzer_results('./data/nouns_with_article_ar_std_lem_report.csv', 'ar_std_lem')
    records = add_new_analyzer_results(records, './data/nouns_with_article_rbl_ara_report.csv', 'rbl_ara')
    save_report('./report_repo/nouns_with_article.json', records)
    generate_accuracy_csv('./report_repo/nouns_with_article.csv', records)


def nouns_singular_plual_and_article():
    process_inflection_in_a_csv_file('./data/nouns_singual_plual_and_article.csv', analyzer='ar_std_lem')
    process_inflection_in_a_csv_file('./data/nouns_singual_plual_and_article.csv', analyzer='rbl_ara')
    process_inflection_in_a_csv_file('./data/nouns_singual_plual_and_article.csv', analyzer='rbl_ara_folding')
    records = collect_analyzer_results('./data/nouns_singual_plual_and_article_ar_std_lem_report.csv', 'ar_std_lem')
    records = add_new_analyzer_results(records, './data/nouns_singual_plual_and_article_rbl_ara_report.csv', 'rbl_ara')
    records = add_new_analyzer_results(records, './data/nouns_singual_plual_and_article_rbl_ara_folding_report.csv', 'rbl_ara_folding')
    save_report('./report_repo/nouns_singual_plual_and_article.json', records)
    generate_accuracy_csv('./report_repo/nouns_singual_plual_and_article.csv', records)


def preposistion():
    process_inflection_in_a_csv_file('./data/preposition.csv', analyzer='ar_std_lem')
    process_inflection_in_a_csv_file('./data/preposition.csv', analyzer='rbl_ara')
    process_inflection_in_a_csv_file('./data/preposition.csv', analyzer='rbl_ara_folding')
    records = collect_analyzer_results('./data/preposition_ar_std_lem_report.csv', 'ar_std_lem')
    records = add_new_analyzer_results(records, './data/preposition_rbl_ara_report.csv', 'rbl_ara')
    records = add_new_analyzer_results(records, './data/preposition_rbl_ara_folding_report.csv', 'rbl_ara_folding')
    save_report('./report_repo/preposition.json', records)
    generate_accuracy_csv('./report_repo/preposition.csv', records)



def run_old():
    regular_verbs()
    irregular_verbs()
    nouns()
    numerals()
    derivation()
    derivation_for_inaccuracy()


def run():
    verbs_imperative()
    verbs_past_tense()
    verbs_present_tense()
    nouns_combined_wiz_possessive_pronoun()
    nouns_with_pronouns()
    # nouns_singular_form()
    # nouns_pluarl_form()
    # nouns_with_article()
    nouns_singular_plual_and_article()
    preposistion()



if __name__ == '__main__':
    run()
