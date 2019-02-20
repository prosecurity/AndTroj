#!/usr/bin/env python
# https://t.me/unk9vvn
# AVI
from core.update import updater
from core.start import start
from core.menu import menu

def main():
    start()
    updater()
    menu().main_menu()

main()
