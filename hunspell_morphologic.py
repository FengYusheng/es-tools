# -*- coding: utf-8 -*-
import os
import csv

import hunspell

def analyze(csv_source, csv_report):
    hobj = hunspell.HunSpell(
        '/home/skywalker/dev-kit/es/elasticsearch-6.2.1/config/hunspell/mozilla_AR/ar.dic',
        '/home/skywalker/dev-kit/es/elasticsearch-6.2.1/config/hunspell/mozilla_AR/ar.aff'
    )

    with open(csv_report, 'w') as report:
        report_writer = csv.DictWriter(report, fieldnames=['Original', 'Inflection', 'Morpho'])
        report_writer.writeheader()
        with open(csv_source, 'r') as source:
            source_reader = csv.DictReader(source)
            for row in source_reader:
                message = hobj.analyze(row['Inflection'])
                message = [i.decode('utf-8') for i in message]
                report_writer.writerow({'Original':row['Original'], 'Inflection':row['Inflection'], 'Morpho':message})


if __name__ == '__main__':
    analyze('./data/verbs_present_tense.csv',
            './report_repo/verbs_present_tense_with_morph.csv')

    analyze(
        './data/verbs_past_tense.csv',
        './report_repo/verbs_past_tense_with_morpho.csv'
    )

    analyze(
        './data/verbs_imperative_form.csv',
        './report_repo/verbs_imperative_form_with_morph.csv'
    )

    analyze(
        './data/nouns_combined_wiz_possessive_pronoun.csv',
        './report_repo/nouns_combined_wiz_possessive_pronoun_with_morph.csv'
    )

    analyze(
        './data/nouns_with_pronouns.csv',
        './report_repo/nouns_with_pronouns_with_morph.csv'
    )

    analyze(
        './data/nouns_singular_form.csv',
        './report_repo/nouns_singular_form_with_morph.csv'
    )

    analyze(
        './data/nouns_pluarl_form.csv',
        './report_repo/nouns_pluarl_form_with_morph.csv'
    )

    # analyze(
    #     './data/nouns_with_article.csv',
    #     './report_repo/nouns_with_article_with_morph.csv'
    # )

    analyze(
        './data/nouns_singual_plual_and_article.csv',
        './report_repo/nouns_singual_plual_and_article_with_morph.csv'
    )

    analyze(
        './data/preposition.csv',
        './report_repo/preposition_with_morph.csv'
    )
