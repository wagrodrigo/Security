import os
import sys
import json
import tweepy


BASE_URL = 'https://twitter.com/%s'
CREDENTIALS_FILE = "credentials.json"
WHITELIST_FILE = "whitelist.txt"

default_credentials = {
    "consumer_key": None,
    "consumer_secret": None,
    "access_token": None,
    "access_token_secret": None
}

def get_input(prompt: str) -> str:
    """Prompts user for input"""
    pass


def load_whitelist():
    """Loads whitelisted accounts from file whitelist.txt"""
    if os.path.isfile(WHITELIST_FILE):
        try:
            with open(WHITELIST_FILE, "r") as whitelist_handle:
                data = [line.strip() for line in whitelist_handle.readlines()]
                return data
        except Exception as ex:
            print(ex)
    return []


def load_credentials():
    """Load credentials from file credentials.json"""
    if os.path.isfile(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, "r") as credentials_handle:
            try:
                data = json.load(credentials_handle)
                return data
            except Exception as ex:
                print(ex)
    return default_credentials


def save_credentials(data: dict) -> bool:
    """Save credentials to file"""
    with open(CREDENTIALS_FILE, "w") as credentials_handle:
        json.dump(data, credentials_handle)


# load credentials from file if it exists
credentials = load_credentials()

# input of data used in code
credentials["consumer_key"] = credentials["consumer_key"] or input('Type your Consumer Key:')
credentials["consumer_secret"] = credentials["consumer_secret"] or input('Type your Consumer Secret:')
credentials["access_token"] = credentials["access_token"] or input('Type your Access token:')
credentials["access_token_secret"] = credentials["access_token_secret"] or input('Type your Access token secret:')
keyword = input('Type here the user related to be search: ')

# twitter authentication
auth = tweepy.OAuthHandler(credentials["consumer_key"], credentials["consumer_secret"])
auth.set_access_token(credentials["access_token"], credentials["access_token_secret"])
api = tweepy.API(auth)

# twitter method to search for users
searched_account = [status for status in api.search_users(q=keyword)]

# Reading of whitelist.txt that contains que whitelist user
whitelist_accounts = load_whitelist()

#print responsible to create the list with users comparing the result with whitelist
for user in searched_account:
    if user._json["screen_name"] not in whitelist_accounts:
        print(BASE_URL % user._json["screen_name"])
