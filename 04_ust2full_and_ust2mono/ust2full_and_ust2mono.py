#!/usr/bin/env python3
# Copyright (c) 2021 oatsu
"""
htsのフルラベルをUSTに一括変換する
"""
from glob import glob

from tqdm import tqdm
from utaupy.utils import ust2hts
from os.path import basename, join


def main():
    ust_files = glob('in_ust/*.ust')
    path_table = 'kana2phonemes_utf8_for_oto2lab_noAIUEO.table'
    for path_ust in tqdm(ust_files):
        path_full = join('out_full', basename(path_ust.replace('.ust', '.lab')))
        path_mono = join('out_mono', basename(path_ust.replace('.ust', '.lab')))
        ust2hts(path_ust, path_full, path_table, strict_sinsy_style=False)
        ust2hts(path_ust, path_mono, path_table, as_mono=True)


if __name__ == '__main__':
    main()
    input('press enter to exit')
