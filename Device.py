# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 09:30:32 2022

@author: tommy
"""
import numpy as np


class Device:
    def __init__(self, name, deviceID, screenDensity, sdk, os):
        self.name = name
        self.deviceID = deviceID
        self.screenDensity = screenDensity
        self.sdk = sdk
        self.os = os
        self.packageList = np.array(5, dtype='S') 
        

    def init_package_list():
        return 0

    def install():
        return 0
    
    
    def uninstall():
        return 0

d1 = Device('Fold', '123123123', 'hdmix', 30, 'Go')
