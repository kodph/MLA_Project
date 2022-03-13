# MLA Project
##Datastructure
### Longterm Data:
| Index | Field                            | Meaning                                                                                                                  | Values                      | Size   |
|-------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------|-----------------------------|--------|
| 0     | wagon_ID Number                  | Unique ID of the wagon                                                                                                   | Number                      | 4 byte |
| 1     | loading_state                    | Loading state                                                                                                            | String (Beladen/Leer)       | 1 byte |
| 2     | loading_state_update             | Last time the loadingstate was updated                                                                                   | String (x days XX:XX:XX)    | 4 byte |
| 3     | altitude                         | Altitude                                                                                                                 | Float                       | 4 byte |
| 4     | latitude                         | Latitude                                                                                                                 | Float                       | 4 byte |
| 5     | longitude                        | Longitude                                                                                                                | Float                       | 4 byte |
| 6     | signal_quality_satellite         | Number of connected GNSS Sats.                                                                                           | Byte                        | 1 byte |12.0
| 7     | signal_quality_hdop              | "Horizontal Diluition of Precision" of the measurement with lower values indicating more accurate position determination | Float                       | 4 byte |1.2
| 8     | determination_position           | way of the position determination 1 = GNSS 4 = cellular                                                                  | Byte                        | 1 byte | 1
| 9     | GNSS_velocity                    | GNSS velocity of the train in km/h                                                                                       | Float                       | 2 byte |0.0
| 10    | timestamp_measure_position       | timestamp from when the actual measurement was conducted                                                                 | String (x days XX:XX:XX.YY) | 4 byte |8 days 03:43:56.615000
| 11    | timestamp_transfer               | timestamp from when the data logger tries to transfer message with the meaesured data                                    | String (x days XX:XX:XX.YY) | 4 byte |10 days 07:31:37.282000
| 12    | movement_state                   | Movement state moving/standing/parking  (3. unknown)                                                                     | String                      | 1 byte |parking/standing/moving
| 13    | timestamp_measure_movement_state | timestamp of the last movement state change                                                                              | String (x days XX:XX:XX.YY) | 4 byte |8 days 03:43:56.615000
| 14    | timestamp_index                  | timestamp from when the data was received, processed and made available in the DB Cargo IT system                        | String (x days XX:XX:XX)    | 4 byte |
| 15    | provider                         | provider of the telematic module that is conducting the measurement                                                      | Int                         | 1 byte |

-> 47 byte per entry 

### Data adjusting
Timestemps are converted to seconds for easy storage and processing \
String states are converted to numbers

## Data processing
Using Dask to load huge Data only when needed into RAM
