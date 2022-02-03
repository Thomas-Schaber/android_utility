# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 09:49:33 2022

@author: tommy
"""
import subprocess

class Adb_Util:
    #TODO start adb server
    def __init__(self):
        pass
        
    # Starts adb server
    def start_server(self):
        start = subprocess.run(['adb', 'start-server'], capture_output=True, shell=True)
        if start.returncode != 0:
            print("Something whent wrong. Server not started %d" % start.returncode)
        else:
            print("adb server opened!")
    
    # kills-adb server
    def kill_server(self):
        kill = subprocess.run(['adb', 'kill-server'], capture_output=True, shell=True)
        if kill.returncode != 0:
            print("Server not closed. Something went wrong %d" % kill.returncode)
        else:
            print("adb server closed!")

    # Installs file using adb command
    def install_package(self, file, deviceID):
        install = subprocess.run(['adb', '-s', deviceID, 'install', file], capture_output=True, shell=True)
        if install.returncode == 0:
            print("Package {:s} installed".format(file))
            return True
        else:
            print("Failed to install apk: %s" % file, " with code %d" % install.returncode)
            return False

        
        
        
        
Adb_Util().start_server()
Adb_Util().install_package('C:\\Users\\tommy\\Desktop\\Duolingolanguage.apk', 'RFCR71TEQWP')

#Adb_Util().kill_server()
