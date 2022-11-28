# QSSS
This is the repository for my QSSS senior thesis.

# parse_files.py
## Arguments:
- `--split_on_semicolon`: Split on semicolons in addition to the end punctuations if `t`, `true`, `y`, or `yes`. Defaults to `f`.
- `--strip_trailing_punctuation`: Strip certain trailing punctuations (!.?;:) if `t`, `true`, `y`, or `yes`. Defaults to `f`.
- `--data_dir`: Directory to the raw data files. Defaults to `./data`.
- `--output_dir`: Directory to the output files. Defaults to `./output`.
- `--output_names`: Naming method for the output files. If `original`, uses the same names as the raw data files. If `random`, uses a random sequence of 12 uppercase letters and digits. Defaults to `original`.
- `--output_format`: Header template of the output csv files, separated by `|`. Defaults to `sentence|tag1|tag2|tag3|section|notes`.
- `--sentence_column`: Column number to place the parsed sentences in the output csv files. Defaults to `1`.
## Sample command:
```
python3 parse_files.py --split_on_semicolon t --strip_trailing_punctuation t --data_dir ./data/raw --output_dir ./data/tag --output_names original --output_format 'sentence|tag1|tag2|tag3|section|notes' --sentence_column 1
```
## Known issues:
- Abbreviations not to split on (like 'etc.' 'vs.' 'i.e.') are currently hard-coded to
```
['eg', 'e\.g', 'ie', 'i\.e', 'et al', 'etc', 'ibid',
 'vs', 'v\.s', 'VS', 'V\.S', 'versus',
 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',
 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun',
 'Dr', 'Prof', 'Mr',  'Ms', 'Mrs', 'Miss',
 'US', 'U\.S', 'UK', 'U\.K', 'EU', 'E\.U']
```
- It gets input files in all subdirectories as well.

# Tagging/Coding:
(Just some random notes to myself. No need to understand.)
- Tagging or coding?
- Defining new variable = MethDef? DataDesc?
- Model selection method and metrics = MethJust? Res?
- "Our client wants us to..." = RQSig?
- Discard section titles?