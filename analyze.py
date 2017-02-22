from functools import *
import json


with open("tweets.json", "r") as tweet_db:
    tweets = json.load(tweet_db)

    def head(xs):
        if len(xs) == 0:
            return []
        else:
            return xs[0]

    def tail(xs):
        if len(xs) == 0:
            return []
        else:
            return xs[1:]

    def flatten(xs):
        if isinstance(xs, list):
            return [element for sublist in xs for element in flatten(sublist)]
        else:
            return [xs]

    def difference(xs, ys):
        """"Finds all the elements that are in either xs or ys, but not both"""
        # [everything that's in xs and not in ys] + [converse]
        return list(filter(lambda x: x not in ys, xs)) + list(filter(lambda y: y not in xs, ys))

    def to_text(tweets):
        """Converts from a list of tweets to a list of tweet contents"""
        return NotImplemented

    def to_lowercase(tweets):
        """Converts the content of each tweet in the list of tweets to lowercase"""
        return NotImplemented

    def nonempty(tweets):
        """remove all tweets with empty contents from the list of tweets"""
        return NotImplemented

    def total_word_count(tweets):
        return NotImplemented

    def hashtags(tweet):
        """get a list of all the hashtags in a tweet"""
        return NotImplemented

    def mentions(tweet):
        """get a list of all the mentions in a tweet"""
        return NotImplemented

    def all_hashtags(tweets):
        return NotImplemented

    def all_mentions(tweets):
        return NotImplemented

    def all_caps_tweets(tweets):
        """Returns a list of all tweets that are completely capitalized from the given list of tweets"""
        return NotImplemented


    def count_individual_words(tweets):
        """count word frequency and output as dictionary"""
        return NotImplemented

    def count_individual_hashtags(tweets):
        """count hashtag frequency and output as dictionary"""
        return NotImplemented

    def count_individual_mentions(tweets):
        return NotImplemented

    def n_most_common(n, word_count):
        """"Calculates the n most common keys in word_count ,
        sorted from most to least common and sorted in alphabetical order when the number of occurrences
        is the same."""
        return NotImplemented
    def iphone_tweets(tweets):
        """returns only the tweets from iphone"""
        return NotImplemented

    def android_tweets(tweets):
        return NotImplemented

    def average_favorites(tweets):
        """"Computes the average number of favorites from the list of
        tweets, rounding appropriately."""
        return NotImplemented

    def average_retweets(tweets):
        return NotImplemented

    def sort_by_favorites(tweets):
        """"sort tweets in ascending order of number of favorites"""
        return NotImplemented

    def sort_by_retweets(tweets):
        return NotImplemented

    def upper_quartile(tweets):
        """"Assuming the input is sorted, find the tweet representative of
        the upper quartile. This is the tweet representing the 75th percentile in the characteristic the list
        has been sorted by. You can compute it as 3/4th of the size of the input"""
        return NotImplemented

    def lower_quartile(tweets):
        """"Assuming the input is sorted, find the tweet representative of
        the lower quartile. This is the tweet representing the 25th percentile in the characteristic the list
        has been sorted by. You can compute it as 1/4th of the size of the input"""
        return NotImplemented

    def top_quarter_by(tweets, factor):
        """"Assuming the input is sorted by factor , find all
        tweets with factor greater than or equal to the upper quartile representative found using the
        upper_quartile function you’ve implemented"""
        return NotImplemented

    def bottom_quarter_by(tweets, factor):
        return NotImplemented

