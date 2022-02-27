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
            print(len(app_list))
            self.app_list = app_list
            self.data = pd.DataFrame()
            self.process()
            self.create_csv()
        
        
    def process(self):
        
        app_name = []
        package = []
        dev = []
        
        for app in self.app_list:
            print(app.app_name, app.developer, app.package_name)
            app_name.append(app.app_name)
            package.append(app.package_name)
            dev.append(app.developer)
            
        self.data['app_name'] = app_name
        self.data['package'] = package
        self.data['developer'] = dev
            
    
    def create_csv(self):
        self.data.to_csv("package_info.csv")