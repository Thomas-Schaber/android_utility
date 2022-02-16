# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 20:15:41 2022

@author: tommy
"""
import subprocess

class App:
    
    
    def __init__(self, directory="C:\\Users\\tommy\\CSC221\\Android_Project1",
                 app_name="Null",
                 package_name=None,
                 size=0,
                 developer="Null",
                 version=None,
                 version_code=None,
                 target_sdk=None,
                 min_sdk=None,
                 rating="Null",
                 maturity="Null",
                 flags=None):
        
        self.app_name = app_name
        self.package_name = package_name
        self.developer = developer
        self.size = size
        self.version = version
        self.version_code = version_code
        self.target_sdk = target_sdk
        self.min_sdk = min_sdk
        self.rating = rating
        self.maturity = maturity
        self.flags = flags
        
    
    #aapt2 dump badging com.booking.apk
    def extract_manifest(self, file_name):
        package_info = {}
        manifest_command = subprocess.run(
            ['aapt', 'dump', 'badging', file_name],
            capture_output=True, shell=True)
        
        if manifest_command.returncode == 0:
            
            for line in manifest_command.stdout.decode('utf8').splitlines():
                
                if line.__contains__("sdkVersion"):
                    min_sdk_version = line.split("sdkVersion:")
                    min_sdk_version = min_sdk_version[1].split("'")
                    self.min_sdk = min_sdk_version[1]
                
                if line.__contains__("targetSdkVersion"):
                    target_sdk_version = line.split("targetSdkVersion:")
                    target_sdk_version = target_sdk_version[1].split("'")
                    self.target_sdk = target_sdk_version[1]
                
                if line.__contains__("package"):
    
                    package_line = line.split("'")
                    package_line.pop(-1)
    
                    for x in range(0, len(package_line), 2):
                        package_info.update(
                            {package_line[x]: package_line[x+1]}
                            )
                    
                    self.package_name = package_info.get("package: name=")
                    self.version_code = package_info.get(" versionCode=")
                    self.version = package_info.get(" versionName=")
                    
        else:
            print("An error occured when extracting manifest", 
                  manifest_command.stderr)
    
            
    def __str__(self):
        string = "App Name: {:s}\nPackage Name: {:s}\nDeveloper: {:s}" \
            "\nSize: {:.2f}\nVersion {:s}\nVersion Code: {:s}" \
            "\nTarget SDK: {:s}\nMin SDK: {:s}" \
            "\nStar Rating: {:s}\nMaturity: {:s}" \
            .format(self.app_name, self.package_name, self.developer, 
                    self.size, self.version, self.version_code,
                    self.target_sdk, self.min_sdk, self.rating, self.maturity)
        return string
            
            
a1 = App()
a1.extract_manifest('C:\\Users\\tommy\\CSC221\\Android_Project1\\com.booking.apk')
print(a1.min_sdk)
print(a1.target_sdk)
print(a1)
