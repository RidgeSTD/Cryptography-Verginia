from __future__ import division
import assign1_global
import assign1

__author__ = 'alex'

dis = {}
tot = 0
text = ''
THRESHOLD = 0.07
STANDARD_IC_EN = 0.067

def scan_cyphertext(f_name = ""):
    global dis, tot, text
    if f_name == "":
        file_name = raw_input('Please input cyphertext file name:\n')
    else:
        file_name = f_name
    text = assign1_global.file_access(file_name, 'r')
    for c in text:
        dis[c] += 1
        tot += 1


def calc():
    global dis, tot
    k_o = 0
    for each in dis:
        k_o += dis[each]*(dis[each] - 1)
        if k_o < 0:
            print "ERROR_OUT_OF_BOUND"
    k_o /= tot
    k_o /= (tot - 1)
    return (STANDARD_IC_EN - 0.0385)/(k_o - 0.0385)


def attack(arg=""):
    global dis, tot, text, THRESHOLD
    for x in xrange(ord('A'), ord('Z')+1):
        dis[chr(x)] = 0
    scan_cyphertext(arg)
    esti_len = calc()
    print "friedman_key_length = "+str(esti_len)
    st = input('please input left search limit\n')
    en = input('please input right search limit\n')

    # located search space, search now...

    esti_len = 0
    for k in xrange(st, en+1):
        tmp = assign1_global.calc_avg_ic(k, text)
        print('k: '+str(k)+', p: '+str(tmp))
        if abs(tmp - STANDARD_IC_EN) < THRESHOLD and esti_len == 0:
            esti_len = k
    print('The estimated length of KEY after comparation is: '+str(esti_len))

    # calculate K
    m_dis = {}
    k_int = []
    for st in xrange(0, esti_len):
        m_dis, n = assign1_global.count_text(st, esti_len, text)
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