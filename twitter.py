#!/usr/bin/env python
# -*- coding=utf-8 -*-

import urllib2, time

from twython import Twython

consumer_key = 'your_stuff'
consumer_secret = 'your_stuff'
access_token = 'your_stuff'
access_token_secret = 'your_stuff'

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
anterior = "0-0"

while(1) :

    response = urllib2.urlopen('http://www.radiovoltrega.com/arasona/data.txt')
    resposta = response.read()
    if resposta != "Fórmula 107.8" :
        message = "Ara Sona: " + resposta

        if anterior != message :
            twitter.update_status(status=message)
            anterior = message
            print("Tweeted: {}".format(message))
        
    time.sleep(15)



