# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 20:15:41 2022

@author: tommy
"""
import subprocess
import pathlib
import os
import zipfile
from Google_Play_Info import Google_Play_Info

class App:
    
    
    def __init__(self, directory="C:\\Users\\tommy\\CSC221\\Android_Project1",
                 file_name = "Null",
                 file_type="Null",
                 app_name="Null",
                 package_name="Null",
                 size=0.0,
                 developer="Null",
                 version="Null",
                 version_code="Null",
                 target_sdk="Null",
                 min_sdk="Null",
                 rating="Null",
                 maturity="Null",
                 flags=[]):
        
        self.file_name = file_name
        self.directory = directory
        self.app_name = app_name
        self.package_name = package_name
        self.developer = developer
        self.size = size
        self.file_type = 'Null'
        self.version = version
        self.version_code = version_code
        self.target_sdk = target_sdk
        self.min_sdk = min_sdk
        self.rating = rating
        self.maturity = maturity
        self.flags = flags
        
        
        self.init_file_type()
        if self.file_type == '.apk':
            self.extract_manifest(self.file_name)
            
        elif self.file_type == '.apks':
            self.extract_base_apk(self.file_name)
            self.extract_manifest('splits\\base.apk')
            os.remove('splits\\base.apk')
            os.rmdir('splits')
        else:
            raise Exception("Invalid file type")
        
        self.init_file_size()
        self.search = Google_Play_Info(self.package_name)
        self.init_app_name()
        self.init_app_developer()
        self.init_app_rating()
        self.init_app_maturity()
        
        
    def init_app_name(self):
        self.app_name = self.search.get_name()
        
    
    def init_app_developer(self):
        self.developer = self.search.get_developer()
        
        
    def init_app_rating(self):
        self.rating = self.search.get_rating()
            
   
    def init_app_maturity(self):
        self.maturity = self.search.get_maturity()

        
    def init_file_type(self):
        self.file_type = pathlib.Path(self.directory 
                                      + "\\" +self.file_name).suffix
        
        
    # Calculates files size in MB
    def init_file_size(self):
        self.size = os.path.getsize(self.file_name) / 1000000  
        
    
    def extract_base_apk(self, file_name):

        with zipfile.ZipFile(file_name) as apks:            
            apks.extract('splits/base.apk')
            
        #print("Successfully extracted base.apk\n")
        
            
    #aapt2 dump badging com.booking.apk
    def extract_manifest(self, file_name):
        package_info = {}
        manifest_command = subprocess.run(
            ['aapt', 'dump', 'badging', self.directory + '\\' + file_name],
            capture_output=True, shell=True)
        
        if manifest_command.returncode == 0:
            
            for line in manifest_command.stdout.decode('utf8').splitlines():
                #print(line)
                if line.__contains__("sdkVersion:"):
                    min_sdk_version = line.split("sdkVersion:")
                    min_sdk_version = min_sdk_version[1].split("'")
                    self.min_sdk = min_sdk_version[1]
                
                if line.__contains__("targetSdkVersion:"):
                    target_sdk_version = line.split("targetSdkVersion:")
                    #print("Before:", target_sdk_version)
                    target_sdk_version = target_sdk_version[1].split("'")
                    #print("After:", target_sdk_version)
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
        if self.file_type == '.apk' or self.file_type == '.apks':
            string = "File Name: {:s}\nFile Type {:s}\nApp Name: {:s}" \
                "\nPackage Name: {:s}\nDeveloper: {:s}" \
                "\nSize: {:.2f}\nVersion {:s}\nVersion Code: {:s}" \
                "\nTarget SDK: {:s}\nMin SDK: {:s}" \
                "\nStar Rating: {:s}\nMaturity: {:s}\n" \
                .format(self.file_name, self.file_type, self.app_name,
                        self.package_name, self.developer, 
                        self.size, self.version, self.version_code,
                        self.target_sdk, self.min_sdk, self.rating,
                        self.maturity)
        else:
            string = "Invalid file type: " + self.file_name
            
        return string
    
    
    
# os.chdir('C:\\Users\\tommy\\CSC221\\Android_Project1\\apk')     
# for file in os.listdir():
#     if pathlib.Path(file).suffix == '.apk' or  pathlib.Path(file).suffix == '.apks':
#         print(App('C:\\Users\\tommy\\CSC221\\Android_Project1\\apk', file))
#a1 = App('C:\\Users\\tommy\\CSC221\\Android_Project1\\apk', 'com.booking.apk')
#a1.extract_manifest('com.booking.apk')
# print(a1.min_sdk)
# print(a1.target_sdk)
#print(a1)
