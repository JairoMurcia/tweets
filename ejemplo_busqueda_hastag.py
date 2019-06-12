# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 10:59:45 2019

@author: Estudiantes

"""

import tweepy
import csv
import pandas as pd

auth = tweepy.OAuthHandler("YAve8QoP6jEbswUj3wL1jnZqF", "OxXPta9Wx67GnOnmSmyR8dHAriXOfcEvpHlUpmXvqCq8YbyRZR ")
auth.set_access_token("1138192133029072897-waIckoLbFnM4ZeOwkAOKSrjmMTji5N ", "Vxlqf17CmexhIC1nPBXsoOYteV4xSZXQwTHz0GVqJrTor")

api = tweepy.API(auth,wait_on_rate_limit=True)

csvFile = open('ua.csv', 'a')

csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#FútbolGratis",count=50,lang="en",since="2019-06-11").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])