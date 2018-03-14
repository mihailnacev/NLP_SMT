from collections import defaultdict
from math import log
import csv
from nltk.translate import PhraseTable, StackDecoder
from nltk.translate import bleu_score

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
input_sentence="he said that macedonian women were victims involved in prostitution during a recent sweep in bulgaria"
with open("translation.txt", 'a', encoding='utf8') as file:
    print("Input sentence: "+input_sentence)
    file.write("Input sentence: "+input_sentence+"\n")
    input_words=input_sentence.split(' ')
    translated_sentence=[]
    temp_sentence=[]
    previous_temp=[]
    iteration_index=0
    for i in range(0, len(input_words)):
        temp_sentence.append(input_words[i])
        translated_temp=stack_decoder.translate(temp_sentence)
        print(translated_temp)
        iteration_index+=1
        file.write("Iteration "+str(iteration_index)+": "+str(' '.join(translated_temp))+"\n")
        if len(translated_temp)==0:
            temp_sentence=[]
            for word in previous_temp:
                translated_sentence.append(word)
            translated_sentence.append('_')
            translated_temp=[]
        previous_temp=translated_temp
    if len(translated_sentence)==0:
        translated_sentence = translated_temp

    print("Translated sentence: "+str(' '.join(translated_sentence)))
    file.write("Translated sentence: "+str(' '.join(translated_sentence))+"\n")
    mk_sentences=[]
    with open('smt/phrase/MK-EN.lower.mk', 'rt', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            mk_sentences.append(row)
    file.write("BLEU score: %f" %(bleu_score.sentence_bleu(references=mk_sentences, hypothesis=translated_sentence, weights=(0.5, 0.5)))+"\n")
    print("BLEU score: %f" %(bleu_score.sentence_bleu(references=mk_sentences, hypothesis=translated_sentence, weights=(0.5, 0.5))))

