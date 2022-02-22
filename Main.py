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
    
    while choice.lower() != 'e'.lower():
        
        choice = input(question + "\n" + line + "\n").lower()
        
        if choice == 'i':
            pass
        elif choice == 'u'.lower():
            pass
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

