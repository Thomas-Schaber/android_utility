# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 18:07:16 2022

@author: tommy
"""
import pandas as pd


class Apk_Processor:
    def __init__(self, app_list):
        if len(app_list) == 0:
            print("No apps to process")
        
        else:
            self.app_list = app_list
            self.data = pd.DataFrame()
            self.process()
            self.create_csv()
        
        
    def process(self):
        
        app_name = []
        package = []
        dev = []
        version = []
        version_code = []
        size = []
        sideload = []
        single_file = []
        app_open = []
        app_close = []
        roadblock = []
        sdk_inspection = []
        app_match_description = []
        google_reviews = []
        app_renders = []
        prohib_content = []
        target_sdk = []
        min_sdk = []
        device_compat = []
        invasive_ads = []
        app_scans = []
        uninstall = []
        conversion = []
        flags = []
        
        for app in self.app_list:
            #print(app.app_name, app.developer, app.package_name)
            app_name.append(app.app_name)
            package.append(app.package_name)
            dev.append(app.developer)
            version.append(app.version)
            version_code.append(app.version_code)
            size.append(app.size)
            sideload.append("")
            
            if app.file_type == ".apks":
                single_file.append("Warn")
            elif app.file_type == "apk":
                single_file.append("Pass")
                
            app_open.append("")
            
            
            
            
        self.data['app_name'] = app_name
        self.data['package'] = package
        self.data['developer'] = dev
        self.data['version_name'] = version
        self.data['version_code'] = version_code
        self.data['size'] = size
        self.data['sideload'] = sideload
        self.data['single_file'] = single_file
        self.data['app_open'] = app_open
        
        
    
    def create_csv(self):
        self.data.to_csv("package_info.csv")