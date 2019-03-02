#!/usr/bin/env python
# coding=utf-8
# https://t.me/unk9vvn
# AVI
import os, sys, time, random
from twilio.rest import Client
from core.start import cls
from lib.Web.Harvester import harstr
from lib.Web.APK_Attack import apk_atck
from lib.SMS.Harvester import s_harstr
from lib.SMS.APK_Attack import sms_apk
from lib.Mail.Mail_Phish import mail_apk



def social_eng_menu():
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
                    "[0] EXIT\n\t"
                    "\n\nroot@unk9vvn:~# ")
    if eng == "1":
        checkauth = os.path.exists('/root/.ngrok2/ngrok.yml')
        if checkauth == (True):
            clone_method = raw_input("\n\t[1] APK Attack"
                                     "\n\t[2] Harvester"
                                     "\n\nroot@unk9vvn:~# ")
            if clone_method == "1":
                apk_atck()
            elif clone_method == "2":
                harstr()
            else:
                social_eng_menu()
        else:
            print "\n\t[X] Please selected 4 menu for install Ngrok..."
            social_eng_menu()

    elif eng == "2":
        check_ngrok = os.path.exists('/root/.AndTroj/twilio_token.txt')
        if check_ngrok == (True):
            clone_method = raw_input("\n\t[1] APK Attack"
                                     "\n\t[2] Harvester"
                                     "\n\nroot@unk9vvn:~# ")
            if clone_method == "1":
                sms_apk()
            elif clone_method == "2":
                s_harstr()
        else:
            print "\n\t[X] Please install Ngrok BeEF and Twilio..."
            social_eng_menu()

    elif eng == "3":
        check_ngrok = os.path.exists('/root/.ngrok2/ngrok.yml')
        if check_ngrok == (True):
            mail_apk()
        else:
            print "\n\t[X] Please install Ngrok BeEF and Twilio..."
            social_eng_menu()

    elif eng == "4":
        check_ngrok = os.path.exists('/root/.ngrok2/ngrok.yml')
        if check_ngrok == (True):
            print "\n\t[X] FileFormat Injection Disabled..."
            social_eng_menu()
        else:
            print "\n\t[X] Please install Ngrok BeEF and Twilio..."
            social_eng_menu()

    elif eng == "0":
        sys.exit()
    else:
        social_eng_menu()
