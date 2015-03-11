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