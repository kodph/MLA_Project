#!/usr/bin/env python
import gc
import pandas as pd
import numpy as np
import glob
import os.path
import sys


dtype_pre_battery={'wagon_ID': np.uint,
                   'provider': np.uint8,
                   'timestamp_measure_battery': np.int32,
                   'battery_state': np.float32,
                   'battery2_state': np.float32}

df_list = []


def time_to_sec(string):
    if string == 'NaT':
        return np.NaN
    date = string.split(' ')
    # print(string)
    time = date[2].split(':')
    return int(int(date[0])*24*60*60 + int(time[0])*60*60 + int(time[1])*60 + int(time[2].split('.')[0]))


raw_data_path = './data/raw'

raw_files = glob.glob(os.path.join(raw_data_path, '*battery_state.csv'))
print('Raw files: {}'.format(raw_files))
for i, file in enumerate(raw_files):
    print('{:2}/{:2} Reading file {}'.format(i+1, len(raw_files), file))
    data = pd.read_csv(file, dtype={'wagon_ID': str,
                                    'provider': np.uint8,
                                    'timestamp_measure_battery': str,
                                    'battery_state': str,
                                    'battery2_state': str})
    print('Loading finished')
    data['wagon_ID'] = data['wagon_ID'].str.replace("'", '').astype(np.uint)

    data['timestamp_measure_battery'] = \
        data['timestamp_measure_battery'].apply(time_to_sec).fillna(0).astype(np.int32)
    print('timestamp_measure_battery DONE')
    
    data['battery_state'] = data['battery_state'].str.replace('%', '')
    data['battery_state'] = data['battery_state'].str.replace(' ', '')
    data['battery_state'] = data['battery_state'].astype(np.float32)
    
    data['battery2_state'] = data['battery2_state'].str.replace('%', '')
    data['battery2_state'] = data['battery2_state'].str.replace(' ', '')
    data['battery2_state'] = data['battery2_state'].astype(np.float32)
    
    df_list.append(data)
    
    print('Saving')
    data.to_csv('./data/preprocessed/data_battery_state{:2}.csv'.format(i), mode='w')
    print(data.info(verbose=False, memory_usage="deep"))

pd.concat(df_list, ignore_index=True).to_csv('./data/preprocessed/data_battery_state', mode='w')