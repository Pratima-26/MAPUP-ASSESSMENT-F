#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# %load python_task_2.py
import pandas as pd


def calculate_distance_matrix(df)->pd.DataFrame():
    """
    Calculate a distance matrix based on the dataframe, df.
     data=pd.read_csv('dataset-3.csv')
     data
    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Distance matrix
    """
    distance_matrix = data.pivot(index='id_start', columns='id_end', values='distance')
    distance_matrix
     

    return df


def unroll_distance_matrix(df)->pd.DataFrame():
    """
    data=pd.DataFrame(data,columns=['id_start','id_end','distance'])
    data
    Unroll a distance matrix to a DataFrame in the style of the initial dataset.
    unrolled_df=data.stack().reset_index()
    unrolled_df
    


    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Unrolled DataFrame containing columns 'id_start', 'id_end', and 'distance'.
    """
    unrolled_df.columns = ['id_start', 'id_end', 'distance']
    unrolled_df = unrolled_df[unrolled_df['id_start'] != unrolled_df['id_end']].reset_index(drop=True)
    unrolled_df


    return df


def find_ids_within_ten_percentage_threshold(df, reference_id)->pd.DataFrame():
    """
    Find all IDs whose average distance lies within 10% of the average distance of the reference ID.

    Args:
        df (pandas.DataFrame)
        reference_id (int)

    Returns:
        pandas.DataFrame: DataFrame with IDs whose average distance is within the specified percentage threshold
                          of the reference ID's average distance.
    "
    avg_distance_reference = data[data['id_start'] == reference_id]['distance'].mean()
    threshold = 0.1 * avg_distance_reference

    ids_within_threshold = data.groupby('id_start')['distance'].mean()
    ids_within_threshold = ids_within_threshold[ (avg_distance_reference - threshold <= ids_within_threshold) &
        (ids_within_threshold <= avg_distance_reference + threshold)].reset_index()

    return data


def calculate_toll_rate(df)->pd.DataFrame():
    """
    Calculate toll rates for each vehicle type based on the unrolled DataFrame.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
     data
        toll_rates = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }

    for vehicle_type, rate in toll_rates.items():
        data[vehicle_type] = data['distance'] * rate

    return df


def calculate_time_based_toll_rates(df)->pd.DataFrame():
    """
    Calculate time-based toll rates for different time intervals within a day.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Write your logic here

    return df


# In[ ]:




