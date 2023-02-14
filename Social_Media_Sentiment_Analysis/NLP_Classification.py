from flair.models import TextClassifier
from flair.data import Sentence

# <editor-fold desc = "NLP Functions">

def twitter_indicator (data, print_output: bool = True):

    """
    Take the Tweets and Apply Sentimental Analysis on them.

    :param data: The Tweets.
    :type data: dict

    :param print_output: Print some details about each Tweets Sentiment Score.
    :type print_output: str

    :return: The Tweets with the Sentimental Score Added for each tweet and The Combined Sentimental Score.
    :rtype: dict and float
    """

    data, sentimental_analysis = classify_tweets (data, print_output)
    twitter_score = tweet_score (sentimental_analysis [1:-1])

    return data, twitter_score

# <editor-fold desc = "Twitter Functions">

def classify_tweets (data, print_output: bool = True):

    """
    The Sentimental Analysis part of Twitter Indicator.

    :param data: The Tweets.
    :type data: dict

    :param print_output: Print some details about each Tweets Sentiment Score.
    :type print_output: str

    :return: The Tweets with the Sentimental Score Added for each tweet and The Sentimental Score in a List.
    :rtype: dict and list
    """

    sentimental_analysis = ['Sentimental Score']

    classifier = TextClassifier.load ('en-sentiment')

    for tweet_content in data ['Tweet Content'] [0:-1]:

        sentence = Sentence (tweet_content)
        classifier.predict (sentence)

        # print sentence with predicted labels
        # if print_output is True: print ('Sentence above is: ', sentence.labels)

        for label in sentence.labels:
            if label.value == 'NEGATIVE':
                sentimental_analysis.append (-label.score)

                if print_output is True: print ('{0}   {1}'.format (-label.score, sentence.labels))

            else:
                sentimental_analysis.append (label.score)

                if print_output is True: print ('{0}   {1}'.format (label.score, sentence.labels))


    data ['Sentimental Score'] = sentimental_analysis

    return data, sentimental_analysis

def tweet_score (sentimental_analysis_data):

    """
    Take all the Sentiment Analysis Values and make it into one score.

    :param sentimental_analysis_data: The Sentimental Analysis Scores.
    :type sentimental_analysis_data: list

    :return: The Final Score of the Sentimental Analysis Scores List.
    :rtype: float
    """

    sentimental_analysis_score = 0

    for sentimental_score in sentimental_analysis_data:
        sentimental_analysis_score += sentimental_score

    sentimental_analysis_score = (min_max (sentimental_analysis_score, -len (sentimental_analysis_data), len (sentimental_analysis_data))) * 100
    # print ("Final Sentiment Score is: {0}".format (sentimental_analysis_score))

    return sentimental_analysis_score

# </editor-fold>

# </editor-fold>

# <editor-fold desc = "Helper Functions">

# Do Min-Max Normalization
def min_max (value, min, max):

    """
    Take all the Sentiment Analysis Values and make it into one score.

    :param value: The Value you want to Min Max.
    :type value: float

    :param min: The Minimum value for the Min Max Operation.
    :type min: float

    :param max: The Maximum value for the Min Max Operation.
    :type max: float

    :return: The Min Maxed Value
    :rtype: float
    """

    min_max_value = (value - min) / (max - min)
    min_max_value = float ("{:.2f}".format (min_max_value))

    return min_max_value

# </editor-fold>
