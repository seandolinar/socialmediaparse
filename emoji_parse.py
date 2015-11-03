__author__ = 'seandolinar'
#__version__ = '0.0.1' #adding more properties to the object
__version__ = '0.0.1' #adding in diversity methods



import os
import pandas as pd

class EmojiDict(object):

    def __init__(self):

        #loads the emoji table in the data folder in the package
        file_path = os.path.dirname(os.path.abspath(__file__))
        emoji_key = pd.read_csv(file_path + '/data/' + 'emoji_table.txt', encoding='utf-8', index_col=0)

        #loads the diversity table
        diversity_df = pd.read_csv(file_path + '/data/' + 'diversity_table.txt', encoding='utf-8', index_col=0)
        
        #intialize emoji count
        emoji_key['count'] = 0
        emoji_dict = emoji_key['count'].to_dict()
        emoji_dict_total = emoji_key['count'].to_dict()

        #initialize diversity analysis
        diversity_df['count'] = 0
        diversity_keys = diversity_df['count'].to_dict().keys()
        human_emoji = []

        for emoji in diversity_keys:

            emoji = emoji.replace(u'\U0001f3fb', '')
            emoji = emoji.replace(u'\U0001f3fc', '')
            emoji = emoji.replace(u'\U0001f3fd', '')
            emoji = emoji.replace(u'\U0001f3fe', '')
            emoji = emoji.replace(u'\U0001f3ff', '')

            human_emoji.append(emoji)

        human_emoji_unique = list(set(human_emoji))
        human_emoji_dict = {}

        for emoji in human_emoji_unique:

            human_emoji_dict[emoji] = 0

        #self define
        self.dict = emoji_dict
        self.dict_total = emoji_dict_total
        self.emoji_list = emoji_dict.keys()
        self.baskets = []
        self.total_emoji = 0
        self.total_indiv_emoji = 0

        self.skin_tones = ['\U0001f3fb', '\U0001f3fc', '\U0001f3fd', '\U0001f3fe', '\U0001f3ff']
        self.skin_tones_dict = {'human_emoji': 0, '\U0001f3fb':0, '\U0001f3fc':0, '\U0001f3fd': 0, '\U0001f3fe':0, '\U0001f3ff':0}
        self.human_emoji = human_emoji_unique
        self.human_emoji_dict = human_emoji_dict



    def add_emoji_count(self, text):

        #increments a count if an emoji as present
        emoji_basket = []

        for emoji in self.emoji_list:

            if emoji in text:
                self.dict[emoji] += 1
                emoji_basket.append(emoji)

            self.dict_total[emoji]  += text.count(emoji)
            self.total_indiv_emoji += text.count(emoji)

        human_emoji_count = 0
        for emoji in self.human_emoji:

            if emoji in text:

                human_emoji_count += 1
                self.skin_tones_dict['human_emoji'] += 1

                for tone in self.skin_tones:

                    if emoji.encode('unicode-escape')+tone in text.encode('unicode-escape'):

                        self.skin_tones_dict[tone] += 1



        if len(emoji_basket) > 0:
            self.total_emoji += 1


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


