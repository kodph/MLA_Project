import pandas as pd
from datetime import timedelta

df = pd.read_csv("D:/data/211202_wagon_type_mapping.csv", usecols = ['wagon_ID','provider'])

df['loading_state'] = 'Leer'
df['loading_state_update'] = timedelta(seconds=0)
df['altitude'] = 0
df['latitude'] = 0
df['longitude'] = 0
df['signal_quality_satellite'] = 0
df['signal_quality_hdop'] = 0
df['determination_position'] = 0
df['GNSS_velocity'] = 0
df['timestamp_measure_position'] = timedelta(seconds=0)
df['timestamp_transfer'] = timedelta(seconds=0)
df['movement_state'] = 3
df['timestamp_measure_movement_state'] = timedelta(seconds=0)
df['timestamp_index'] = timedelta(seconds=0)
df = df[(df['provider'] != 0)]
df['provider'] = 0

df.to_csv("D:/data/preprocessed/01_data.csv", index = False)