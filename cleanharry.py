
#
# Usage: 
# $ python3 clean.py data/test.csv results/test-clean.csv
#


import argparse
import json
import logging
from pathlib import Path
import pandas as pd
import numpy as np

harry_df = pd.read_csv('/Users/natalyanaser/desktop/hpcleanvlarge1.csv')
# Clean data in Harry Potter Fanfic Dataset
    # Remove unneeded column ('Updated' 'story_link')
logging.info('Removing unneeded columns.')
harry_df.drop(['Updated', 'story_link'], axis=1, inplace=True)

    # Remove column values that are empty in 'pairing' and 'Follows'.
logging.info('Removing records with empty pairing or Follows.')
harry_df.dropna(subset=['pairing'], inplace=True)
harry_df.dropna(subset=['Follows'], inplace=True)

# Split the "published_mmyy" column into separate "Month" and "Year" columns
logging.info('Create distinct Month and Year columns from single mmyy column')
harry_df[['Month Published', 'Year Published']] = harry_df['published_mmyy'].str.split('-', expand=True)

# Drop the original "published_mmyy" column
logging.info('Removing original mmyy column')
harry_df = harry_df.drop('published_mmyy', axis=1)

# Filter out all categories other than "English" in the "Language" column
logging.info('Removing non English stories from dataset')
harry_df = harry_df.drop(harry_df[~(harry_df['language'] == 'English')].index)

# Save the modified dataframe to a clean CSV file
harry_df.to_csv('cleaned_data.csv', index=False)
