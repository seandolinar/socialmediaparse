__author__ = 'seandolinar'
__version__ = '0.0.0'

import collections as col

class HashtagParse(object):

    def __init__(self):

        self.list = []
        self.dict = {}

    def count(self, text, case=False):

        '''
        finds and returns all the hashtags
        while adding them to the internal counter
        no support for multiple hastags per item
        '''

        if not case:
            text = text.lower()

        text = text.replace('#', ' #')
        hash_dict = list({tag for tag in text.split() if tag.startswith("#")})

        temp_dict = self.dict
        self.dict = col.Counter(temp_dict) + col.Counter(hash_dict)

        return hash_dict






