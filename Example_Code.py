
"""
# exactPhrase ('"BTC"')
# save_tweets (tweets, '', 'tweets', '.csv')

data = read_tweets ('tweets.csv')
print (data)

sentimental_analysis = classify_tweets (data)

data ['Sentimental Score'] = sentimental_analysis

# pd.set_option ('display.max_rows', None)
# pd.set_option ('display.max_columns', None)

# print (data)

print (sentimental_analysis)"""

import Social_Media_Sentiment_Analysis as SM_SA

from Social_Media_Sentiment_Analysis import Social_Media
from Social_Media_Sentiment_Analysis import NLP_Classification as Classify

import pandas

# Get Tweets and Apply Sentimental Analysis to it
tweets = Social_Media.get_tweets ('BTC', 'lang:"en"', 32, True)
tweets, twitter_score = Classify.twitter_indicator (tweets, True)

# Save Tweets and Load it in an a Pandas Dataframe
Social_Media.save_tweets (tweets, 'tweets')
tweets = pandas.read_csv ('tweets.csv')


print ('\nTweet Time Length: {0}'.format (len (tweets ['Tweet Time'])))
print ('Username Length: {0}'.format (len (tweets ['Username'])))
print ('Followers Count Length: {0}'.format (len (tweets ['Followers Count'])))
print ('Tweet Content Length: {0}'.format (len (tweets ['Tweet Content'])))
print ('Sentimental Score Length: {0}\n'.format (len (tweets ['Sentimental Score'])))

print (tweets)

print ('\n{0}'.format (twitter_score))

