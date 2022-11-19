import os
from pathlib import Path
import re
import pandas as pd
from tqdm import tqdm

SPLIT_PUNC = '[!.?;] |\n|\.["”\)] '
STRIP_PUNC = '!.?;:'

def strip_punc(sent):
    return sent.strip(STRIP_PUNC)

def parse_doc_all(data_dir, save_dir):
    path_list = Path(data_dir).rglob('*.txt')
    for file_path in tqdm(path_list):
        # read in text
        f = open(file_path, "r", encoding="utf8")
        file_text = f.read()
        f.close()
        # split text by sentences and clean up trailing punctuations
        sent = re.split(SPLIT_PUNC, file_text)
        sent = list(map(strip_punc, sent))
        # make dataframe of text and write into csv
        df = pd.DataFrame({'sentence': sent, 'tag1': None, 'tag2': None, 'tag3': None, 'section': None, 'notes': None})
        file_name = os.path.split(file_path)[1][:-4]
        df.to_csv('{}\{}.csv'.format(save_dir, file_name), index=False, encoding='utf-8-sig') 

if __name__ == "__main__":
    current_dir = os.getcwd()
    data_dir = os.path.join(current_dir, 'data\\raw\\extra')
    save_dir = os.path.join(current_dir, 'data\\tag')
    parse_doc_all(data_dir, save_dir)
