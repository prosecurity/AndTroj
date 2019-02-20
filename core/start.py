#!/usr/bin/env python
# coding=utf-8
# https://t.me/unk9vvn
# AVI
from core.social_menu import *


dir = '/usr/share/AndTroj'
tmp = dir + '/tmp/'

try:
    from colorama import Fore, Back, Style
    r = Fore.RED
    g = Fore.GREEN
    w = Fore.WHITE
    b = Fore.BLUE
    y = Fore.YELLOW
    m = Fore.MAGENTA
    res = Style.RESET_ALL
    os.system('service postgresql start && service tor start')
except ImportError:
    os.system('pip install colorama twilio flask env paramiko freeze SocksiPy-branch email smtp2go')
    pass


cwd = os.getcwd()


def start():
    atlv = 'apktool -version'
    atl = os.popen(atlv)
    chk_atl = atl.read()
    if chk_atl > '2.3.4':
        pass
    else:
        os.system(
            'apt-get install -y tor apktool aapt sendemail proxychains python-socks kali-linux-full;service tor start;'
            'proxychains wget https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.3.4.jar -O /usr/local/bin/apktool.jar;'
            'wget https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool -O /usr/local/bin/apktool;'
            'chmod +x /usr/local/bin/apktool.jar && chmod +x /usr/local/bin/apktool')
    chk_cmd = os.path.exists('/usr/share/AndTroj/')
    
    if chk_cmd == (False):
        executor = '#!/bin/bash\npython /usr/share/AndTroj/atj.py "$@"'
        commandline = open('/usr/bin/atj', 'w')
        commandline.write(executor)
        commandline.close()
        os.system(
            'mkdir /usr/share/AndTroj && cd ' + cwd + '&& cp -r * /usr/share/AndTroj && chmod +x '
                                                      '/usr/share/AndTroj/atj.py /usr/share/AndTroj/requirements.txt '
                                                      '&& chmod +x /usr/bin/atj')
    else:
        pass

    chk_htm = os.path.exists('/var/www/html/index.html')
    if chk_htm == (False):
        pass
    else:
        os.system('cd /var/www/html/ && rm -r *')
        pass


    chk_tmp = os.path.exists('/usr/share/AndTroj/tmp')
    if chk_tmp == (False):
        os.system('mkdir {0}/tmp'.format(dir))
        os.system('chmod +x {0}/tmp'.format(dir))
    else:
        os.system('rm -r {0}/tmp'.format(dir))
        os.system('mkdir {0}/tmp'.format(dir))
        os.system('chmod +x {0}/tmp'.format(dir))
        pass


def Tor():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, "127.0.0.1", 9050, True)
    socket.socket = socks.socksocket


def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])

