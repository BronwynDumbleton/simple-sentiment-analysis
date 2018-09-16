from config import *
import tweepy
from textblob import TextBlob 
import re 

def clean_tweet(tweet): 
    ''' 
    Utility function to clean tweet text by removing links, special characters 
    using simple regex statements. 
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 
  
def get_tweet_sentiment(tweet): 
    ''' 
    Utility function to classify sentiment of passed tweet 
    using textblob's sentiment method 
    '''
    # create TextBlob object of passed tweet text 
    analysis = TextBlob(clean_tweet(tweet)) 
    # set sentiment 
    if analysis.sentiment.polarity > 0: 
        return 'positive'
    elif analysis.sentiment.polarity == 0: 
        return 'neutral'
    else: 
        return 'negative'


# Download tweets using the Tweepy API. The API returns tweets matching the 'query' keyword,
# and number of tweets downloaded equals 'max_tweets'.
def get_tweets(query, max_tweets):
    # Authentication is necessary to interact with the Twitter API through Tweepy.
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    tweets_return = []

    print "Downloading {0} tweets".format(max_tweets)

    i = 1
    # Make use of the Cursor function, that automatically paginates across pages while searching
    # for tweets.
    for tweet in tweepy.Cursor(api.search,
                           q=query,
                           result_type="recent",
                           include_entities=True,
                           lang="en").items():
        
        # Store each tweet's tweet.user.name (twitter name), tweet.user.screen_name (twitter handle),
        # and tweet.text (tweet message).
        tweets_return.append([tweet.user.name, tweet.user.screen_name, tweet.text])
        if i >= int(max_tweets):
        	break
        else:
        	i += 1

    print "Downloaded {0} tweets".format(len(tweets_return))
    return tweets_return

def nice_print(tweet_info):
    print "User",tweet_info[0],"with handle",tweet_info[1],"tweeted the following with a sentiment score of",get_tweet_sentiment(tweet_info[2])
    print tweet_info[2]
    print "\n"

tweets = get_tweets("Donald Trump", 10)

for t in tweets:
    nice_print(t)