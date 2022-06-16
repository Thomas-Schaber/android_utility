# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 09:30:32 2022

@author: tommy
"""
import numpy as np
from Adb_Util import Adb_Util

class Device:


    def __init__(self, deviceID,
                 os=None,
                 sdk=None,
                 cpu_arch=None,
                 screen_density=None,
                 name=None):
        
        self.deviceID = deviceID
        self.exclude = np.array(["com.expressvpn.vpn", "com.symantec.mobilesecurity"])
        if name == None:
            self.name = self.init_device_name()    
        else:
            self.name = name
            
        if screen_density == None:
            self.screen_density = self.init_screen_density()  
        else:
            self.screen_density = screen_density
            
        if cpu_arch == None:
            self.cpu_arch = self.init_cpu_arch() 
        else:
            self.cpu_arch = cpu_arch
            
        if sdk == None:
            self.sdk = self.init_sdk()
        else:
            self.sdk = sdk
            
        if os == None:
            self.os = self.init_os()
        else:
            self.os = os
            
        self.packageList = np.array([], dtype='S')
        self.init_package_list()
        

    def init_package_list(self):
        self.packageList = Adb_Util().package_list(self.deviceID)

        
    #ro.product.model
    #adb -s A00000K580152200711 shell getprop ro.product.model
    # Gets device name using adb
    def init_device_name(self):
        
        device_name_command = Adb_Util().device_info(
            self.deviceID, 'ro.product.model'
            )
        
        device_name = device_name_command.split('\r')
        return device_name[0]


    # pulls screen density using device id and command arg for adb
    def init_screen_density(self):
        
        screen_density_command =  Adb_Util().device_info(
            self.deviceID, 'ro.sf.lcd_density'
            )
        
        screen_density = screen_density_command.split('\r')
        
        return screen_density[0]
    
        
    #[ro.product.cpu.abi]: [armeabi-v7a] [ro.product.cpu.abi2]: [armeabi]
    def init_cpu_arch(self):
        cpu_arch_command = Adb_Util().device_info(
            self.deviceID,
            'ro.product.cpu.abi'
            )
        
        return cpu_arch_command
    
    
    #Find device sdk version using command ro.build.version.sdk
    def init_sdk(self):
        sdk_command = Adb_Util().device_info(
            self.deviceID,
            'ro.build.version.sdk'
            )
        
        return sdk_command
    
    
    def init_os(self):
        
        os_command = Adb_Util().device_info(
            self.deviceID,
            'ro.build.version.release'
            )
        
        return os_command
    

    def install(self, file_path):
        Adb_Util().install_package(file_path, self.deviceID)
        
        
    def install_bundle(self, file_path):
        Adb_Util().install_bundle(file_path, self.deviceID)
    
    
    def uninstall_all(self):
        if len(self.packageList) > 0:
            for package_name in self.packageList:
                if package_name not in self.exclude:
                    Adb_Util().unistall_package(self.deviceID, package_name)
            self.init_package_list()
        else:
            print("The amount of apps installed on device is currently 0")
    
            
    def uninstall(self, package_name):
        if len(self.packageList) > 0:
            Adb_Util().unistall_package(self.deviceID, package_name)
        else:
            print("The amount of apps installed on device is currently 0")
    
    
    def get_packageList(self):
        return self.packageList
    
    
    def __str__(self):
        return "Device name: {:s} \nDevice ID: {:s}\nOS Version: {:s}" \
            "SDK: {:s}cpu arch: {:s}Screen Density: {:s}\n" \
            .format(self.name,
                    self.deviceID,
                    self.os,
                    self.sdk,
                    self.cpu_arch,
                    self.screen_density)
    

    

# d3 = Device('RFCR71TEQWP')
# d3.uninstall_all()
# d1 = Device('A00000K580152200711')
# d2 = Device('RFCR71TEQWP')
# print(d1)
# print(d2)
# =============================================================================
# d3 = Device('R38M40EX5ZA')
# d3.uninstall_all()
# =============================================================================
# d1 = Device('A00000K580152200711', 'hdmix', 30, 'Go')
# d1.init_package_list()
# =============================================================================
# print(d1.packageList)
# print(d1.name)
# print(d1.init_screen_density())
# print(d1.screen_density)
# print(d1.sdk)
# print(d1.os)
# =============================================================================
# d1.uninstall_all()
# =============================================================================
