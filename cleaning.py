#this file is for the cleaning of the dataframes from the streaming platforms
def set_index(df, column):
    """
    This will change the value of the column to lowercase
    """
    return df.set_index(column)


def drop(df, *args, axis):
    return df.drop(*args, axis=1)


def reindex(df, column):
    return df.reindex(columns = [column])


def inner_merge(new_df, df1, df2, type, column):
    """This whill merge two databases 
        new_df is name of the created dataframe,
        df1 this is the main dataframe,
        df2 second dataframe,
        type = joining method,
        Column = name of the column they will join on """
    import pandas as pd
    new_df = pd.inner_merge(df1, df2, how=type, on=[column])
    return new_df