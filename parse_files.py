import os
from pathlib import Path
import re
import pandas as pd
from tqdm import tqdm

# Not to split on pattens of "these words followed by period"
SKIP_LIST = ['eg', 'e.g', 'ie', 'i.e', 'et al', 'etc', 'ibid',
             'vs', 'v.s', 'VS', 'V.S', 'versus',
             'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',
             'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun',
             'Dr', 'Prof', 'Mr',  'Ms', 'Mrs', 'Miss',
             'US', 'U.S', 'UK', 'U.K', 'EU', 'E.U']
SKIP_REGEX = ''.join(['(?<!{})'.format(s) for s in SKIP_LIST])
# Split on ! or . or ? or ; followed by a space
# the above patterns followed by " or ” or ) followed by a space
# or newline
SPLIT_REGEX = SKIP_REGEX + '[!.?;] |[!.?;]["”\)] |\n'
# Strip these trailing punctuations:
STRIP_PUNC = '!.?;:'

# Paths FROM THE CURRENT DIRECTORY to data and save locations
DATA_PATH = 'data\\raw'
SAVE_PATH = 'data\\tag'

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
        sent = re.split(SPLIT_REGEX, file_text)
        sent = list(map(strip_punc, sent))
        # make dataframe of text and write into csv
        df = pd.DataFrame({'sentence': sent, 'tag1': None, 'tag2': None, 'tag3': None, 'section': None, 'notes': None})
        file_name = os.path.split(file_path)[1][:-4]
        df.to_csv('{}\{}.csv'.format(save_dir, file_name), index=False, encoding='utf-8-sig') 

if __name__ == "__main__":
    current_dir = os.getcwd()
    data_dir = os.path.join(current_dir, DATA_PATH)
    save_dir = os.path.join(current_dir, SAVE_PATH)
    parse_doc_all(data_dir, save_dir)
