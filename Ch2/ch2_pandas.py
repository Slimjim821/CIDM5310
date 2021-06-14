import datetime as dt
import numpy as np
import pandas as pd

# create a dataframe from a list/dictionary

my_dataframe = pd.DataFrame(
    [
        {'mag': 5.2, 'place': 'California'},
        {'mag': 1.2, 'place': 'Alaska'},
        {'mag': 50.5, 'place': 'California'},
    ]
)

# print(my_dataframe)

quakes_df = pd.read_csv('data/earthquakes.csv')

print(quakes_df)
