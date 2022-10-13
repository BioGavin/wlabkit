#!/usr/bin/env python
import sys

import pandas as pd

from astool.antismash_utils import AntismashJsonParser
from astool.utils import get_json_dir_ls
from astool.query_antismash import AntismashJsonQueryer

if __name__ == '__main__':
    input = sys.argv[1]
    all_polymer = []
    for json_dir in get_json_dir_ls(input):
        try:
            json_file = AntismashJsonParser(json_dir)
            queryer = AntismashJsonQueryer(json_dir)
            all_polymer += json_file.get_modules_nrps_pks_region_polymer()
        except:
            print(json_dir)
    df = pd.DataFrame(all_polymer)
    df.to_csv('polymer.tsv', index=False, sep='\t')
