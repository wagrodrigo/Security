import tweepy


# twitter authentication
auth = tweepy.OAuthHandler('Consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')


api = tweepy.API(auth)



base_url = 'https://twitter.com/%s'


query = 'keyword'
searched_account = [status for status in api.search_users(q=query)]

for user in searched_account:
    print(base_url % user._json["screen_name"])