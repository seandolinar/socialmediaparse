__author__ = 'seandolinar'
__version__ = '0.1.0'

import collections as col
import pandas as pd
import re

class HashtagParse(object):

    def __init__(self):

        self.list = []
        self.dict = {}
        self.baskets = []

    def count(self, text, case=False):

        '''
        finds and returns all the hashtags
        while adding them to the internal counter
        no support for multiple hastags per item
        '''

        if not case:
            text = text.lower()

        text = text.replace('#', ' #')
        text = re.sub(r'([^A-Za-z1-9# ])', ' ', text)


        hash_dict = list({tag for tag in text.split() if tag.startswith("#")})

        temp_dict = self.dict
        self.dict = col.Counter(temp_dict) + col.Counter(hash_dict)

        if hash_dict != []:
            self.baskets.append(hash_dict)

        return hash_dict

    def create_csv(self, file='hashtag_out.csv'):

        hashtag_items = self.dict.items()

        hashtag_count_df = pd.DataFrame(hashtag_items, columns=['hashtag', 'total'])

        with open(file, 'w') as f:
            hashtag_count_df.to_csv(f, sep=',', index = False, encoding='utf-8')
        return



