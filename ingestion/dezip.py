#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File for pulling up TAQ gzip files
and extracting time,ticker,volume and
price data from it and saving to new csv
"""

import pandas as pd
import gzip
import os
tem_list = []
for filename in os.listdir('<Foldername>'):
    f = gzip.open('<Folder directory>' + filename, 'r')
    for i in f:
        s = f.readline().decode().split('|')
        if len(s) < 4:
            continue
        else:
            tem_list.append([s[0], s[2], s[4], s[5]])
tem_list = pd.DataFrame(tem_list)
tem_list.drop(tem_list.tail(2).index, inplace=True)
tem_list[0] = tem_list[0].astype(dtype=int)
tem_list = tem_list.sort_values(by=0)
tem_list.to_csv(filename + '.csv', header=False, index=False)
