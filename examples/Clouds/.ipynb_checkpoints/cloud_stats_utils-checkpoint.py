from datetime import datetime
import pandas as pd


def generate_cloud_stats_table(clean_percent, dates, mode = "median"):
    
    
    df = pd.DataFrame(dict(dates= dates, values = clean_percent))
    df['dates'] = pd.to_datetime(df['dates'])
    df['year'] = df['dates'].dt.year
    df['month'] = df['dates'].apply(lambda x: x.strftime('%B'))
    df = df[['month','year','values']]
    
    if mode == "median":
        df_grouped = df.groupby(['year', 'month']).median().reset_index()
    elif mode == "mean":
        df_grouped = df.groupby(['year', 'month']).mean().reset_index()
    else:
        raise f"No mode called '{mode}'"
    
    pivoted = df_grouped.pivot("month", "year", "values")
    return pivoted

