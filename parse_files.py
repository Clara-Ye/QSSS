import os
from pathlib import Path
import argparse
import warnings

import re
import string
import pandas as pd
from tqdm import tqdm
import random


# Not to split on pattens of "these words followed by period"
SKIP_LIST = ['eg', 'e\.g', 'ie', 'i\.e', 'et al', 'etc', 'ibid',
             'vs', 'v\.s', 'VS', 'V\.S', 'versus',
             'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',
             'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun',
             'Dr', 'Prof', 'Mr',  'Ms', 'Mrs', 'Miss',
             'US', 'U\.S', 'UK', 'U\.K', 'EU', 'E\.U']
SKIP_REGEX = ''.join(['(?<!{})'.format(s) for s in SKIP_LIST])
# Split on ! or . or ? (or ;) followed by a space
# the above patterns followed by " or ” or ) followed by a space
# or newline
SPLIT_REGEX_SEMICOLON = SKIP_REGEX + '[!.?;] |[!.?;]["”\)] |\n'
SPLIT_REGEX_NO_SEMICOLON = SKIP_REGEX + '[!.?] |[!.?]["”\)] |\n'
# Strip these trailing punctuations:
STRIP_PUNC = '!.?;:'


parser = argparse.ArgumentParser()

parser.add_argument('--split_on_semicolon', type=str, default='f')
parser.add_argument('--strip_trailing_punctuation', type=str, default='f')
parser.add_argument('--data_dir', type=str, default='./data')
parser.add_argument('--output_dir', type=str, default='./output')
parser.add_argument('--output_names', type=str, default='original')
parser.add_argument('--output_format', type=str, default='sentence|tag1|tag2|tag3|section|notes')
parser.add_argument('--sentence_column', type=int, default=1)


def strip_punc(sent):
    return sent.strip(STRIP_PUNC)

def parse_doc_all(args):
    path_list = Path(args.data_dir).rglob('*.txt')

    for file_path in tqdm(path_list):
        # read in text
        f = open(file_path, 'r', encoding='utf8')
        file_text = f.read()
        f.close()

        # split text by sentences and clean up trailing punctuations
        if args.split_on_semicolon in ['t', 'true', 'y', 'yes']:
            sent = re.split(SPLIT_REGEX_SEMICOLON, file_text)
        else:
            sent = re.split(SPLIT_REGEX_NO_SEMICOLON, file_text)

        if args.strip_trailing_punctuation.lower() in ['t', 'true', 'y', 'yes']:
            sent = list(map(strip_punc, sent))

        # make dataframe of text and write into csv
        headers = args.output_format.split('|')
        df = pd.DataFrame(columns = headers)

        if 1 <= args.sentence_column <= len(headers):
            df[ headers[args.sentence_column-1] ] = sent
        else:
            df.iloc[:,0] = sent
            warnings.warn(
                f'Provided sentence column number not in acceptable range (1-{len(headers)}). Placing sentences in the first column.',
                stacklevel=2
                )
            
        if args.output_names == 'random':
            file_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
        else: # original or unaccepted
            file_name = os.path.split(file_path)[1][:-4]
            if args.output_names != 'original':
                warnings.warn(
                f'`{args.output_names}` is not a supported naming method. Using the original file names.',
                stacklevel=2
                )

        df.to_csv(f'{args.output_dir}\{file_name}.csv', index=False, encoding='utf-8-sig') 


if __name__ == '__main__':
    args = parser.parse_args()
    parse_doc_all(args)