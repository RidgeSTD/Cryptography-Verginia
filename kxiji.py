__author__ = 'ZSY'
import random


def calculateIC(n, len):
    ele_sum = 0
    for ele in n:
        ele_sum = ele_sum + ele * (ele - 1)
    IC = ele_sum / 1.0 / len / (len - 1)
    return IC


def analyse_deciphering(ciphertext, dic, dic_zsy):
    str = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for ele in ciphertext:
        if ele.lower() in dic:
            for dicitem in dic.iteritems():
                if ele.lower() == dicitem[0]:
                    str[dicitem[1]] += 1
    str_sorted = sorted(str, lambda x, y: -cmp(x, y))
    n = 0
    for str_ele in str:
        if str_ele == str_sorted[0]:
            cho = dic_zsy[n]
            dic_cho = dic[cho]
            if dic_cho < 4:
                k = 22 + dic_cho
                return dic_zsy[k]
            else:
                k = dic_cho - 4
                return dic_zsy[k]
        n += 1


# spilt the text
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


def deciphering_newIC(key, dic, sercert, ser_sum):
    nl = 0
    str = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for single in sercert:
        for serfre in dic.iteritems():
            if single.lower() == serfre[0]:
                ser_sum[serfre[1]] += 1
        sin_num = dic[single]
        nx = nl % len(key)
        rel_num = 26 + sin_num - dic[key[nx]]
        if rel_num >= 26:
            rel_num = sin_num - dic[key[nx]]
        else:
            pass
        nl += 1
        for keyvalue2 in dic.iteritems():
            if keyvalue2[1] == rel_num:
                str[keyvalue2[1]] += 1
    IC = calculateIC(str, len(sercert))
    return IC


# arrange list
def arrange_list(post):
    new_post = []
    n = 0
    while n < len(post):
        if n < len(post) - 1:
            new_post.append((post[n + 1] - post[n]))
        n += 1
    return new_post


# get common divisor
def getcommondivisor(str):
    sortstr = sorted(str, lambda x, y: -cmp(x, y))
    a = sortstr[0]
    i = 2
    count = 0
    nk = 2
    fin = []
    re = []
    dic = []
    while i <= a:
        for x in str:
            if x % i == 0:
                count += 1
            if x not in dic:
                dic.append(x)
        re.append(count)
        count = 0
        i += 1
    for w in re:
        if w >= 5:
            fin.append(nk)
        nk += 1
    print fin
    return fin


def main():
    # read text
    f = open('m.txt')
    try:
        alltext = f.read()
    finally:
        f.close()
    #print alltext

    key_num = raw_input("Please input the key:")

    dic = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10,
           'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20,
           'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

    dic_zsy = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k',
               11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u',
               21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

    fre_sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fre = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    ser_sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ser_fre = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # create random key
    key = []
    ini = 0
    while ini < int(key_num):
        a = random.randrange(0, 26)
        for x in dic.iteritems():
            if x[1] == a:
                key.append(x[0])
        ini += 1
    print key

    # encrypt function
    n = 0
    sercert = []
    alltext_len = 0
    for letter in alltext:
        if letter.lower() not in dic:
            pass
        else:
            alltext_len += 1
            for keyfre in dic.iteritems():
                if letter.lower() == keyfre[0]:
                    fre_sum[keyfre[1]] += 1

            le_num = dic[letter.lower()]
            pos = n % len(key)
            n += 1
            key_num = dic[key[pos].lower()]
            new_num = (key_num + le_num) % 26
            for keyvalue in dic.iteritems():
                if keyvalue[1] == new_num:
                    new_le = keyvalue[0]
                    sercert.append(new_le)
    #calculate proclaimed in writing letter frequency
    fre_count = 0
    for fre_s in fre_sum:
        fre[fre_count] = fre_s / 1.0 / alltext_len
        print str(fre[fre_count]) + ' '
        fre_count += 1

    #calculate proclaimed in writing IC
    print 'proclaimed in writing IC:' + str(calculateIC(fre_sum, alltext_len))
    print r'deciphering Program is running now...'

    # deciphering function
    nl = 0
    oldsercert = []
    for single in sercert:
        for serfre in dic.iteritems():
            if single.lower() == serfre[0]:
                ser_sum[serfre[1]] += 1

        sin_num = dic[single]
        nx = nl % len(key)
        rel_num = 26 + sin_num - dic[key[nx]]
        if rel_num >= 26:
            rel_num = sin_num - dic[key[nx]]
        else:
            pass
        nl += 1
        for keyvalue2 in dic.iteritems():
            if keyvalue2[1] == rel_num:
                oldsercert.append(keyvalue2[0])
    ser_count = 0
    ser_k = 0
    print 'ciphertext letter frequency :'
    for ser_s in ser_sum:
        ser_fre[ser_count] = ser_s / 1.0 / alltext_len
        print str(ser_fre[ser_count]) + ' '
        ser_count += 1
    # calculate ciphertext IC
    print 'ciphertext IC:' + str(calculateIC(ser_sum, alltext_len))
    print oldsercert[:100]

    model = []
    nw = 0
    nr = 1
    #posi = 0
    post = []
    find = False
    while nw < alltext_len:
        model.append(sercert[nw])
        model.append(sercert[nw + 1])
        print model[0] + model[1]
        while nr < alltext_len:
            if sercert[nr] == model[0]:
                if sercert[nr + 1] == model[1]:
                    post.append(nr)

            nr += 1
        newpost = arrange_list(post)
        common = getcommondivisor(newpost)
        nw += 1
        model = []
        for xt in common:
            fin_sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            countr = 0
            strk = spilt_sen(sercert, xt)
            strr = []
            while countr < len(strk):
                k = analyse_deciphering(strk[countr], dic, dic_zsy)
                strr.append(k)
                countr += 1
            x = deciphering_newIC(strr, dic, sercert, fin_sum)
            print 'key value is:' + str(xt) + 'IC:' + str(x)
            if -0.005 < x - 0.065 < 0.003:
                print strr
                find = True
                break
            xt += 1
        if find:
            break


if __name__ == '__main__':
    main()





