# Dahlia Development Installer 
import os

ans = input ('''
Dahlia Development Installer
###################################

This will install the environment to build
dahlia assets. This will take a while so get
a cuppa tea.

YOU MUST HAVE AT LEAST 6GB OF FREE STORAGE!

Install? (y/n):''')

if ans = 'y':
    os.system("sudo apt update")
    os.system("sudo apt install wget git xterm tar")
    os.system("wget https://dl.google.com/dl/android/studio/ide-zips/3.4.1.0/android-studio-ide-183.5522156-linux.tar.gz")
    os.system("tar xvzf android-studio-ide-183.5522156-linux.tar.gz")
    print('when android studio is finished installing exit xterm to continue installing the rest of the packages')
    os.system("xterm -e sh $HOME/android-studio/bin/studio.sh")
    os.system("wget https://storage.googleapis.com/flutter_infra/releases/stable/linux/flutter_linux_v1.2.1-stable.tar.xz")
    os.system("tar xf $HOME/flutter_linux_v1.2.1-stable.tar.xz")
    os.system("wget https://az764295.vo.msecnd.net/stable/51b0b28134d51361cf996d2f0a1c698247aeabd8/code_1.33.1-1554971066_amd64.deb")
    os.system("sudo apt install $HOME/code_1.33.1-1554971066_amd64.deb")
    print('cleaning out old files that are not needed anymore')
    os.system("sudo rm code_1.33.1-1554971066_amd64.deb")
    os.system("sudo rm flutter_linux_v1.2.1-stable.tar.xz")
    os.system("sudo rm android-studio-ide-183.5522156-linux.tar.gz")
    print('finished setting up environment...')
    
