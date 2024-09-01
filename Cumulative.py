import numpy as np
import pandas as pd

# Sample data with missing values
data = {
    'A': [1, np.nan, 3, np.nan, 5, np.nan, 7],
    'B': [np.nan, 2, np.nan, 4, np.nan, 6, np.nan],
    'C': [7, np.nan, np.nan, 10, 11, np.nan, np.nan]
}

# Creating a DataFrame
df = pd.DataFrame(data)
def forward_fill(df):
    for col in df.columns:
        cumulative_mean = df[col].expanding().mean()
        df[col] = df[col].fillna(cumulative_mean)
forward_fill(df)        



# Backward fill with cumulative mean
def backward_fill(df):
    for col in df.columns:
         cumulative_mean = df[col][::-1].expanding().mean()[::-1]
         df[col] = df[col].fillna( cumulative_mean)

backward_fill(df)
print(df)
