from nltk.translate import IBMModel2
from nltk.translate import AlignedSent
import dill as pickle
import csv
import os
import gc
from nltk.corpus import stopwords
from math import log

stopWords = set(stopwords.words('english'))

bitext_part1 = []
bitext_part2 = []
bitext_part3 = []
bitext_part4 = []
bitext_part5 = []
mk_sentences1=[]
mk_sentences2=[]
en_sentences1=[]
en_sentences2=[]

print("START TRAINING")
if os.path.exists('jajksdkhk.pkl'):
    print('Loading pickles')
    # with open('part1.pkl', 'rb') as file:
    #     bitext_part1 = pickle.load(file)
    # with open('part2.pkl', 'rb') as file:
    #     bitext_part2 = pickle.load(file)
    # with open('part3.pkl', 'rb') as file:
    #     bitext_part3 = pickle.load(file)
    with open('part1EN.pkl', 'rb') as file:
        en_sentences1 = pickle.load(file)
    with open('part1MK.pkl', 'rb') as file:
         mk_sentences1 = pickle.load(file)
    # with open('part4.pkl', 'rb') as file:
    #     bitext_part4 = pickle.load(file)
    # with open('part5.pkl', 'rb') as file:
    #     bitext_part5 = pickle.load(file)
    # print('Finished loading pickles')
else:
    with open('MK-EN.lower.mk', 'rt', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            mk_sentences1.append(row)

    with open('MK-EN.lower.en', 'rt', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            en_sentences1.append(row)

    # with open('setimes.en-mk.en.txt', 'rt', encoding='utf8') as csvfile:
    #     reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    #     for row in reader:
    #         en_sentences2.append(row)
    #
    # with open('setimes.en-mk.mk.txt', 'rt', encoding='utf8') as csvfile:
    #     reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    #     for row in reader:
    #         mk_sentences2.append(row)

    # with open('part1MK.pkl', 'wb') as file:
    #     pickle.dump(mk_sentences1, file)
    # with open('part1EN.pkl', 'wb') as file:
    #     pickle.dump(en_sentences1, file)


    for index in range(0, 20000):
        bitext_part1.append(AlignedSent(en_sentences1[index], mk_sentences1[index]))
    print('bitext part 1 finished')
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

    # with open('part1.pkl', 'wb') as file:
    #     pickle.dump(bitext_part1, file)
    # with open('part2.pkl', 'wb') as file:
    #     pickle.dump(bitext_part2, file)
    # with open('part3.pkl', 'wb') as file:
    #     pickle.dump(bitext_part3, file)
    # with open('part4.pkl', 'wb') as file:
    #     pickle.dump(bitext_part4, file)
    # with open('part5.pkl', 'wb') as file:
    #     pickle.dump(bitext_part5, file)
# print(len(mk_sentences))
# print(len(en_sentences))

print("FINISHED creating parts")

# if os.path.exists('ibm_part1.pkl'):
#     print('Loading ibm model 1')
#     with open('ibm_part1.pkl', 'rb') as file:
#         ibm_part1 = pickle.load(file)
#     print('Loading ibm model 2')
#     with open('ibm_part2.pkl', 'rb') as file:
#         ibm_part2 = pickle.load(file)
#     print('Loading ibm model 3')
#     with open('ibm_part3.pkl', 'rb') as file:
#         ibm_part3 = pickle.load(file)
#     # with open('ibm_part4.pkl', 'rb') as file:
#     #     ibm_part4 = pickle.load(file)
#     # with open('ibm_part5.pkl', 'rb') as file:
#     #     ibm_part5 = pickle.load(file)
# else:
    #bitext = bitext_part1+bitext_part2+bitext_part3#+bitext_part4+bitext_part5
print('Creating ibm part 1')
ibm_part1 = IBMModel2(bitext_part1, 5)
    # with open('ibm_part1.pkl', 'wb') as file:
    #     pickle.dump(ibm_part1, file)
    #
    # print('Creating ibm part 2')
    # ibm_part2 = IBMModel2(bitext_part2, 5)
    # with open('ibm_part2.pkl', 'wb') as file:
    #     pickle.dump(ibm_part2, file)
    #
    # print('Creating ibm part 3')
    # ibm_part3 = IBMModel2(bitext_part3, 5)
    # with open('ibm_part3.pkl', 'wb') as file:
    #     pickle.dump(ibm_part3, file)
    #
    # print('Creating ibm part 4')
    # ibm_part4 = IBMModel2(bitext_part4, 5)
    # with open('ibm_part4.pkl', 'wb') as file:
    #     pickle.dump(ibm_part4, file)
    #
    # print('Creating ibm part 5')
    # ibm_part5 = IBMModel2(bitext_part5, 5)
    # with open('ibm_part5.pkl', 'wb') as file:
    #     pickle.dump(ibm_part5, file)
    # print('Saving parts')


print("FINISHED TRAINNING")
#print('{0:.3f}'.format(ibm1.translation_table['police']['полиција']))
#print('{0:.3f}'.format(ibm1.translation_table['police']['пожарна'])
if os.path.exists('mk_words.pkl'):
    print('Loading mk words')
    with open('mk_words.pkl', 'rb') as file:
        mk_words = pickle.load(file)
else:
    mk_words=set()
    en_words = set()
    for sentence in en_sentences1:
        words_set=set(sentence)
        for word in words_set:
            en_words.add(word)
    en_words=set(mk_words)
    with open('en_words.pkl', 'wb') as file:
        pickle.dump(en_words, file)

    for sentence in mk_sentences1:
        words_set=set(sentence)
        for word in words_set:
            if word not in en_words and word not in stopWords:
                mk_words.add(word)
    mk_words=set(mk_words)
    with open('mk_words.pkl', 'wb') as file:
        pickle.dump(mk_words, file)


# del mk_sentences1, en_sentences1, bitext_part1, bitext_part2, bitext_part3, bitext_part4, bitext_part5, mk_sentences2, en_sentences2
# gc.collect()

print("TRANSLATING SENTENCE")
sentence_example='Federer into finals after Chung retire'
sentence_example = sentence_example.lower()
sentence_words=sentence_example.split(' ')
tranlated_sentence=[]
i=0
translated_sentence_probabilities = []
for sentence_word in sentence_words:
    i += 1
    if sentence_word not in stopWords:
        max_prob=0
        translated_word=''
        for word in mk_words:
            prob1 = ibm_part1.translation_table[sentence_word][word]
            align1 = ibm_part1.alignment_table[i][i][len(sentence_words)][len(sentence_words)]
            #prob2 = ibm_part2.translation_table[sentence_word][word]
            #prob3 = ibm_part3.translation_table[sentence_word][word]
            #prob4 = ibm_part4.translation_table[sentence_word][word]
            #prob5 = ibm_part5.translation_table[sentence_word][word]
            #probArr = [prob1, prob2, prob3]
            # del max_prob, probArr, prob1, prob2, prob3, translated_word
            # gc.collect()
            maxP = log(prob1)+log(align1)
            if maxP>max_prob:
                max_prob=maxP
                translated_word=word
        print(max_prob)
        print(translated_word)
        if (max_prob >= 0.35):
            tranlated_sentence.append(translated_word)
        else:
            tranlated_sentence.append('unknown')
        translated_sentence_probabilities.append(max_prob)

# del ibm_part1, ibm_part2, ibm_part3
# gc.collect()
# print('Memory dealocated')
#
# with open('ibm_part4.pkl', 'rb') as file:
#     ibm_part4 = pickle.load(file)
# with open('ibm_part5.pkl', 'rb') as file:
#     ibm_part5 = pickle.load(file)
# print('Finished loading')
#
# tranlated_sentence2=[]
# translated_sentence_probabilities2 = []
# for sentence_word in sentence_words:
#     if sentence_word not in stopWords:
#         max_prob=0
#         translated_word=''
#         for word in mk_words:
#             prob4 = ibm_part4.translation_table[sentence_word][word]
#             prob5 = ibm_part5.translation_table[sentence_word][word]
#             probArr = [prob4, prob5]
#             maxP = max(probArr)
#             if maxP>max_prob:
#                 max_prob=maxP
#                 translated_word=word
#         print(max_prob)
#         print(translated_word)
#         if (max_prob >= 0.35):
#             tranlated_sentence2.append(translated_word)
#         else:
#             tranlated_sentence2.append('unknown')
#         translated_sentence_probabilities2.append(max_prob)
#
# for i in range(0, len(translated_sentence_probabilities)):
#     if translated_sentence_probabilities[i]<=translated_sentence_probabilities2[i]:
#         tranlated_sentence[i] = tranlated_sentence2[i]
#
# print(ibm_part4.translation_table['of']['од'])
# print(ibm_part5.translation_table['of']['од'])

print(tranlated_sentence)

