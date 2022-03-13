#!/usr/bin/env python
import gc

import pandas as pd
import numpy as np
import glob
import os.path
import sys

def fillnabygroup(wagon_info):
    # change data type from 'string' in 'timedelta'
    wagon_info['timestamp_measure_position'] = pd.to_timedelta(wagon_info['timestamp_measure_position'])
    wagon_info['timestamp_measure_position'] = wagon_info['timestamp_measure_position'].fillna(method='ffill').dropna()
    wagon_info.sort_values("timestamp_measure_position", inplace=True)

    # fill vacant values and simplify the data
    wagon_info['movement_state'] = wagon_info['movement_state'].fillna(method='ffill').fillna('3')
    wagon_info['movement_state'] = wagon_info['movement_state'].astype(np.uint8)

    return(wagon_info.iloc[-1, :])

dtype={'wagon_ID': str,
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
       'provider': np.uint8}


data1 = pd.read_csv('../../data/211202_wagon_type_mapping_add.csv', dtype=dtype)

raw_data_path = '../../data/raw'

raw_files = glob.glob(os.path.join(raw_data_path, '*_TUDA_data.csv'))
print('Raw files: {}'.format(raw_files))

for i, file in enumerate(raw_files, start=1):
    print('{:2}/{:2} Reading file {}'.format(i, len(raw_files), file))
    data_init = pd.read_csv(file, dtype=dtype)
    print('Loading finished 1/4')

    data_init['movement_state'] = data_init['movement_state'].str.replace('parking', '0')
    data_init['movement_state'] = data_init['movement_state'].str.replace('standing', '1')
    data_init['movement_state'] = data_init['movement_state'].str.replace('moving', '2')
    print('movement_state DONE 2/4')

    data = pd.concat([data_init, data1])
    print('concat DONE 3/4')

    data1 = data.groupby('wagon_ID', as_index=False).apply(fillnabygroup)
    print('timestamp_index DONE 4/4')
    
    data1.to_csv('../../data/preprocessed/{:02}_data.csv'.format(i+1), mode='w', index=False)
    print('saved')

    print(data.info(verbose=False, memory_usage="deep"))
    del data
    del data_init
    gc.collect()
