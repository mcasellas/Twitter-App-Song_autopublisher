#!/usr/bin/env python
# -*- coding=utf-8 -*-

import urllib2, time

from twython import Twython

consumer_key = 'Ao9Jse36YR4I1iPQylbACEqe3'
consumer_secret = 'CWnfv2EgdFzkSNC64V511dTSA6tj0jDYWcw4bse3TZOWwtVZvs'
access_token = '957639945576951808-6N8BpEAq7JJ6iVJOjzRMfxQDCImkH6H'
access_token_secret = '3jhJDjq8LCuEpxXQ9xvHFchrfd0tS0I5gGmGxso2d6BeC'

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



