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
        self.app_name_class = "Fd93Bb"
        self.app_dev_class = "Vbfug auoIOc"
        self.app_rating_class = "TT9eCd"
        self.app_maturity_class = "ClM7O"

        pass
    
    
    def get_name(self):
        try:
            name = self.soup.find("h1", class_=self.app_name_class).find("span").text
            #print(name)
            return name
        except Exception as e:
            #print("Failed to get name from Google Play")
            #self.soup = BeautifulSoup(self.page, "html.parser")
            #name = self.soup.find("h1", class_=self.app_name_class).find("span").text
            #print(name)
            print("Did not find name retrying for package ", self.package_name)
            print(e)
            return "null"
    
    def get_developer(self):
        try:

            developer = self.soup.find("div", {'class':self.app_dev_class})
            developer = developer.findChild("span").text

            #developer = self.soup.find("a", class_=self.app_dev_class).text
            #print(developer)
            return developer
        except Exception as e:
            print("Failed to pull developer from Google Play:", self.package_name)
            print(e)
            #print(self.soup.prettify())

            return "null"

     
    def get_rating(self):
        try:
            rating = self.soup.find("div", class_=self.app_rating_class).text
            rating = rating.split('s')[0]
            return rating
        except Exception as e:
            print("No star rating for package:", self.package_name)
            #print(e)
            return '0'

    
    def get_maturity(self):
        try:
            maturity = self.soup.find("div", class_="q078ud").text
            return maturity
        except Exception as e:
            #print("Failed to pull maturity for:", self.package_name)
            #print(e)

            return "null"

    def retry(self):
        self.page = requests.get(self.URL + self.package_name).text
        self.soup = BeautifulSoup(self.page, "html.parser")
    
# print(Google_Play_Info('com.booking').get_name())
#print(Google_Play_Info('com.booking').get_developer())
# print(Google_Play_Info('com.booking').get_rating())
# print(Google_Play_Info('com.booking').get_maturity())
    
