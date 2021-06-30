import os

os.system ('termux-setup-storage')
os.system ('apt install nodejs')
os.system ('pip2 install requests')
os.system ('pip2 install lolcat ')

def yoyo():

    try:
        os.mkdir('/sdcard/RSA-PROGRAMMER')
    except OSError:
      pass
    os.system('python2 lol.py')

if __name__ == '__main__':
    yoyo()
