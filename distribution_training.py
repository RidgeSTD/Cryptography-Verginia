from __future__ import division

def train():
    dis = {}
    tot = 0
    for x in xrange(ord('A'), ord('Z')+1):
        dis[chr(x)] = 0
    file_name = raw_input('please input file name\n')
    print('calculating...')
    fi = open(file_name, 'r')
    text = fi.read()
    fi.close()
    for c in text:
        dis[c] += 1
        tot += 1
    fo = open('distribution.txt', 'w')
    for x in xrange(ord('A'), ord('Z')+1):
        fo.write(chr(x)+": "+str(dis[chr(x)]/tot)+"\n")
    fo.close()
    print("finish distribution training")
    return dis, tot



if __name__ == '__main__':
    train()

