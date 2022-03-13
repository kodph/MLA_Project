#!/usr/bin/env python
import gc

import pandas as pd
import numpy as np
import glob
import os.path
import sys


def time_to_sec(string):
    if string == 'NaT':
        return np.NaN
    date = string.split(' ')
    # print(string)
    time = date[2].split(':')
    return int(int(date[0])*24*60*60 + int(time[0])*60*60 + int(time[1])*60 + int(time[2].split('.')[0]))


raw_data_path = './data/raw'

raw_files = glob.glob(os.path.join(raw_data_path, '*data.csv'))
print('Raw files: {}'.format(raw_files))
for i, file in enumerate(raw_files):
    print('{:2}/{:2} Reading file {}'.format(i, len(raw_files)-1, file))
    data = pd.read_csv(file, dtype={'wagon_ID': str,
                                    'loading_state': str,
                                    'loading_state_update': str,
                                    'altitude': np.float16,
                                    'latitude': np.float32,
                                    'longitude': np.float32,
                                    'signal_quality_satellite': np.float32,
                                    'signal_quality_hdop': np.float32,
                                    'determination_position': np.uint8,
                                    'GNSS_velocity': np.float16,
                                    'timestamp_measure_position': str,
                                    'timestamp_transfer': str,
                                    'movement_state': str,
                                    'timestamp_measure_movement_state': str,
                                    'timestamp_index': str,
                                    'provider': np.uint8})
    data['wagon_ID'] = data['wagon_ID'].str.replace("'", '').astype(np.uint)
    print('Loading finished')
    data['loading_state'] = data['loading_state'].replace('Beladen', True)
    data['loading_state'] = data['loading_state'].replace('Leer', False)
    data['loading_state'] = data['loading_state'].astype(np.bool_)
    print('loading_state DONE 1/8')
    data['loading_state_update'] = data['loading_state_update'].apply(time_to_sec).astype(np.int32)
    print('loading_state_update DONE 2/8')
    data['timestamp_measure_position'] = data['timestamp_measure_position'].apply(time_to_sec).astype(np.int32)
    print('timestamp_measure_position DONE 3/8')
    data['timestamp_transfer'] = data['timestamp_transfer'].apply(time_to_sec).astype(np.int32)
    print('timestamp_transfer DONE 4/8')

    data['signal_quality_satellite'] = data['signal_quality_satellite'].fillna(0).astype(np.uint8)
    print('signal_quality_satellite DONE 5/8')
    data['movement_state'] = data['movement_state'].str.replace('parking', '0')
    data['movement_state'] = data['movement_state'].str.replace('standing', '1')
    data['movement_state'] = data['movement_state'].str.replace('moving', '2')
    data['movement_state'] = data['movement_state'].fillna('3')
    data['movement_state'] = data['movement_state'].astype(np.uint8)
    print('movement_state DONE 6/8')

    data['timestamp_measure_movement_state'] = \
        data['timestamp_measure_movement_state'].apply(time_to_sec).fillna(0).astype(np.int32)
    print('timestamp_measure_movement_state DONE 7/8')
    data['timestamp_index'] = data['timestamp_index'].apply(time_to_sec).fillna(0).astype(np.int32)
    print('timestamp_index DONE 8/8')
    print('Saving')
    data.to_csv('./data/preprocessed/data_{:2}.csv'.format(i), mode='w')
    data.to_hdf('data.hdf5', '/raw/data/{}'.format(i))
    print(data.info(verbose=False, memory_usage="deep"))
    del data
    gc.collect()
