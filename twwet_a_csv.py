# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 10:59:45 2019

@author: Estudiantes

"""

import tweepy
import csv
import pandas as pd

auth = tweepy.OAuthHandler("YAve8QoP6jEbswUj3wL1jnZqF", "OxXPta9Wx67GnOnmSmyR8dHAriXOfcEvpHlUpmXvqCq8YbyRZR")
auth.set_access_token("1138192133029072897-waIckoLbFnM4ZeOwkAOKSrjmMTji5N", "Vxlqf17CmexhIC1nPBXsoOYteV4xSZXQwTHz0GVqJrTor")

api = tweepy.API(auth,wait_on_rate_limit=True)

cricTweet = tweepy.Cursor(api.search, q='canción').items(20)
i=0
datos=[]
for tweet in cricTweet:
    i+=1
    print (i,tweet.created_at,":",tweet.text,tweet.lang) 
    datos=datos+[[tweet.created_at,tweet.text]]

dt=pd.DataFrame(datos,columns=['Fecha','Texto'])

                         
    
dt.to_csv('Tweets.csv')    

   