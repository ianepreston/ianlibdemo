"""Do something with pandas just to see if we can"""
import pandas as pd

def give_me_a_df():
    """Return a dataframe"""
    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)
    return df