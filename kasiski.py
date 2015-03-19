# coding=utf-8
from __future__ import division
import assign1_global
import assign1

__author__ = 'alex'


DIS = {}
TOT_LENGTH = 0
TEXT = ''
HASH_C2I = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
           'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20,
           'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
THRESHOLD = 0.007
STANDARD_IC_EN = 0.067



def scan_cyphertext(f_name = ""):
    global DIS, TOT_LENGTH, TEXT
    if f_name == "":
        file_name = raw_input('Please input cyphertext file name:\n')
    else:
        file_name = f_name
    TEXT = assign1_global.file_access(file_name, 'r')
    TOT_LENGTH = len(TEXT)
    return TEXT

# arrange list
def arrange_list(__post):
    __newpost = []
    for i in xrange(1, len(__post)):
        __newpost.append((__post[i] - __post[i - 1]))
    return __newpost


# get common divisor
def getcommondivisor(__newpost):
    sortstr = sorted(__newpost, lambda x, y: -cmp(x, y))
    print('Gap between is :')
    print(sortstr)
    print("Getting commond divisor...")
    a = sortstr[0]
    i = 2
    count = 0
    nk = 2
    fin = []
    re = {}
    dic = []
    while i <= a:
        for x in __newpost:
            if x % i == 0:
                count += 1
            if x not in dic:
                dic.append(x)
        re[i] = count
        count = 0
        i += 1
    for w in re:
        if re[w] >= 5:
            fin.append(w)
        nk += 1
    return fin


def spilt_sen(text, num):
    str_res = []
    n = 0
    gln = 0
    while gln < num:
        str2 = []
        while n < len(text):
            if n % num == gln:
                str2.append(text[n])
            n += 1
        str_res.append(str2)
        gln += 1
        n = gln
    return str_res


def kasiski(__text):
    __model = []
    __nw = 0
    __nr = 1
    #posi = 0
    __post = [1]
    __find = False
    __model.append(__text[__nw])
    __model.append(__text[__nw + 1])
    print __model[0] + __model[1]
    while __nr < TOT_LENGTH:
        if __text[__nr] == __model[0]:
            if __text[__nr + 1] == __model[1]:
                __post.append(__nr)

        __nr += 1
    __newpost = arrange_list(__post)
    common = getcommondivisor(__newpost)

    return common


def attack(arg=""):
    global DIS, TOT_LENGTH, TEXT
    for x in xrange(ord('A'), ord('Z')+1):
        DIS[chr(x)] = 0
    scan_cyphertext(arg)
    esti_len_list = kasiski(TEXT)
    print('Suspected Key Length As Follow:\n')
    print(esti_len_list)

    esti_len = 0
    for each_key_len in esti_len_list:
        tmp = assign1_global.calc_avg_ic(each_key_len, TEXT)
        print(str(each_key_len)+" bit(s) Key has IC of: "+str(tmp))
        if abs(tmp - STANDARD_IC_EN) < THRESHOLD:
            esti_len = each_key_len
            break
    if esti_len == 0:
        print("Fail to attack on the cyphertext. Program Exit...")
        exit(0)
    print('The estimated length of KEY after comparation is: '+str(esti_len))

    # calculate K
    m_dis = {}
    k_int = []
    for st in xrange(0, esti_len):
        m_dis, n = assign1_global.count_text(st, esti_len, TEXT)
        tmp = -1
        for each in m_dis:
            if tmp<m_dis[each]:
                tmp = m_dis[each]
                bit_char = ord(each)
        bit_char = (bit_char - 43) % 26
        if bit_char == 0:
            bit_char = 26
        k_int.append(bit_char)
    return k_int


def main():
    filename = raw_input('Please input filename. Press ENTER directly for default file...')
    if filename == '':
        filename = 'bainiangudu.txt'
    key_length = raw_input('Please input key length. Press ENTER directyly for default length 20')
    if key_length=='':
        key_length = 20
    else:
        key_length = int(key_length)
    assign1.e(filename, key_length)
    k_int = attack("c.txt")
    k_chr = []
    print k_int
    for x in xrange(0, len(k_int)):
        k_chr.append(chr(k_int[x] + 64))
    print('The KEY is:')
    print k_chr

if __name__ == '__main__':
    main()