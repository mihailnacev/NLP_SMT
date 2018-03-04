from collections import defaultdict
from math import log
import csv
from nltk.translate import PhraseTable, StackDecoder

phrase_table=PhraseTable()
with open('smt/phrase/phrases_full.txt', 'rt', encoding='utf8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in reader:
        parts=row[0].split('->')
        mk_phrase=parts[0]
        en_phrase=parts[1]
        prob=float(parts[2])
        mk_phrase_parts=tuple(mk_phrase.lstrip().rstrip().split(' '))
        en_phrase_parts=tuple(en_phrase.lstrip().rstrip().split(' '))
        phrase_table.add(en_phrase_parts, mk_phrase_parts, prob)

language_prob = defaultdict(lambda: -999.0)
language_model = type('',(object,),{'probability_change': lambda self, context, phrase: language_prob[phrase], 'probability': lambda self, phrase: language_prob[phrase]})()
stack_decoder=StackDecoder(phrase_table, language_model)
print(stack_decoder.translate(['macedonian', 'women', 'and', 'children', 'church', 'because', 'sweep']))
