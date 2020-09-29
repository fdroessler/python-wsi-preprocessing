import pandas as pd
from sklearn.model_selection import train_test_split
import shutil

def get_label(row):
    for c in df_label.columns:
        if row[c]==1:
            return c

df_meta = pd.read_csv('train_metadata_eRORy1H.csv')
df_meta = df_meta.loc[:, df_meta.columns[~df_meta.columns.str.endswith('url')]]

df_label = pd.read_csv('train_labels.csv')
df_label['class'] = df_label.apply(get_label, axis=1)

df = pd.merge(df_meta, df_label, on='filename')

train, test = train_test_split(df['class'], test_size=0.1, random_state=42)

train_df = df.loc[train.index]
train_df['mapping'] = [str(x).zfill(4) for x in range(len(train_df))]
test_df = df.loc[test.index]
test_df['mapping'] = [str(x).zfill(4) for x in range(len(test_df))]

df.to_csv('full.csv')
train_df.to_csv('train.csv')
test_df.to_csv('test.csv')