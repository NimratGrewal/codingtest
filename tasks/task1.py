import tweepy
import pandas as pd


# personal keys and tokens from the developer account
# replaced with arbitrary strings but tried to use my own personal keys and
# tokens while web scraping.
api_key = 'XXX'
api_secret = 'XXX'
access_token = 'YYY'
access_token_secret = 'YYY'
bearer_token = 'ZZZ'

# used the tweepy package for conducting analysis. 
# also tried using OAuth2Handler and OAuth1Handler as well as the bearer class as well, but 
# nothing worked, i think because of authentication issues. 
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

# Create a Tweepy API object
api = tweepy.API(auth, wait_on_rate_limit=True)


# Define a function to get the information you want for a given Twitter account
def get_twitter_info(username): # pass in my username "_nimratg"
    results = api.search_users(q=username)
    if results:
        user = results[0]
        id_ = user.id
        user_name = user.username
        pinned_tweet_id = user.pinned_tweet_id
        creation_date = user.created_at
        return {'username': user_name,
                'id': id_,
                'creation date': creation_date,
                'pinned tweet id': pinned_tweet_id}
    else:
        print(f"No user found with username '{username}'")
        return None


# Loop through the list of Twitter accounts and get their information
twitter_info_list = []

for username in ['_nimratg']:
    twitter_info = get_twitter_info(username)
    if twitter_info:
        twitter_info_list.append(twitter_info)

# Convert the list of Twitter information into a Pandas DataFrame
df = pd.DataFrame(twitter_info_list)
# make this into a csv
df.to_csv('scraped_user_data.csv')

# I keep getting a 401 error, i think there might be something
# wrong with my authentication, although i tried running different scripts and
# also tried to regenerate the keys and tokens again. I have never used a
# twitter API before, so I also tried to just use
# the bearer token for the app only access, but that also generated the
# same results. So because of this my code won't run. But this is the structure
# of the format that i would apply.

# For the authentication, i also tried running the "curl" method on the shell,
# but that gave me the same error as well. I googled around a lot and also used
# some AI to potentially solve this problem, but could not find a sufficient
# answer to this. I think the keys and tokens are up to date, and my app is
# also in my projects folder in the developer account, it just keeps saying
# that i don't have access to use these fields. I think i might be missing
# something. But overall, this would be the presentation of my code.

# i also tried using twurl to use the api as well, so i had to change my ruby
# version to the newer one - since it kept not giving me permission to install
# twurl. So after googling around for awhile i was able to install twurl
# using "gem install twurl' command.then when inputting my consumer key
# and secret key, i got these errors "undefined method `Exception' for
# Twurl::CLI:Class (NoMethodError)" and "invalid option:
# --consumer-key (OptionParser::InvalidOption)". i tried googling
# those errors as well, and i think it all boils down to my oauth issue.
# whatever method i use to gain access to the twitter api, it does not
# authorize me to run these command line codes or my python script codes.
