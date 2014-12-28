__author__ = 'seandolinar'
__version__ = '0.0.0'


import os
import pandas as pd

class EmojiDict(object):

    def __init__(self):

        #calls the emoji table in the data folder in the package
        file_path = os.path.dirname(os.path.abspath(__file__))
        emoji_key = pd.read_csv(file_path + '/data/' + 'emoji_table.txt', encoding='utf-8', index_col=0)
        
        #intialize emoji count
        emoji_key['count'] = 0
        emoji_dict = emoji_key['count'].to_dict()
        emoji_dict_total = emoji_key['count'].to_dict()

        self.dict = emoji_dict
        self.dict_total = emoji_dict_total
        self.emoji_list = emoji_dict.keys()
        self.baskets = []



    def add_emoji_count(self, text):

        #increments a count if an emoji as present
        emoji_basket = []
        for emoji in self.emoji_list:

            if emoji in text:
                self.dict[emoji] += 1
                emoji_basket.append(emoji)

            self.dict_total[emoji]  += text.count(emoji)

        self.baskets.append(emoji_basket)

        return


    def create_csv(self, file='emoji_out.csv', total=False):


        emoji_df_total = self.dict_total.items()
        emoji_df_unique = self.dict.items()


      

        emoji_count = pd.DataFrame(emoji_df_total, columns=['emoji', 'total'])
        emoji_unique = pd.DataFrame(emoji_df_unique, columns=['emoji', 'unique'])

        #emoji_count.set_index('emoji')
        #emoji_unique.set_index('emoji')

        emoji_df = pd.merge(left=emoji_count, right=emoji_unique, on=['emoji'])

        emoji_df.sort("unique", ascending=False)

        #writes output file
        #possible rewrite this so it doesn't use pandas
        with open(file, 'w') as f:
            emoji_df.to_csv(f, sep=',', index = False, encoding='utf-8')
        return


    def clear(self):

        for emoji in self.dict.keys():
            self.dict[emoji] = 0
        return


    def __str__(self):
        return str(self.dict)

