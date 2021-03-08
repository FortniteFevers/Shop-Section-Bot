'''
The section below is your twitter develepor keys & tokens required for posting to your twitter!
You must have a twitter dev account of which you can apply for at https://developer.twitter.com/ 
You must create an app to acess your keys at https://developer.twitter.com/en/portal/projects-and-apps 
Whatever you name your app is what will appear as the source of where your tweet was posted from eg. Twitter for iPhone
'''
class keys:
    consumer_key: str = "Paste Key Here" #this is found under the Consumer Keys section and is the API key
    consumer_secret_key: str = "Paste Key Here" #this is found under the Consumer Keys section and is the Secret API key
    access_token: str = "Paste Key Here" #this is found under Authentication Tokens and is the Access token
    access_token_secret: str = "Paste Key Here" #this is found under Authentication Tokens and is the Secret Access token

'''
The below section is for the customisation of the tweet itself
'''
class customisation:
    Heading: str = f"Today's Shop Sections!" #this will be the text displayed in the post above the sections
    Brackets: bool = "True" #NOTE: THIS IS EITHER True or False! True means that the quantity will have brackets around it -> (X7) false means it won't -> X7
    point: str = "-" #this is the thing that will appear before the section name, For example it would currently look like -Marvel (X7), you can change the - before the section name if you wish. NOTE: not everything works!!

'''
If you have any issues please message me on discord or twitter and I will respond as quick as possible!!
Twitter: @SwiftNite
Discord: Swift-nite#3722
'''