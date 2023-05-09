def get_df_from_excel(name, skiprows, skipfooter, cols_rename, parse_dates=['Date']):
    df = pd.read_excel(f"{name}.xlsx", decimal=',', parse_dates=parse_dates, skiprows=skiprows, skipfooter=skipfooter)
    df = df[list(cols_rename.keys())]
    df.rename(columns=cols_rename, inplace=True)
    df = df.set_index('period')
    return df
