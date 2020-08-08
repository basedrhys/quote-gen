import gpt_2_simple as gpt2
import pandas as pd
from tqdm import tqdm
import os

input_data_file = './data/2-quotes_filtered.csv'
output_folder = "output/"

split_quotes = pd.read_csv(input_data_file)
print(split_quotes.head())

## These were the top 20 most common topics in the dataset
topics_to_keep = ['life', 'love','inspirational', 'humor', 
                  'death', 'art', 'education', 'books', 'change', 'time', 
                  'beauty', 'god', 'happiness', 'children', 'work', 'faith', 
                  'funny', 'good', 'family', 'friendship']

quotes_to_keep = split_quotes[split_quotes['topic'].isin(topics_to_keep)]

## Create the GPT-ready dataset
file_name = os.path.join(output_folder, "processed_quotes.txt")
with open(file_name, mode='w') as open_file:
  for index, row in split_quotes.iterrows():
    open_file.write("_TOPIC_ {} _QUOTE_ {} _AUTHOR_ {} _END_\n".format(row['topic'], row['quote'], row['author']))

## Encode it to make loading faster during training
gpt2.encode_dataset(file_name, out_path=os.path.join(output_folder,'text_encoded.npz'))