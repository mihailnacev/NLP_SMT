#! /usr/bin/env python
# coding:utf-8

import collections
from smt.ibmmodel import ibmmodel1
from smt.utils import utility
import decimal
from decimal import Decimal as D

decimal.getcontext().prec = 4
decimal.getcontext().rounding = decimal.ROUND_HALF_UP


class _keydefaultdict(collections.defaultdict):
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        else:
            ret = self[key] = self.default_factory(key)
            return ret


def _train(corpus, loop_count=1000):
    f_keys = set()
    for (es, fs) in corpus:
        for f in fs:
            f_keys.add(f)
    t = ibmmodel1._train(corpus, loop_count)

    def key_fun(key):
        i, j, l_e, l_f = key
        return D("1") / D(l_f + 1)
    a = _keydefaultdict(key_fun)

    for _i in range(loop_count):
        count = collections.defaultdict(D)
        total = collections.defaultdict(D)
        count_a = collections.defaultdict(D)
        total_a = collections.defaultdict(D)

        s_total = collections.defaultdict(D)
        for (es, fs) in corpus:
            l_e = len(es)
            l_f = len(fs)
            for (j, e) in enumerate(es, 1):
                s_total[e] = 0
                for (i, f) in enumerate(fs, 1):
                    s_total[e] += t[(e, f)] * a[(i, j, l_e, l_f)]
            for (j, e) in enumerate(es, 1):
                for (i, f) in enumerate(fs, 1):
                    c = t[(e, f)] * a[(i, j, l_e, l_f)] / s_total[e]
                    count[(e, f)] += c
                    total[f] += c
                    count_a[(i, j, l_e, l_f)] += c
                    total_a[(j, l_e, l_f)] += c

        for (e, f) in count.keys():
            try:
                t[(e, f)] = count[(e, f)] / total[f]
            except decimal.DivisionByZero:
                print(u"e: {e}, f: {f}, count[(e, f)]: {ef}, total[f]: \
                      {totalf}".format(e=e, f=f, ef=count[(e, f)],
                                       totalf=total[f]))
                raise
        for (i, j, l_e, l_f) in count_a.keys():
            a[(i, j, l_e, l_f)] = count_a[(i, j, l_e, l_f)] / \
                total_a[(j, l_e, l_f)]

    print('FINISH Model2')
    return (t, a)


def train(sentences, loop_count=1000):
    corpus = utility.mkcorpus(sentences)
    return _train(corpus, loop_count)


def viterbi_alignment(es, fs, t, a):

    max_a = collections.defaultdict(float)
    l_e = len(es)
    l_f = len(fs)
    for (j, e) in enumerate(es, 1):
        current_max = (0, -1)
        for (i, f) in enumerate(fs, 1):
            val = t[(e, f)] * a[(i, j, l_e, l_f)]
            if current_max[1] < val:
                current_max = (i, val)
        max_a[j] = current_max[0]
    return max_a

