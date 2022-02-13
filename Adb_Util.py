# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 09:49:33 2022

@author: tommy
"""
import subprocess
import numpy as np

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
        
    # Pulls devices installed packages returns a numpy array or False
    # adb shell cmd package list packages
    # adb -s R38M40EX5ZA shell cmd package list packages
    def package_list(self, device_id):
        packages = np.array([])
        packages_command = subprocess.run(['adb', '-s', device_id, 'shell', 'cmd', 'package', 'list', 'packages', '-3' ], capture_output=True, shell=True)

        if packages_command.returncode == 0:
            for line in packages_command.stdout.decode('utf-8').splitlines():
                line = line.split('package:')
                packages = np.append(packages, line[1])
            print(packages)
            print(len(packages))
            return packages
        else:
            print(packages_command.stderr)
            return False
            

        
        
        

Adb_Util().start_server()
test_list = Adb_Util().package_list('A00000K580152200711')
Adb_Util().package_list('R38M40EX5ZA')

deviceID = 'A00000K580152200711'

for package in test_list:
    print(f'unistalling package: {package}')
    uninstall = subprocess.run(['adb', '-s', deviceID, 'uninstall', package], capture_output=True, shell=True)
    
    

#Adb_Util().package_list('A00000K580152200711')
#Adb_Util().install_package('C:\\Users\\tommy\\Desktop\\Duolingolanguage.apk', 'R38M40EX5ZA')

#Adb_Util().kill_server()
