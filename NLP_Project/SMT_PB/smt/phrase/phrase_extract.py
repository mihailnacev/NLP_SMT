#! /usr/bin/env python
# coding:utf-8


def phrase_extract(es, fs, alignment):
    ext = extract(es, fs, alignment)
    ind = {((x, y), (z, w)) for x, y, z, w in ext}
    es = tuple(es)
    fs = tuple(fs)
    return {(es[e_s-1:e_e], fs[f_s-1:f_e])
            for (e_s, e_e), (f_s, f_e) in ind}


def extract(es, fs, alignment):
    phrases = set()
    len_es = len(es)
    for e_start in range(1, len_es+1):
        for e_end in range(e_start, len_es+1):
            # find the minimally matching foreign phrase
            f_start, f_end = (len(fs), 0)
            for (e, f) in alignment:
                if e_start <= e <= e_end:
                    f_start = min(f, f_start)
                    f_end = max(f, f_end)
            phrases.update(_extract(es, fs, e_start,
                                    e_end, f_start,
                                    f_end, alignment))
    return phrases


def _extract(es, fs, e_start, e_end, f_start, f_end, alignment):
    if f_end == 0:
        return {}
    for (e, f) in alignment:
        if (f_start <= f <= f_end) and (e < e_start or e > e_end):
            return {}
    ex = set()
    f_s = f_start
    while True:
        f_e = f_end
        while True:
            ex.add((e_start, e_end, f_s, f_e))
            f_e += 1
            if f_e in list(zip(*alignment))[1] or f_e > len(fs):
                break
        f_s -= 1
        if f_s in list(zip(*alignment))[1] or f_s < 1:
            break
    return ex


def available_phrases(fs, phrases):
    available = set()
    for i, f in enumerate(fs):
        f_rest = ()
        for fr in fs[i:]:
            f_rest += (fr,)
            if f_rest in phrases:
                available.add(tuple(enumerate(f_rest, i+1)))
    return available

from string import punctuation
def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)


if __name__ == '__main__':

    # test2
    from SMT_PB.smt.utils.utility import mkcorpus
    from SMT_PB.smt.phrase.word_alignment import alignment
    from SMT_PB.smt.phrase.word_alignment import symmetrization
    from SMT_PB.smt.ibmmodel import ibmmodel2
    import sys
    import csv
    import pickle

    delimiter = " "
    # load file which will be trained
    #modelfd = open(sys.argv[1])
    mk_sentences1=[]
    en_sentences1=[]
    en_sentences=[]
    mk_sentences=[]
    counter=0
    with open('MK-EN.lower.mk', 'rt', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            counter+=1
            if counter>=0and counter<1000:
                mk_sentences1.append(row)
            mk_sentences.append(row)
    counter=0
    with open('MK-EN.lower.en', 'rt', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            counter+=1
            if counter>=0 and counter<1000:
                en_sentences1.append(row)
            en_sentences.append(row)
    # sentenses = [line.rstrip().split(delimiter) for line
    #              in modelfd.readlines()]
    # make corpus
    niza_tuples=[]
    for index in range(0, len(en_sentences1)):
        mk_temp=' '.join(mk_sentences1[index])
        en_temp=' '.join(en_sentences1[index])
        niza_tuples.append((mk_temp, en_temp))
    corpus = mkcorpus(niza_tuples)

    niza_recenici=[]
    for index in range(0, len(en_sentences)):
        mk_temp=' '.join(mk_sentences[index])
        en_temp=' '.join(en_sentences[index])
        niza_recenici.append((mk_temp, en_temp))

    # train model from corpus
    # f2e_train = ibmmodel2._train(corpus, loop_count=10)
    # e2f_corpus = list(zip(*reversed(list(zip(*corpus)))))
    # e2f_train = ibmmodel2._train(e2f_corpus, loop_count=10)

    # phrase extraction
    niza_test=[]
    phrases_pairs = []
    for index in range(0, len(en_sentences1)):
        mk_temp=' '.join(mk_sentences1[index])
        en_temp=' '.join(en_sentences1[index])
        niza_vlez=""+mk_temp+";"+en_temp
        niza_test.append(niza_vlez)
    #niza_test=["бугарската полиција ги заострува односите во однос на проституциајта и сексуалното искористување.;bulgarian police crack down on prostitution, sexual exploitation."]
    for line in niza_test:
        parts = line.rstrip().split(';')
        es = parts[0].split()
        fs = parts[1].split()

        # f2e = ibmmodel2.viterbi_alignment(es, fs, *f2e_train).items()
        # e2f = ibmmodel2.viterbi_alignment(fs, es, *e2f_train).items()
        alignment = symmetrization(es, fs, corpus)
        #align = alignment(es, fs, e2f, f2e)  # symmetrized alignment
        ext = phrase_extract(es, fs, alignment)
        with open('phrases_full.txt', 'a', encoding='utf8') as file:
            for e, f in ext:
                e_new=str(' '.join(e))
                f_new=str(' '.join(f))
                counter_ef=0
                counter_e=0
                for en in niza_recenici:
                    e_rec=en[0]
                    f_rec=en[1]
                    if e_rec.find(e_new)!=-1:
                        counter_e+=1
                    if e_rec.find(e_new)!=-1 and f_rec.find(f_new)!=-1:
                        counter_ef+=1
                freq_phrase=counter_ef/counter_e
                phrases_pairs.append((e_new, f_new, freq_phrase))
                print("{} {} {} {} {}".format(e_new, "->", f_new, "->", freq_phrase))
                file.write("{} {} {} {} {}\n".format(e_new, "->", f_new, "->", freq_phrase))
    with open('phrases.pkl', 'wb') as file:
            pickle.dump(phrases_pairs, file)