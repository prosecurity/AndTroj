#!/usr/bin/env python
# coding=utf-8
# https://t.me/unk9vvn
# AVI
import os, sys, urllib2, time, random, shutil, socket, string, subprocess, socks, smtplib
from urllib import urlopen
from urllib2 import urlopen
from twilio.rest import Client
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from core.start import cls
from lib.Web.Harvester import harstr
from lib.Web.APK_Attack import apk_atck
from lib.SMS.Harvester import s_harstr
from lib.SMS.APK_Attack import s_apk_atck
from lib.Mail.Mail_Phish import mailph


def eng_menu():
    global URL, NoIP, METHOD, URL_CLONE, LGPORT_BEEF, TWIL_SID, TWIL_TOKEN, SPOOF_NUM, TARGET_NUM, PHONELIST, MailPhish, TARGET_MAIL, TARGET_LIST, SUBJECT_MAIL
    cls()
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
                   ___          _      _ 
                  / __| ___  __(_)__ _| |
                  \__ \/ _ \/ _| / _` | |
                  |___/\___/\__|_\__,_|_|

                   ___           _                  _           
                  | __|_ _  __ _(_)_ _  ___ ___ _ _(_)_ _  __ _ 
                  | _|| ' \/ _` | | ' \/ -_) -_) '_| | ' \/ _` |
                  |___|_||_\__, |_|_||_\___\___|_| |_|_||_\__, |
                           |___/                          |___/ 
                                  Unk9vvN
                            https://t.me/Unk9vvN
                                  AndTroj

[i] You need Port Forwarded to ports > 3000-5432-55552-4141-5151-8000
[i] Register & Buy Business License > https://dashboard.ngrok.com/user/signup
[i] Register & Buy a Spoof Number > https://www.twilio.com/try-twilio
[i] Register & Buy a Mail Spoof > https://www.smtp2go.com/pricing
    """
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.01)

    eng = raw_input("\t[1] Web SpearPhishing\n\t"
                    "[2] SMS SpearPhishing\n\t"
                    "[3] Mail SpearPhishing\n\t"
                    "[4] FileFormat Injection(Disabled)\n\t"
                    "[5] Add Ngrok Ports\n\t"
                    "[0] EXIT\n\t"
                    "\n\nroot@unk9vvn:~# ")

    if eng == "1":
        checkauth = os.path.exists('/root/.ngrok2/ngrok.yml')
        if checkauth == (True):
            CLONE_MTD = raw_input("\n\t[1] APK Attack"
                                  "\n\t[2] Harvester"
                                  "\n\nroot@unk9vvn:~# ")
            if CLONE_MTD == "1":
                apk_atck()
            elif CLONE_MTD == "2":
                harstr()
            else:
                eng_menu()
        else:
            print "\n\t[X] Please install Ngrok BeEF and Twilio..."
            eng_menu()

    elif eng == "2":
        chekngk = os.path.exists('/root/.AndTroj/twilio_token.txt')
        if chekngk == (True):
            CLONE_MTD = raw_input("\n\t[1] APK Attack"
                                  "\n\t[2] Harvester"
                                  "\n\nroot@unk9vvn:~# ")
            if CLONE_MTD == "1":
                s_apk_atck()
            elif CLONE_MTD == "2":
                s_harstr()
        else:
            print "\n\t[X] Please install Ngrok BeEF and Twilio..."
            eng_menu()

    elif eng == "3":
        chekngk = os.path.exists('/root/.ngrok2/ngrok.yml')
        if chekngk == (True):
            mailph()
        else:
            print "\n\t[X] Please install Ngrok BeEF and Twilio..."
            eng_menu()

    elif eng == "4":
        chekngk = os.path.exists('/root/.ngrok2/ngrok.yml')
        if chekngk == (True):
            print "\n"
        else:
            print "\n\t[X] Please install Ngrok BeEF and Twilio..."
            eng_menu()

    elif eng == "5":
        chekngk = os.path.exists('/root/.ngrok2/ngrok.yml')
        if chekngk == (True):
            total = int(input("\n\tA few Ports: "))
            for i in range(total):
                print "\n"
                m = raw_input("\tProtocol(tcp/http): ")
                n = raw_input("\tNumber NPORT: ")
                print "\n"
                subprocess.call(
                    'gnome-terminal --tab -e \'proxychains ngrok ' + m + ' ' + n + '\'',
                    shell=True)
        else:
            print "\n\t[X] Please install Ngrok BeEF and Twilio..."
            eng_menu()

    elif eng == "0":
        sys.exit()
    else:
        eng_menu()
