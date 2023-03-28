
# cleaning scripts applied to dataset. all changes made will be saved to new cleaned_data.csv

#import packages needed

import argparse
import json
import logging
from pathlib import Path
import pandas as pd
import numpy as np

# Clean data in Harry Potter Fanfic Dataset
harry_df = pd.read_csv('/Users/natalyanaser/desktop/hpcleanvlarge1.csv')

    #1 Remove unwanteds columns ('Updated' 'story_link')
logging.info('Removing unneeded columns.')
harry_df.drop(['Updated', 'story_link'], axis=1, inplace=True)

    #2 Remove column values that are empty in the following columns.
logging.info('Removing records with empties.')
harry_df.dropna(subset=['pairing'], inplace=True)
harry_df.dropna(subset=['Follows'], inplace=True)
harry_df.dropna(subset=['Reviews'], inplace=True)
harry_df.dropna(subset=['Favs'], inplace=True)
harry_df.dropna(subset=['Words'], inplace=True)


#3 Split the "published_mmyy" column into separate "Month" and "Year" columns
logging.info('Create distinct Month and Year columns from single mmyy column')
harry_df[['Month Published', 'Year Published']] = harry_df['published_mmyy'].str.split('-', expand=True)

#4 Delete the original "published_mmyy" column
logging.info('Removing original mmyy column')
harry_df = harry_df.drop('published_mmyy', axis=1)


#5 Filter out all language categories other than "English" in the "Language" column
logging.info('Removing non English stories from dataset')
harry_df = harry_df.drop(harry_df[~(harry_df['language'] == 'English')].index)

#6 Delete the original "language" column since it no longer serves a purpose since they're all english
logging.info('Removing original language column')
harry_df = harry_df.drop('language', axis=1)

#7 Convert month numbers to names
def convert_month(month_num):
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month_num = int(month_num)
    return month_names[month_num-1] # Subtract 1 to get the correct month

#8 Convert the month numbers in 'Month Published' column to month names
harry_df['Month Published'] = harry_df['Month Published'].apply(convert_month)

#9 Sort and concatenate names in each pairing so duplicates of inverse can be removed
#original categires showed 'harry, ron' and 'ron, harry' as two separte values!
def sort_pairings(pairing):
    names = pairing.split(',')
    names.sort()
    return ', '.join(names)

# Applies the above to the 'pairing' column to create a new 'pairing sorted' column and this sorts it in alphabetical to get rid of inverses as different values problem
harry_df['pairing sorted'] = harry_df['pairing'].apply(lambda x: ', '.join(sorted(x.split(', '))))

#9 Save the modified dataframe to a clean CSV file
harry_df.to_csv('cleaned_data.csv', index=False)
