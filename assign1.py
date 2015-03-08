import random

k_int = []
k_chr = ''
n = 0


def file_access(filename, arg1, arg2=''):
    f = open(filename, arg1)
    if arg1 == 'r':
        text = f.read()
        f.close()
        return text
    elif arg1 == 'w':
        f.write(arg2)


def key_generate(n):
    global k_int
    global k_chr
    print('Generating key...')
    for x in xrange(0, n):
        tmp = random.randint(0, 25)
        k_int.append(tmp+1)
        k_chr += chr(tmp + ord('a'))
    file_access('key.txt', 'w', k_chr)
    print('Key has been stored in file key.txt')
    # print k_int


def readfile_and_trim(filename):
    buf = file_access(filename, 'r')
    text = ''
    for each in buf:
        if ('a' <= each <= 'z') or ('A' <= each <= 'Z'):
            text += each
    file_access(filename, 'w', text)
    return text


def calculation(ori, tar, arg):
    if 'a' <= ori <= 'z':
        tmp = ord(ori) + tar * arg
        if tmp > ord('z'):
            tmp -= 26
        if tmp < ord('a'):
            tmp += 26
    else:
        tmp = ord(ori) + tar * arg
        if tmp > ord('Z'):
            tmp -= 26
        if tmp < ord('A'):
            tmp += 26
    return chr(tmp)


def encryption(m):
    global n
    global k_int
    print('Encrypting...')
    c = ''
    for x in xrange(0, len(m)):
        c += calculation(m[x], k_int[x % n], 1)
    file_access('c.txt', 'w', c)
    print('Finish encrypting! Please check file c.txt')
    return c


def decryption(c):
    global n
    global k_int
    print('Decrypting')
    m = ''
    for x in xrange(0, len(c)):
        m += calculation(c[x], k_int[x % n], -1)
    file_access('decrypted_file.txt', 'w', m)
    print('Finish decrypting! Please check file m_new.txt')




def main():
    global n
    filename = raw_input('Please input the filename\n')
    m = readfile_and_trim(filename)
    n = input('Please input the length N to generate key\n')
    key_generate(n)
    c = encryption(m)
    decryption(c)



if __name__ == '__main__':
    main()

