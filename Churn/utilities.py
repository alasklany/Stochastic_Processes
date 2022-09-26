import numpy as np

class Utilities:
    def cat_to_binary(df, varname):
        df[varname + '_num'] = df[varname].apply(lambda x: 1 if x == 'yes' else 0)
        #print("checking")
        #print(df.groupby([varname + '_num', varname]).size())
        return df

    def create_cpm(df,charge_vars,minutes_vars):
        df['total_charges'] = 0
        df['total_minutes'] = 0
        for indexer in range(0, len(charge_vars)):
            df['total_charges'] += df[charge_vars[indexer]]
            df['total_minutes'] += df[minutes_vars[indexer]]
        df['charge_per_minute'] = np.where(df['total_minutes'] > 0, df['total_charges'] / df['total_minutes'], 0)
        df.drop(['total_minutes', 'total_charges'], axis=1, inplace=True)
        print(df['charge_per_minute'].describe())
        return df
