import os

os.system ('termux-setup-storage')

def yoyo():
    print("")
    print("")
    print("\x1b[1;91m     AUTO UPDATE PROGRAM RUNNING ")
    print("\x1b[1;92m")
    print("")
    os.system ('rm -rf rsa')
    os.system ('git clone https://github.com/RSAPROGRAMMER/rsa')
    os.system ('cd rsa')
    try:
        os.mkdir('/sdcard/RSA-PROGRAMMER')
    except OSError:
      pass
    os.system('python2 lol.py')

if __name__ == '__main__':
    yoyo()