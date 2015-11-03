__author__ = 'seandolinar'

from emoji_parse import EmojiDict
from datetime import datetime


class TweetAnalysis(object):

    def __init__(self, tweet):

        self.screen_name = tweet.get('user').get('screen_name')
        self.followers = tweet.get('user').get('followers_count')
        self.friends = tweet.get('user').get('friends_count')
        self.verified = tweet.get('user').get('verified')

        self.text = tweet.get('text')
        self.datetime = datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
        # self.client =  #add in

        self.reply = tweet.get('in_reply_to_screen_name') is not None
        self.rt = tweet.get('retweeted_status') is not None
        self.rt_non_verified = tweet.get('retweeted_status') is not None and tweet.get('retweeted_status').get('user').get('verified') == False



    def emoji(self):

        emoji_counter = EmojiDict()
        emoji_counter.add_emoji_count(self.text)

        self.emoji_fl = emoji_counter.total_emoji >= 1
        self.emoji = emoji_counter.total_emoji
        self.total_emoji = emoji_counter.total_indiv_emoji

        self.human_emoji_dict = emoji_counter.skin_tones_dict
        self.human_emoji = emoji_counter.skin_tones_dict['human_emoji']

