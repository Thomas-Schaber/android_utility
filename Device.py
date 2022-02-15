# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 09:30:32 2022

@author: tommy
"""
import numpy as np
from Adb_Util import Adb_Util

class Device:
    def __init__(self, name, deviceID, screenDensity, sdk, os):
        self.name = name
        self.deviceID = deviceID
        self.screenDensity = screenDensity
        self.sdk = sdk
        self.os = os
        self.packageList = np.array([], dtype='S') 
        

    def init_package_list(self):
        self.packageList = Adb_Util().package_list(self.deviceID)

    def install(self, file):
        Adb_Util().install_package(file, self.deviceID)
    
    
    def uninstall_all(self):
        if len(self.packageList) > 0:
            for package_name in self.packageList:
                Adb_Util().unistall_package(self.deviceID, package_name)
        else:
            print("The amount of apps installed on device is currently 0")
            
    def uninstall(self, package_name):
        if len(self.packageList) > 0:
            Adb_Util().unistall_package(self.deviceID, package_name)
        else:
            print("The amount of apps installed on device is currently 0")
    
    def get_packageList(self):
        return self.packageList

d1 = Device('Nokia', 'A00000K580152200711', 'hdmix', 30, 'Go')
d1.init_package_list()
print(d1.packageList)
d1.uninstall_all()