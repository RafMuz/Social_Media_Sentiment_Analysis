import snscrape.modules.twitter as twitter
import pandas as pd
import csv


# <editor-fold desc = "Twitter Functions">

def get_tweets (keyword: str, operators: str = '', max_tweets: int = None, print_output: bool = True):

    """
    Get Tweets from Twitter.

    :param keyword: The Tweets you want to find, e.x. 'BTC'.
    :type keyword: str

    :param operators: Here you can Filter out Tweets, e.x. 'since:2023-01-17 until:2023-01-18 lang:"en"'.
    :type operators: str

    :param max_tweets: The Max Number of Tweets to find ( If set to None then it will find all tweets ).
    :type operators: int

    :param print_output: Print some details about each Tweet.
    :type operators: bool

    :return: The Collected Tweets.
    :rtype: dict
    """

    # <editor-fold desc = "Variables">

    tweet_time = ['Tweet Time']
    username = ['Username']
    followers_count = ['Followers Count']
    tweet_content = ['Tweet Content']
    sentimental_score = ['Sentimental Score']

    tweets = {'Tweet Time': tweet_time, 'Username': username, 'Followers Count': followers_count, 'Tweet Content': tweet_content, 'Sentimental Score': sentimental_score}

    # </editor-fold>         # operators = 'since:2023-01-17 until:2023-01-18 lang:"en"'

    for i, tweet in enumerate (twitter.TwitterSearchScraper (keyword + ' ' + operators).get_items ()):

        if type (max_tweets) is not type (None):
            if i > max_tweets:
                break

        if print_output is True:

            print (i)
            print (tweet.user.username)
            print (tweet.user.followersCount)
            print (tweet.date)
            print (tweet.rawContent)
            print ('\n')

        tweets ['Tweet Time'].append (tweet.date.strftime ('%Y-%m-%d %H:%M:%S'))
        tweets ['Username'].append (tweet.user.username)
        tweets ['Followers Count'].append (tweet.user.followersCount)
        tweets ['Tweet Content'].append (str (tweet.rawContent.encode ('ascii', 'ignore')).lstrip ("b'").rstrip ("'"))
        tweets ['Sentimental Score'].append ('')

    return tweets


def save_tweets (data: dict, file_location: str):

    """
    Save Tweets to a CSV File.

    :param data: This is the Tweets.
    :type data: dict

    :param file_location: This is the File Location (Including File name).
    :type file_location: str
    """

    complete_file_location = file_location + '.csv'

    x = 0

    with open (complete_file_location, 'w', newline='') as file:
        writer = csv.writer (file)
        while x < len (data ['Tweet Content']):
            writer.writerow ([data ['Tweet Time'] [x], data ['Username'] [x], data ['Followers Count'] [x], data ['Tweet Content'] [x], data ['Sentimental Score'] [x]])

            x = x + 1

def read_tweets (complete_file_location):

    """
    Read Tweets ( From Saved Tweets File ).

    :param complete_file_location: The Complete File Location ( Including File name and Extension ).
    :type complete_file_location: str

    :return: Tweets from the File.
    :rtype: pandas.core.frame.DataFrame
    """

    data = pd.read_csv (complete_file_location)
    data ['Tweet Time'] = pd.to_datetime (data ['Tweet Time'])

    # df.set_index ('Tweet Time', inplace=True)
    # data_by_hour = df.groupby (pd.Grouper (freq='H')).sum ()

    return data

# </editor-fold>
