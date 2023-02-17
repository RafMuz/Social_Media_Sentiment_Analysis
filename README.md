# Social Media Sentiment Analysis
A Library for webscraping social media platforms (twitter) and using sentiment analysis on them!

## Installation

	pip install social_media_sentiment_analysis


## Get started
Get Tweets from twitter and apply sentiment analysis on it:

~~~Python
# Import Library's
import pandas
from Social_Media_Sentiment_Analysis import Social_Media
from Social_Media_Sentiment_Analysis import NLP_Classification as Classify

tweets = Social_Media.get_tweets ('BTC', 'lang:"en"', 128)  # Get Tweets
tweets, twitter_score = Classify.twitter_indicator (tweets) # Apply Sentiment Analysis

Social_Media.save_tweets (tweets, 'tweets')                 # Save Tweets
tweets = pandas.read_csv ('tweets.csv')                     # Read Tweets

# Print the Results
print (tweets)
print ('\n{0}'.format (twitter_score))
~~~

Documentaion: https://social-media-sentiment-analysis.readthedocs.io/en/latest/

And that's the end of the Readme, Thanks for Reading!
