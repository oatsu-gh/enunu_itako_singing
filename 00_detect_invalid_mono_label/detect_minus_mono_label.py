#!/usr/bin/env python3
# Copyright (c) 2021 oatsu
"""
指定されたフォルダにあるモノラベルに負の発声時間がないか調べる
"""

import utaupy
from os.path import basename
from glob import glob

def main():
    label_dir = input('label_dir: ').strip('"')
    lab_files = glob(f'{label_dir}/*.lab')
    for path_lab in lab_files:
        print('\n----------------------------------------')
        print(basename(path_lab))
        label = utaupy.label.load(path_lab)
        label.check_invalid_time()

if __name__ == '__main__':
    main()
