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
            "favorites": 53588,
            "retweets": 10836,
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


if __name__ == '__main__':
    unittest.main()
