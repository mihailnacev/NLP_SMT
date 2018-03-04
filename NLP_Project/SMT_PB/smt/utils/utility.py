#! /usr/bin/env python
# coding:utf-8

from __future__ import division, print_function


def mkcorpus(sentences):
    
    return [(es.split(), fs.split()) for (es, fs) in sentences]


def matrix(
        m, n, lst,
        m_text: list=None,
        n_text: list=None):

    fmt = ""
    if n_text:
        fmt += "     {}\n".format(" ".join(n_text))
    for i in range(1, m+1):
        if m_text:
            fmt += "{:<4.4} ".format(m_text[i-1])
        fmt += "|"
        for j in range(1, n+1):
            if (i, j) in lst:
                fmt += "x|"
            else:
                fmt += " |"
        fmt += "\n"
    return fmt
