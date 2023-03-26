
#
# Usage: 
# $ python3 clean.py data/test.csv results/test-clean.csv
#
# where:
#   data/test.csv              = path to the input file
#   results/test-clean.csv     = path to the output file
#
# test input file provided: data/test.csv





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
harry_df[['Month Published', 'Year Published']] = harry_df['published_mmyy'].str.split('-', expand=True)

# Drop the original "published_mmyy" column
harry_df = harry_df.drop('published_mmyy', axis=1)

# Save the modified dataframe to a clean CSV file
harry_df.to_csv('cleaned_data.csv', index=False)


import csv
from itertools import islice

# Open the original CSV file
with open('/Users/natalyanaser/desktop/hpcleanvlarge1.csv') as csvfile:

    # Create a CSV reader object
    reader = csv.reader(harry_df)

    # Extract the first 100 rows using islice
    test_rows = list(islice(reader, 100))
    
# Write the test rows to a new CSV file
with open('test_dataset.csv', 'w', newline='') as csvfile:

   # Create a CSV writer object
    writer = csv.writer(csvfile)

    # Write the test rows to the new CSV file
    for row in test_rows:
        writer.writerow(row)
   
   
   