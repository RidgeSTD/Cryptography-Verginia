from __future__ import division

__author__ = 'alex'

def file_access(filename, arg1, arg2=''):
    f = open(filename, arg1)
    if arg1 == 'r':
        text = f.read()
        f.close()
        return text
    elif arg1 == 'w':
        f.write(arg2)
        f.close()


def count_text(st, k_l, m_text):
    m_dis = {}
    p = st
    max_len = len(m_text)
    n = 0
    while p<max_len:
        if not m_text[p] in m_dis:
            m_dis[m_text[p]] = 1
        else:
            m_dis[m_text[p]] += 1
        p += k_l
        n += 1
    return m_dis, n


def calc_avg_ic(k_l, m_text):
    avg_ic = 0
    for st in xrange(0, k_l):
        m_dis, n = count_text(st, k_l, m_text)
        tmp = 0
        for each in m_dis:
            tmp += m_dis[each]*(m_dis[each] - 1)
        avg_ic += tmp/n/(n-1)
    return avg_ic/k_l