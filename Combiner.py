import glob
import os
import pandas as pd

def CombineFiles(folder_path):
    folder = folder_path
    pth=os.path.dirname(folder)
    extension = os.path.splitext(folder)[1]
    files = glob.glob(os.path.join(pth, '*.xls*'))
    newfile=os.path.join(pth,'combined.xlsx')
    df = pd.DataFrame()
    for f in files:
        data = pd.read_excel(f)
        df = df.append(data)

    df.to_excel(newfile, sheet_name='combined', index=False)
    print('Completed')


