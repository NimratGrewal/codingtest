import pandas as pd
import task1
import requests

# set up your authentication credentials
consumer_key = task1.api_key
consumer_secret = task1.api_secret
access_token = task1.access_token
access_token_secret = task1.access_token_secret
bearer_token = task1.bearer_token

# create a Tweepy Client object
# set up the API endpoint and headers
# since we can use the bearer token for the tweet endpoints, i used that here
# instead of the consumer key and access keys.
endpoint = "https://api.twitter.com/2/tweets" # endpoint usage
headers = {"Authorization": f"Bearer {bearer_token}"} #authentication for this
#endpoint

# retrieve the text of the tweets with the given IDs and store them in a
# DataFrame
tweet_ids = [
    '1540348242960846849',
    '1540345715616006148',
    '1540341761658085376',
    '1540338100521603074',
    '1521296227291312133',
    '1540343622486327296',
    '1521328439759761408',
    '1540337296473526272',
    '1540405941094326272',
    '1522330619618996225'
]

tweets = []
for tweet_id in tweet_ids:
    params = {"ids": tweet_id, "tweet.fields": "text"}
    response = requests.get(endpoint, headers=headers, params=params)

    if response.status_code == 200: # if there is valid data
        data = response.json()["data"]
        if data:
            tweets.append({'id': data[0]['id'], 'text': data[0]['text']})
    else:
        print(f"Error retrieving tweet {tweet_id}: {response.text}")

df = pd.DataFrame(tweets)
print(df.head())
