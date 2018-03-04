import numpy as np
from nltk.translate import IBMModel1
from nltk.translate import AlignedSent
import dill as pickle
import csv
import os
import gc
from nltk.corpus import stopwords
from api_call import api_call_funct
import json
from nltk.stem import PorterStemmer

stopWords = set(stopwords.words('english'))
ps = PorterStemmer()

bitext_part1 = []
bitext_part2 = []
bitext_part3 = []
bitext_part4 = []
bitext_part5 = []
bitext_part6 = []
bitext_part7 = []
bitext_part8 = []
bitext_part9 = []
bitext_part10 = []
mk_sentences1=[]
mk_sentences2=[]
en_sentences1=[]
en_sentences2=[]

print("START TRAINING")
if os.path.exists('MK/part2EN.pkl'):

    # print('Loading corpuses_part1')
    # with open('MK/part1EN.pkl', 'rb') as file:
    #     en_sentences1 = pickle.load(file)
    # with open('MK/part1MK.pkl', 'rb') as file:
    #     mk_sentences1 = pickle.load(file)
    #
    # print('Loading pickles_part1')
    # with open('MK/part1.pkl', 'rb') as file:
    #     bitext_part1 = pickle.load(file)
    # with open('MK/part2.pkl', 'rb') as file:
    #     bitext_part2 = pickle.load(file)
    # with open('MK/part3.pkl', 'rb') as file:
    #     bitext_part3 = pickle.load(file)
    # with open('MK/part4.pkl', 'rb') as file:
    #     bitext_part4 = pickle.load(file)
    # with open('MK/part5.pkl', 'rb') as file:
    #     bitext_part5 = pickle.load(file)
    # print('Finished loading pickles')

    print('Loading corpuses_part2')
    with open('MK/part2EN.pkl', 'rb') as file:
        en_sentences1 = pickle.load(file)
    with open('MK/part2MK.pkl', 'rb') as file:
        mk_sentences1 = pickle.load(file)

    print('Loading pickles_part2')
    with open('MK/part6.pkl', 'rb') as file:
        bitext_part6 = pickle.load(file)
    with open('MK/part7.pkl', 'rb') as file:
        bitext_part7 = pickle.load(file)
    with open('MK/part8.pkl', 'rb') as file:
        bitext_part8 = pickle.load(file)
    with open('MK/part9.pkl', 'rb') as file:
        bitext_part9 = pickle.load(file)
    with open('MK/part10.pkl', 'rb') as file:
        bitext_part10 = pickle.load(file)
    print('Finished loading pickles')
else:
    # print('Building mk corpus')
    # with open('MK/MK-EN.lower.mk', 'rt', encoding='utf8') as csvfile:
    #     reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    #     for row in reader:
    #         mk_sentences1.append(row)
    #
    # print('Building en corpus')
    # with open('MK/MK-EN.lower.en', 'rt', encoding='utf8') as csvfile:
    #     reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    #     for row in reader:
    #         en_row = []
    #         for word in row:
    #             en_row.append(ps.stem(word))
    #         en_sentences1.append(en_row)

    # print('Saving corpuses_part1')
    # with open('MK/part1MK.pkl', 'wb') as file:
    #     pickle.dump(mk_sentences1, file)
    # with open('MK/part1EN.pkl', 'wb') as file:
    #     pickle.dump(en_sentences1, file)

    with open('MK/setimes.en-mk.en.txt', 'rt', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            en_row = []
            for word in row:
                en_row.append(ps.stem(word))
            en_sentences2.append(row)

    with open('MK/setimes.en-mk.mk.txt', 'rt', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            mk_sentences2.append(row)

    print('Saving corpuses_part2')
    with open('MK/part2MK.pkl', 'wb') as file:
        pickle.dump(mk_sentences2, file)
    with open('MK/part2EN.pkl', 'wb') as file:
        pickle.dump(en_sentences2, file)

    # print('Buindlig parts_part1')
    # for index in range(0, 40000):
    #     bitext_part1.append(AlignedSent(en_sentences1[index], mk_sentences1[index]))
    # print('bitext part 1 finished')
    # for index in range(40000, 80000):
    #     bitext_part2.append(AlignedSent(en_sentences1[index], mk_sentences1[index]))
    # print('bitext part 2 finished')
    # for index in range(80000, 120000):
    #     bitext_part3.append(AlignedSent(en_sentences1[index], mk_sentences1[index]))
    # print('bitext part 3 finished')
    # for index in range(120000, 160000):
    #     bitext_part4.append(AlignedSent(en_sentences1[index], mk_sentences1[index]))
    # print('bitext part 4 finished')
    # for index in range(160000, 200000):
    #     bitext_part5.append(AlignedSent(en_sentences1[index], mk_sentences1[index]))
    # print('bitext part 5 finished')
    #
    # with open('MK/part1.pkl', 'wb') as file:
    #     pickle.dump(bitext_part1, file)
    # with open('MK/part2.pkl', 'wb') as file:
    #     pickle.dump(bitext_part2, file)
    # with open('MK/part3.pkl', 'wb') as file:
    #     pickle.dump(bitext_part3, file)
    # with open('MK/part4.pkl', 'wb') as file:
    #     pickle.dump(bitext_part4, file)

    print('Buindlig parts_part2')
    for index in range(0, 40000):
        bitext_part6.append(AlignedSent(en_sentences2[index], mk_sentences2[index]))
    print('bitext part 6 finished')
    for index in range(40000, 80000):
        bitext_part7.append(AlignedSent(en_sentences2[index], mk_sentences2[index]))
    print('bitext part 7 finished')
    for index in range(80000, 120000):
        bitext_part8.append(AlignedSent(en_sentences2[index], mk_sentences2[index]))
    print('bitext part 8 finished')
    for index in range(120000, 160000):
        bitext_part9.append(AlignedSent(en_sentences2[index], mk_sentences2[index]))
    print('bitext part 9 finished')
    for index in range(160000, 200000):
        bitext_part10.append(AlignedSent(en_sentences2[index], mk_sentences2[index]))
    print('bitext part 10 finished')

    with open('MK/part6.pkl', 'wb') as file:
        pickle.dump(bitext_part6, file)
    with open('MK/part7.pkl', 'wb') as file:
        pickle.dump(bitext_part7, file)
    with open('MK/part8.pkl', 'wb') as file:
        pickle.dump(bitext_part8, file)
    with open('MK/part9.pkl', 'wb') as file:
        pickle.dump(bitext_part9, file)
    with open('MK/part10.pkl', 'wb') as file:
        pickle.dump(bitext_part10, file)

    print("FINISHED creating parts_part2")


if os.path.exists('MK/ibm_part10.pkl') == False:
#     print('Creating ibm part 1')
#     ibm_part1 = IBMModel1(bitext_part1, 5)
#     with open('MK/ibm_part1.pkl', 'wb') as file:
#         pickle.dump(ibm_part1, file)
#
#     print('Creating ibm part 2')
#     ibm_part2 = IBMModel1(bitext_part2, 5)
#     with open('MK/ibm_part2.pkl', 'wb') as file:
#         pickle.dump(ibm_part2, file)
#
#     print('Creating ibm part 3')
#     ibm_part3 = IBMModel1(bitext_part3, 5)
#     with open('MK/ibm_part3.pkl', 'wb') as file:
#         pickle.dump(ibm_part3, file)
#
#     print('Creating ibm part 4')
#     ibm_part4 = IBMModel1(bitext_part4, 5)
#     with open('MK/ibm_part4.pkl', 'wb') as file:
#         pickle.dump(ibm_part4, file)
#
#     print('Creating ibm part 5')
#     ibm_part5 = IBMModel1(bitext_part5, 5)
#     with open('MK/ibm_part5.pkl', 'wb') as file:
#         pickle.dump(ibm_part5, file)
#     print('Saving parts_part1')
#
# print("FINISHED TRAINNING_part1")

    # print('Creating ibm part 6')
    # ibm_part6 = IBMModel1(bitext_part6, 5)
    # with open('MK/ibm_part6.pkl', 'wb') as file:
    #     pickle.dump(ibm_part6, file)
    #
    # print('Creating ibm part 7')
    # ibm_part7 = IBMModel1(bitext_part7, 5)
    # with open('MK/ibm_part7.pkl', 'wb') as file:
    #     pickle.dump(ibm_part7, file)

    # print('Creating ibm part 8')
    # ibm_part8 = IBMModel1(bitext_part8, 5)
    # with open('MK/ibm_part8.pkl', 'wb') as file:
    #     pickle.dump(ibm_part8, file)

    # print('Creating ibm part 9')
    # ibm_part9 = IBMModel1(bitext_part9, 5)
    # with open('MK/ibm_part9.pkl', 'wb') as file:
    #     pickle.dump(ibm_part9, file)

    print('Creating ibm part 10')
    ibm_part10 = IBMModel1(bitext_part10, 5)
    with open('MK/ibm_part10.pkl', 'wb') as file:
        pickle.dump(ibm_part10, file)
    print('Saving parts_part2')

print("FINISHED TRAINNING_part2")


if os.path.exists('MK/mk_words2.pkl'):
    print('Loading mk words1')
    with open('MK/mk_words.pkl', 'rb') as file:
        mk_words = pickle.load(file)
    print('Loading mk words2')
    with open('MK/mk_words2.pk1', 'rb') as file:
        mk_words2 = pickle.load(file)

else:
    mk_words=set()
    en_words = set()
    for sentence in en_sentences1:
        words_set=set(sentence)
        for word in words_set:
            en_words.add(word)
    en_words=set(en_words)
    with open('MK/en_words.pkl', 'wb') as file:
        pickle.dump(en_words, file)

    for sentence in mk_sentences1:
        words_set=set(sentence)
        for word in words_set:
            if word not in en_words and word not in stopWords:
                mk_words.add(word)
    mk_words=set(mk_words)
    with open('MK/mk_words.pkl', 'wb') as file:
        pickle.dump(mk_words, file)

    mk_words2=set()
    en_words2 = set()
    for sentence in en_sentences2:
        words_set=set(sentence)
        for word in words_set:
            en_words2.add(word)
    en_words2=set(en_words2)
    with open('MK/en_words2.pkl', 'wb') as file:
        pickle.dump(en_words2, file)

    for sentence in mk_sentences2:
        words_set=set(sentence)
        for word in words_set:
            if word not in en_words and word not in stopWords:
                mk_words2.add(word)
    mk_words2=set(mk_words2)
    with open('MK/mk_words2.pkl', 'wb') as file:
        pickle.dump(mk_words2, file)


del mk_sentences1, en_sentences1, bitext_part1, bitext_part2, bitext_part3, bitext_part4, bitext_part5, mk_sentences2, en_sentences2, bitext_part6, bitext_part7, bitext_part8, bitext_part9, bitext_part10
gc.collect()

titles = api_call_funct()

temp_sentence = ""
dict = {}

print("TRANSLATING SENTENCE")

file_names = ['MK/ibm_part1.pkl', 'MK/ibm_part2.pkl', 'MK/ibm_part3.pkl', 'MK/ibm_part4.pkl', 'MK/ibm_part5.pkl', 'MK/ibm_part6.pkl', 'MK/ibm_part7.pkl', 'MK/ibm_part8.pkl', 'MK/ibm_part9.pkl', 'MK/ibm_part10.pkl']

for file_name in file_names:
    print('Loading %s' %file_name)
    with open(file_name, 'rb') as file:
        ibm_part = pickle.load(file)
    print('Translating...')
    for source_sentence in titles:
        print(source_sentence)
        source_sentence = source_sentence.lower()
        temp_sentence = source_sentence
        sentence_words=source_sentence.split(' ')
        tranlated_sentence=['' for w in range(0, len(sentence_words))]
        translated_sentence_probabilities = [0 for x in range(0, len(sentence_words))]
        word_index = 0
        stop_words_number = 0
        for sentence_word in sentence_words:
            if sentence_word not in stopWords:
                max_prob=0
                translated_word=''
                for word in mk_words:
                    prob = ibm_part.translation_table[ps.stem(sentence_word)][word]
                    if prob>max_prob:
                        max_prob=prob
                        translated_word=word
                print(max_prob)
                print(translated_word)
                if (max_prob <= 0.35):
                    translated_word = 'unknown'
                if max_prob > translated_sentence_probabilities[word_index]:
                    tranlated_sentence[word_index] = translated_word
                    translated_sentence_probabilities[word_index] = max_prob
                word_index += 1
            else:
                stop_words_number += 1
        print(tranlated_sentence)
        dict[temp_sentence] = tranlated_sentence[:(len(tranlated_sentence) - stop_words_number)]

print(dict)
with open('translation.txt', 'w', encoding='utf8') as file:
    file.write(json.dumps(dict, ensure_ascii=False))

