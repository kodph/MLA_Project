#!/usr/bin/env python
# coding: utf-8
import pandas as pd

import numpy as np

from datetime import timedelta

def time_moving(wagon_info):

    # change data type from 'string' in 'timedelta'
    wagon_info['timestamp_measure_position'] = pd.to_timedelta(wagon_info['timestamp_measure_position'])
    wagon_info['timestamp_measure_position'] = wagon_info['timestamp_measure_position'].fillna(method='ffill').dropna()
    wagon_info.sort_values("timestamp_measure_position", inplace=True)

    # fill vacant values and simplify the data
    #wagon_info['movement_state'] = wagon_info['movement_state'].str.replace('parking', '0')
    #wagon_info['movement_state'] = wagon_info['movement_state'].str.replace('standing', '1')
    #wagon_info['movement_state'] = wagon_info['movement_state'].str.replace('moving', '2')
    #wagon_info['movement_state'] = wagon_info['movement_state'].fillna(method='ffill').fillna('3')
    #wagon_info['movement_state'] = wagon_info['movement_state'].astype(np.uint8)

    # calculate the difference between two nearby rows, this difference is 'timedelta'
    wagon_info['timedelta'] = wagon_info['timestamp_measure_position'].shift(periods=-1) - wagon_info['timestamp_measure_position']
    # if the difference between two nearby rows are too huge, more than two days. we can consider that the wagon is not tested.
    # The time in this period will be deleted.
    wagon_info = wagon_info.drop(wagon_info[wagon_info['timedelta'] > timedelta(days=2)].index)
    Time_total = timedelta(0)
    Time_start = timedelta(0)
    Time_moving = timedelta(0)

    # If a set of data is full of null values, the next code will not be executed.
    if len(wagon_info) != 0:
        # The difference between the last value and the first value of each set of data is 'Time_total'.
        Time_total = wagon_info['timestamp_measure_position'].iloc[-1] - wagon_info['timestamp_measure_position'].iloc[0]
        # The first value of each set of data is 'Time_delta'.
        Time_start = wagon_info['timestamp_measure_position'].iloc[0]
        # When 'movement_state' is 2, wagon is moving. Select the eligible rows and sum.
        Time_moving_col = wagon_info[wagon_info['movement_state'] == 2]
        Time_moving = Time_moving_col['timedelta'].sum()

    # return list
    Time= [Time_moving, Time_total, Time_start]

    return Time
