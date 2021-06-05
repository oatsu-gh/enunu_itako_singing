#!/usr/bin/env python3
# Copyright (c) 2021 oatsu
"""
htsのフルラベルをUSTに一括変換する
"""
from glob import glob

from tqdm import tqdm
from utaupy.utils import hts2ust


def main():
    full_label_files = glob('in/*.lab')
    path_table = 'kana2phonemes_utf8_for_oto2lab_noAIUEO.table'
    for path_full in tqdm(full_label_files):
        path_ust = path_full.replace('.lab', '.ust')
        hts2ust(path_full, path_ust, path_table)


if __name__ == '__main__':
    main()
