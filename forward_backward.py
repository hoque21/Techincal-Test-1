import pandas  as pd
import numpy as np

data = {
    'A': [1, np.nan, 3, np.nan, 5],
    'B': [np.nan, 2, np.nan, 4, np.nan],
    'C': [7, np.nan, np.nan, 10, 11],
    'd': [6, 7, 8, 9, 10],
    'E': [5, np.nan, 6, np.nan, 7],
    'F': [12, np.nan, 13, 14, np.nan]
}


df = pd.DataFrame(data)

print(df)

df_forward = df.fillna(method = 'ffill')
print(df_forward)



df_backward = df.fillna(method = 'bfill')
print(df_backward)

