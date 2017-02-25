import unittest
from analyze import *


class AnalyzeSpec(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.tweets = [{
            "username": "Donald J. Trump",
            "source": "Twitter for Android",
            "content": "The judge opens up our country to potential terrorists and others that do not have our best interests at heart. Bad people are very happy!",
            "favorites": 58128,
            "retweets": 13167,
            "number": 1
        }, {
            "username": "Donald J. Trump",
            "source": "Twitter for Android",
            "content": "Interview with @oreillyfactor on Fox Network - 4:00 P.M. (prior to Super Bowl). Enjoy!",
            "favorites": 35399,
            "retweets": 6303,
            "number": 2
        }, {
            "username": "Donald J. Trump",
            "source": "Twitter for Android",
            "content": "Why aren't the lawyers looking at and using the Federal Court decision in Boston, which is at conflict with ridiculous lift ban decision?",
            "favorites": 53588,
            "retweets": 10836,
            "number": 3
        }, {
            "username": "Donald J. Trump",
            "source": "Twitter for Android",
            "content": "",
            "favorites": 53587,
            "retweets": 10835,
            "number": 4
        }]

    def test_flatten(self):
        self.assertEqual(flatten([1, [2, 3, 4], [5, 6], [7, [8]]]), [1, 2, 3, 4, 5, 6, 7, [8]])

    def test_difference(self):
        self.assertEqual(difference([1, 2, 3], [1, 2, 4]), [3, 4])

    def test_to_text(self):
        self.assertEqual(to_text(self.tweets),
                         ["The judge opens up our country to potential terrorists and others that do not have our best interests at heart. Bad people are very happy!",
                          "Interview with @oreillyfactor on Fox Network - 4:00 P.M. (prior to Super Bowl). Enjoy!",
                          "Why aren't the lawyers looking at and using the Federal Court decision in Boston, which is at conflict with ridiculous lift ban decision?",
                          ""])

    def to_numbers(self, tweets):
        print(list(map(lambda x: x["number"], nonempty(tweets))))

    def test_nonempty(self):
        self.assertEqual(nonempty(self.tweets), self.tweets[:3])

    def test_total_word_count(self):
        self.assertEqual(total_word_count(self.tweets), 63)

    def test_words_with_char(self):
        tweet = {
            "username": "Donald J. Trump",
            "source": "Twitter for Android",
            "content": "#1 #2 3 @1 @2",
            "favorites": 53588,
            "retweets": 10836,
            "number": 4
        }
        self.assertEqual(hashtags(tweet), ["#1", "#2"])
        self.assertEqual(mentions(tweet), ['@1', '@2'])

    def test_all_words_with(self):
        self.assertEqual(all_mentions(self.tweets), ["@oreillyfactor"])

    def test_all_caps_tweets(self):
        tweet = {
            "username": "Donald J. Trump",
            "source": "Twitter for Android",
            "content": "#1 #2 3 @1 @2 ASDASDASD",
            "favorites": 53588,
            "retweets": 10836,
            "number": 4
        }
        self.assertEqual(all_caps_tweets(self.tweets + [tweet]), [tweet])

    def test_n_most_common(self):
        word_count = {
            "word_1": 1,
            "word_2": 2,
            "word_3": 3,
            "word_4": 4,
            "z_word_5": 5,
            "word_5": 5
        }
        self.assertEqual(n_most_common(3, word_count), [("word_4", 4), ("word_5", 5), ("z_word_5", 5)])

    def test_tweets_from_source(self):
        tweet = {
            "username": "Donald J. Trump",
            "source": "Twitter for iPhone",
            "content": "#1 #2 3 @1 @2 ASDASDASD",
            "favorites": 53588,
            "retweets": 10836,
            "number": 4
        }
        alternate_tweets = self.tweets + [tweet]
        self.assertEqual(android_tweets(alternate_tweets), self.tweets)
        self.assertEqual(iphone_tweets(alternate_tweets), [tweet])

    def test_average_x(self):
        self.assertEqual(average_favorites(self.tweets), 50176)
        self.assertEqual(average_retweets(self.tweets), 10285)

    def nums(self, tweets):
        return list(map(lambda x: x["number"], tweets))

    def test_sort_by(self):
        self.assertEqual(sort_by_favorites(self.tweets), [self.tweets[1], self.tweets[3], self.tweets[2], self.tweets[0]])

    def test_top_quarter_by(self):
        self.assertEqual(top_quarter_by(self.tweets, "favorites"), [self.tweets[0]])
        self.assertEqual(bottom_quarter_by(self.tweets, "retweets"), [self.tweets[1]])

if __name__ == '__main__':
    unittest.main()
