import pandas as pd
import numpy as np
import os

def extract(data_dir, prefix, start_week, end_week):
    """ Extract a temporal slice of data for a given data source.
    
    Parameters
    ----------
    data_dir: str
        Data directory path.
    start_week: int
        First week number (included)
    end_week: int
        Last week number (included)
    prefix: str
        Data source identification (e.g. restaurant_1)
    """
    df = pd.DataFrame()
    
    for i in range(start_week, end_week+1):
        file_path = os.path.join(data_dir, f'{prefix}_week_{i}.csv')

        if os.path.isfile(file_path):
            batch = pd.read_csv(file_path)
            df = pd.concat([df, batch], sort=True)
    
    return df

def clean(df):
    """Clean dataframe."""
    
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    df['order_date'] = pd.to_datetime(df['order_date'])
    df = df.rename(columns={'order_number': 'order_id'})
    df = df.sort_values('order_date')
    df['total_product_price'] = df['quantity'] * df['product_price']
    df['cash_in'] = df.groupby('order_id')['total_product_price'].transform(np.sum)
    df = df.drop(columns=['item_name', 'quantity', 'product_price', 
                          'total_products', 'total_product_price'],
                errors="ignore")
    df = df.drop_duplicates()
    df = df.reset_index(drop=True)
    return df

df = extract(data_dir= "C:/Users/277775/MLops/data/",
       prefix="restaurant_1" , start_week=108, end_week=110)

input()
print(df.head())