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

dtype_pre={'wagon_ID': np.uint,
       'loading_state': np.bool_,
       'loading_state_update': np.int32,
       'altitude': np.float16,
       'latitude': np.float32,
       'longitude': np.float32,
       'signal_quality_satellite': np.float32,
       'signal_quality_hdop': np.float32,
       'determination_position': np.uint8,
       'GNSS_velocity': np.float16,
       'timestamp_measure_position': np.int32,
       'timestamp_transfer': np.int32,
       'movement_state': np.uint8,
       'timestamp_measure_movement_state': np.int32,
       'timestamp_index': np.int32,
       'provider': np.uint8}

dtype_pre_battery={'wagon_ID': np.uint,
                   'provider': np.uint8,
                   'timestamp_measure_battery': np.int32,
                   'battery_state': np.float32,
                   'battery2_state': np.float32}


def load_raw_csv(index, columns=None):
    return pd.read_csv('./data/raw/{:02}_211203_TUDA_data.csv'.format(index), dtype=dtype_raw)

def load_pre_processed_csv(index, columns=None):
    return pd.read_csv('./data/preprocessed/data_{:2}.csv'.format(index), dtype=dtype_pre, usecols=columns)

def load_pre_processed_battery(index, columns=None):
    return pd.read_csv('./data/preprocessed/data_battery_state{:2}.csv'.format(index), dtype=dtype_pre_battery, usecols=columns)
