import os
from pathlib import Path
from nltk import tokenize
import pandas as pd
from tqdm import tqdm

def parse_doc_all(data_dir, save_dir):
    path_list = Path(data_dir).rglob('*.txt')
    for file_path in tqdm(path_list):
        # read in text
        f = open(file_path, "r", encoding="utf8")
        file_text = f.read()
        f.close()
        # split text by sentences
        file_text = file_text.replace("\n", " ")
        sent = tokenize.sent_tokenize(file_text)
        # make dataframe of text and write into csv
        df = pd.DataFrame({'sentence': sent, 'tag1': None, 'tag2': None, 'section': None})
        file_name = os.path.split(file_path)[1][:-4]
        df.to_csv('{}\{}.csv'.format(save_dir, file_name), index=False, encoding='utf-8-sig') 

if __name__ == "__main__":
    current_dir = os.getcwd()
    data_dir = os.path.join(current_dir, 'data\\raw')
    save_dir = os.path.join(current_dir, 'data\\tag')
    parse_doc_all(data_dir, save_dir)
