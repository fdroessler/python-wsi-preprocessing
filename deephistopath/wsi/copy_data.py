from tqdm import tqdm
from pathlib import Path
import pandas as pd
import shutil

df = pd.read_csv('test_addition.csv', index_col=0)

df['mapping'] = df['mapping'].apply(lambda x: str(x).zfill(4))
base = Path('/data2/tif/')

for idx, row in tqdm(df.iterrows()):
    filen = base / row['filename']
    if filen.exists():
        target = base / 'training_data_addition' / f"{row['mapping']}.tif"
        shutil.move(filen, target)