# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 14:34:12 2022

@author: tommy
This class scraps app in formation from Google Play and returns app info
"""
import requests
from bs4 import BeautifulSoup

class Google_Play_Info:
    
    
    def __init__(self, package_name):
        self.URL = 'https://play.google.com/store/apps/details?id='
        self.package_name = package_name
        self.page = requests.get(self.URL + self.package_name).text
        self.soup = BeautifulSoup(self.page, "html.parser")
        self.app_name_class = "AHFaub"
        self.app_dev_class = "hrTbp R8zArc"
        self.app_rating_class = "BHMmbe"
        self.app_maturity_class = "KmO8jd"

        pass
    
    
    def get_name(self):
        
        name = self.soup.find("h1", class_=self.app_name_class).find("span").text

        return name
    
    
    def get_developer(self):

        developer = self.soup.find("a", class_=self.app_dev_class).text
        
        return developer

     
    def get_rating(self):
        try:
            rating = self.soup.find("div", class_=self.app_rating_class).text
        except Exception as e:
            print("No star rating for package:", self.package_name)
            return '0'
            
        return rating
        
    
    def get_maturity(self):
        
        maturity = self.soup.find("div", class_=self.app_maturity_class).text
        
        return maturity
        
    
# print(Google_Play_Info('com.booking').get_name())
# print(Google_Play_Info('com.booking').get_developer())
# print(Google_Play_Info('com.booking').get_rating())
# print(Google_Play_Info('com.booking').get_maturity())
    
