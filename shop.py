from requests import get
import os, re, os.path
from time import sleep
import tweepy
import json
from config import keys, customisation
consumer_key = keys.consumer_key
consumer_secret_key = keys.consumer_secret_key
access_token = keys.access_token
access_token_secret = keys.access_token_secret
Heading = customisation.Heading
Brackets = customisation.Brackets
point = customisation.point
print("\n\nWelcome to Swift-Nite's Shop Section Bot!\n\n")

def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    response = get('https://fn-api.com/api/shop_categories')
    if response:
        main = get('https://fn-api.com/api/shop_categories')
        stamp = main.json()['timestamp']
        res = main.json()['shopCategories']
        with open('cache.json', 'r') as fnapi_file:
            old = json.load(fnapi_file)
        if stamp != old:
            print("changes detected!")
            my_file = open(f"sections.txt","w+")
            my_file.write(f"{Heading}\n\n")
            for i in res:
                name=i["sectionName"]
                if i["quantity"] != 1:
                    quantity=i["quantity"]
                    if Brackets is True:
                        quantity=f" (X{quantity})"
                    else:
                        quantity=f" X{quantity}"
                else:
                    quantity=''
                my_file.write(f"{point}{name}{quantity}\n")
            my_file = open(f"sections.txt","r")
            file_contents = my_file.read()
            print (file_contents)
            api.update_status(f"{file_contents}")
            print("Posted!")
            my_file.close()
            with open('cache.json', 'w') as file:
                json.dump(stamp, file, indent=3)
    else:
        print("error")
if __name__ == "__main__":
    while True:
        print("Checking for section changes!")
        main()
        sleep(20)

 

