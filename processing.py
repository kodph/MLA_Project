import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import dask
import dask.dataframe as dd


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

data = pd.read_csv('./data/raw/01_211203_TUDA_data.csv', dtype=dtype)

fig, axs = plt.subplots(1, 1, squeeze=False)
axs[0][0].scatter(data.longitude, data.latitude)

fig.show()
