"""The Application central_bot's file"""
from flask import Flask
from flask import render_template, request
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
        
        response = self.ask.split()
        
        for elt in response:
            if elt not in self.stopwords:
                self.result.append(elt)
        return ' '.join(self.result)
    
    def MediaWiki(self, name):
        
        self.SelectWord()

        base_url = "http://fr.wikipedia.org/w/api.php"
        params_url = {"action": "opensearch",
                  "search": self.result[0],
                  "limit": "1",
                  "namespace": "0",
                  "format": "json"}
        
        ResultUrl = requests.get(url=base_url, params=params_url)
    
        return name + self.result[0] + "\n" + "Pybot :"+"  Voila une petite histoire sur "+ self.result[0] + ' "'+ResultUrl.json()[2][0]+'".'