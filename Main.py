# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 10:00:26 2022

@author: tommy


This is the driver program for the android utility
"""

import sys
import os
import requests
import subprocess

try:
    import numpy as np
    from Device import Device
    from Adb_Util import Adb_Util
    from Google_Play_Info import Google_Play_Info
    from Apk_Processor import Apk_Processor
    from App import App

except ModuleNotFoundError:
    print("Installing required packages...")
    install_packages = subprocess.run("pip install -r requirements.txt")
    from Device import Device
    from Adb_Util import Adb_Util
    from Google_Play_Info import Google_Play_Info
    from Apk_Processor import Apk_Processor
    from App import App
    print("Done...")


def main():
    apk_directory = os.getcwd()
    bundletool_download_url = 'https://github.com/google/bundletool/releases/download/1.10.0/bundletool-all-1.10.0.jar'

    if os.path.exists(apk_directory + '\\apk'):
        apk_directory = apk_directory + '\\apk'
    else:
        print("Directory 'apk' not found creating folder and installing bundletool")
        os.mkdir('apk')
        apk_directory = apk_directory + '\\apk'
        response = requests.get(bundletool_download_url)
        open(apk_directory + "\\bundletool-all.jar", "wb").write(response.content)
        print("Done...")

    question = "What would you like to do?\nInstall, Uninstall," \
               " Process apk info, Get device info, Device list, Exit:"
    line = ""
    for x in range(len(question)):
        line += '-'

    choice = ""
    device_list_serials = []
    device_list = []
    app_list = []
    Adb_Util().start_server()
    print("Initializing app list...")
    os.chdir(apk_directory)

    for file in os.listdir():
        try:
            app_list.append(App(apk_directory, file))
        except Exception as e:
            print(e, " ", file)
            pass

    print(len(app_list), "apps found\n")
    print("initializing device list...")
    device_list = refresh_device_list()

    while choice.lower() != 'e'.lower():

        choice = input(question + "\n" + line + "\n").lower()
        print()

        if choice == 'i':
            device_list = refresh_device_list()

            if len(device_list) > 0:
                for device in device_list:
                    for app in app_list:
                        if app.file_type == ".apk":
                            device.install(app.file_name)
                        else:
                            device.install_bundle(app.file_name)

        elif choice == 'u'.lower():

            device_list = refresh_device_list()

            for device in device_list:
                try:
                    device.init_package_list()
                    device.uninstall_all()
                except Exception as e:
                    print(e)

        elif choice == 'p'.lower():
            Apk_Processor(app_list)
            print("Processed successfully...")

        elif choice == 'g'.lower():
            refresh_device_list()

        elif choice == 'd'.lower():
            refresh_device_list()

            for x in range(len(device_list_serials)):
                print(device_list_serials[x])

        elif choice == 'e':
            print("Exiting...")
            Adb_Util().kill_server()

        else:
            print("Invalid choice:", choice)


def refresh_device_list():
    device_list = []
    device_list_serials = Adb_Util().get_device_list()

    for serial_number in device_list_serials:
        device_list.append(Device(serial_number))

    for device in device_list:
        print(device)

    return device_list


if __name__ == '__main__':
    main()
