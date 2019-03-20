"""The Application central_bot's file"""
from flask import Flask
from flask import render_template, request
import os
import urllib.parse
import requests



class App():
    """This class made to send and get the data from the APIs"""
    def __init__(self, ask):
        self.ask = ask
        self.stopwords = []
        self.result = []

    def ReadSW(self):
        """ Method to creat a list of the words that 
        must be ignored to have a specific question """
        
        with open('app/stopwords.txt', 'r') as my_words :
            for line  in my_words:
                line = line.rstrip()
                self.stopwords.append(line)
        return self.stopwords

    
    def SelectWord(self):
        """Select and filter the world we need from the user input"""
        response = self.ask.split()
        
        for elt in response:
            if elt not in self.stopwords:
                self.result.append(elt)
        return ' '.join(self.result)
    
    def MediaWiki(self):
        """A Moethod to get the"""
        self.SelectWord()

        base_url = "http://fr.wikipedia.org/w/api.php"
        params_url = {"action": "opensearch",
                  "search": self.result[0],
                  "limit": "1",
                  "namespace": "0",
                  "format": "json"}
        
        ResultUrl = requests.get(url=base_url, params=params_url)
        
    
        return  "Pybot :"+"  Voila une petite histoire sur "+ self.result[0] + ' "'+ResultUrl.json()[2][0]+'".'
    
    def GooglGeo(self):
        """Geting the Geaoinformations about the user's task entred"""
        self.SelectWord()

        sendQts = self.result[0]
        APIKEY = 'AIzaSyAVO3bsHT5e9zsllBpmclvrYyvaIJ-FSHE'
        base_url = "https://maps.googleapis.com/maps/api/geocode/json?address="+sendQts+"&key="+APIKEY
        request = requests.get(base_url)
        jsRequest = request.json()
        target = jsRequest["results"]
        for elt in target:
            points = elt['geometry']['location']
        self.latitude = points['lat']
        self.longetude = points['lng']
        print('La longetude est : '+str(self.latitude) +'et latitudes est : '+ str(self.longetude))

    def GooglMapFrame(self):
        """Geting the localisation on the map"""
        self.GooglGeo()
        
        base_url = "https://www.google.com/maps/search/?api=1&query="+str(self.latitude)+','+str(self.longetude)
        print(base_url)