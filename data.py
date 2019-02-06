import pandas as pd
import numpy as np
import random 
import string

def make_data(start_date='2019-01-01',n_data=30,n_num_var=5,n_cat_var=5,n_cat_var_cardinality_upper=10):
    ''' Function to make some data and put it in a df
    '''
    dates = pd.date_range(start_date,periods=n_data)
    df = pd.DataFrame()
    df['date'] = dates
    df = df.set_index(dates)
    for n in range(n_num_var):
        df[f'num_var_{n}'] = np.random.randn(n_data)
    for n in range(n_cat_var):
        cat_vars_generated = np.unique([''.join(random.choices(string.ascii_uppercase + string.digits, k=np.random.randint(2,8))) for i in range(10000)])
        cat_vars_possible = np.random.choice(cat_vars_generated,np.random.randint(1,n_cat_var_cardinality_upper))
        df[f'cat_var_{n}'] = np.random.choice(cat_vars_possible,n_data)
    return df