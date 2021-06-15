from requests import get
import os, re, os.path
from time import sleep
import tweepy
import json
from config import keys, customisation, language, botdelay
consumer_key = keys.consumer_key
consumer_secret_key = keys.consumer_secret_key
access_token = keys.access_token
access_token_secret = keys.access_token_secret
Heading = customisation.Heading
Brackets = customisation.Brackets
point = customisation.point
language = language.Language
BotDelay = botdelay.SleepDelay
print(f"\n\nWelcome to Swift-Nite's Shop Section Bot!\nYour Delay is {BotDelay} seconds.\n\n")

def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    count = 1
    apiurl = f'https://fn-api.com/api/shop/sections?lang={language}'

    response = get(apiurl)
    newsData = response.json()['data']['hash']

    while 1:
        response = get(apiurl)
        if response:
            newsDataLoop = response.json()['data']['hash']
            print("Checking for change in the Shop Sections... ("+str(count)+")")
            count = count + 1
            
            if newsData != newsDataLoop:

                print('\nShop sections have changed!')
                sleep(3)
                response = get(f'https://fn-api.com/api/shop/sections?lang={language}')
                ss = response.json()['data']['sections']
                sections = ""

                for i in ss:
                    #print(f'{i["sectionName"]} - (x{i["quantity"]})\n')
                    sections += f'{i["name"]} - (x{i["quantity"]})\n'

                print(sections)

                print('\nTweeting out the current shop sections...')
                
                api.update_status(f'#Fortnite Shop Sections Update:\n\n'+str(sections))
                print('Tweeted out the shop sections!')
                main()
        else:
            print("FAILED TO GRAB SHOP SECTIONS DATA: URL DOWN")

        sleep(BotDelay)

main()
