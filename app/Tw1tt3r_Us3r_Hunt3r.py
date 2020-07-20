import os
import tweepy

BASE_URL = 'https://twitter.com/%s'
WHITELIST_FILE = "whitelist.txt"

# input of data used in code
consumer_key = input('Type your Consumer Key:')
consumer_secret = input('Type your Consumer Secret:')
access_token = input('Type your Access token:')
access_token_secret = input('Type your Access token secret:')
keyword = input('Type here the user related to be search: ')

# twitter authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#User to search for
query = keyword

# twitter method to search for users
searched_account = [status for status in api.search_users(q=query)]

whitelist_accounts = []
if os.path.isfile(WHITELIST_FILE):
    with open(WHITELIST_FILE, "r") as whitelist_handle:
        for line in whitelist_handle.readlines():
            whitelist_accounts.append(line.strip())

for user in searched_account:
#print responsible to create the list with users
    if user._json["screen_name"] not in whitelist_accounts:
        print(BASE_URL % user._json["screen_name"])
