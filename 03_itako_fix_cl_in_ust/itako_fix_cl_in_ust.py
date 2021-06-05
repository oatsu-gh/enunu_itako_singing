#!/usr/bin/env python3
# Copyright (c) 2021 oatsu
"""
about module
"""
import utaupy
from os.path import basename
from glob import glob
from tqdm import tqdm
def fix_cl(path_ust):
    ust = utaupy.ust.load(path_ust)
    for note in ust.notes:
        lyric = note.lyric
        if ' cl' in lyric:
            note.lyric = 'っ'
    ust.write(path_ust)

def main():
    ust_files = glob('ust/*.ust')
    for path_ust in tqdm(ust_files):
        fix_cl(path_ust)


if __name__ == '__main__':
    main()
    
