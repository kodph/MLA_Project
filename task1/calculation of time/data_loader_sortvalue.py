from datetime import timedelta
import pandas as pd
import numpy as np

dtype_raw={'wagon_ID': str,
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

dtype_pre_battery={'wagon_ID': np.uint,
                   'provider': np.uint8,
                   'timestamp_measure_battery': np.int32,
                   'battery_state': np.float32,
                   'battery2_state': np.float32}

def load_raw_csv(index, columns=None):
    df1 = pd.read_csv('D:/data/raw/{:02}_211203_TUDA_data.csv'.format(index), dtype=dtype_raw, usecols=columns)
    df2 = pd.read_csv('D:/data/preprocessed/{:02}_data.csv'.format(index), dtype=dtype_raw, usecols=columns)
    print('Loading finished 1/4')

    df1['movement_state'] = df1['movement_state'].str.replace('parking', '0')
    df1['movement_state'] = df1['movement_state'].str.replace('standing', '1')
    df1['movement_state'] = df1['movement_state'].str.replace('moving', '2')
    print('movement_state DONE 2/4')

    df = pd.concat([df1,df2])
    print('concat DONE 3/4')

    df['timestamp_measure_position'] = pd.to_timedelta(df['timestamp_measure_position'])
    df['timestamp_measure_position'] = df['timestamp_measure_position'].fillna(method='ffill').dropna()
    df.sort_values(by=['wagon_ID', 'timestamp_measure_position'],inplace=True)

    df['movement_state'] = df['movement_state'].fillna(method='ffill').fillna('3')
    df['movement_state'] = df['movement_state'].astype(np.uint8)
    print('timestamp_index DONE 4/4')

    df = df[(df['provider'] != 0)]
    df = df[(df['timestamp_measure_position'] != timedelta(0))]
    del df1
    del df2
    return df

def load_pre_processed_battery(index, columns=None):
    return pd.read_csv('./data/preprocessed/data_battery_state{:2}.csv'.format(index), dtype=dtype_pre_battery, usecols=columns)
