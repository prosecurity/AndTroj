#!/usr/bin/env python
# https://t.me/unk9vvn
# AVI
from core.update import updater
from core.start import version
from core.menu import main_menu


def main():
    version()
    updater()
    main_menu()

main()
