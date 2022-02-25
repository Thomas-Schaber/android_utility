# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 10:00:26 2022

@author: tommy


This is the driver program for the android utility
"""
from Device import Device
from Adb_Util import Adb_Util
from Google_Play_Info import Google_Play_Info
from App import App
import os


def main():
    apk_directory = "C:\\Users\\tommy\\CSC221\\Android_Project1\\apk"
    
    question = "What would you like to do?\nInstall, Uninstall," \
                   " Process apk info, Get device info, Device list, Exit:"
    line = ""
    for x in range(len(question)):
        line += '-'
        
    choice = ""
    device_list_serials = []
    device_list = []
    app_list = []
    print("Initializing app list...")
    os.chdir(apk_directory)

    for file in os.listdir():
        try:
            app_list.append(App(apk_directory, file))
        except Exception as e:
            print(e)
            pass
    print(len(app_list), "apps found\n")
    print("initializing device list...")
    device_list_serials = Adb_Util().get_device_list()
    
    for serial_number in device_list_serials:
        #print(device_list_serials[serial_number])
        device_list.append(Device(serial_number))
    for device in device_list:
        print(device)
    
    while choice.lower() != 'e'.lower():
        
        choice = input(question + "\n" + line + "\n").lower()
        
        if choice == 'i':
            
            if len(device_list) > 0:
                for device in device_list:
                    for app in app_list:
                        if app.file_type == ".apk":
                            device.install(app.file_name)
                        else:
                            device.install_bundle(app.file_name)                
            
        elif choice == 'u'.lower():
            
            for device in device_list:
                device.init_package_list()
                device.uninstall_all()


        elif choice == 'p'.lower():
            pass
        elif choice == 'g'.lower():
            pass
        elif choice == 'd'.lower:
            pass
        elif choice == 'e':
            print("Exiting...")
        
        else:
            print("Invalid choice:", choice)
    
    
    
    




if __name__ == '__main__':
    main()

