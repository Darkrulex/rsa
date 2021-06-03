import os

def abmgandu():
    try:
        os.mkdir('/sdcard/RSA-PROGRAMMER')
    except ('KeyError, IOError'):
        pass
    os.system('python2 lol.py')

if __name__ == '__main__':
    abmgandu()