#! /usr/bin/env python
# coding:utf-8

from operator import itemgetter
import collections
from smt.utils import utility
import decimal
from decimal import Decimal as D

decimal.getcontext().prec = 4
decimal.getcontext().rounding = decimal.ROUND_HALF_UP


def _constant_factory(value):
    return lambda: value


def _train(corpus, loop_count=1000):
    f_keys = set()
    for (es, fs) in corpus:
        for f in fs:
            f_keys.add(f)
    t = collections.defaultdict(_constant_factory(D(1/len(f_keys))))

    for i in range(loop_count):
        count = collections.defaultdict(D)
        total = collections.defaultdict(D)
        s_total = collections.defaultdict(D)
        for (es, fs) in corpus:
            # compute normalization
            for e in es:
                s_total[e] = D()
                for f in fs:
                    s_total[e] += t[(e, f)]
            for e in es:
                for f in fs:
                    count[(e, f)] += t[(e, f)] / s_total[e]
                    total[f] += t[(e, f)] / s_total[e]

        for (e, f) in count.keys():
            t[(e, f)] = count[(e, f)] / total[f]

    return t


def train(sentences, loop_count=1000):
    corpus = utility.mkcorpus(sentences)
    return _train(corpus, loop_count)


def _pprint(tbl):
    for (e, f), v in sorted(tbl.items(), key=itemgetter(1), reverse=True):
        print(u"p({e}|{f}) = {v}".format(e=e, f=f, v=v))
