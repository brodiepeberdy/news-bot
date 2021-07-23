import twitter
import requests

def auth():
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_secret = ''
    try:
        api = twitter.Api(consumer_key, consumer_secret, access_token, access_secret)
        print ("LOGGED INTO TWITTER.")
        return api
    except Exception as e:
        print (e + "TWITTER LOGIN FAILED.")

def tweet(api, message):
    try:
        status = api.PostUpdate(message)
        print ("Tweet posted.")
    except Exception as e:
        print (str(e) + "FAILED TO TWEET")

api = auth()

response = requests.get("https://www.reddit.com/r/worldnews/top.json?t=today&limit=5", headers = {'User-agent': 'Daily News Robot'})
for article in response.json()["data"]["children"]:
    new_tweet = article["data"]["title"] + " " + article["data"]["url"]
    print(new_tweet + str(len(new_tweet)))
    tweet(api, new_tweet)
