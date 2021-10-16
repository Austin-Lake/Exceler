import pandas as pd
import glob
import os
from openpyxl import load_workbook
import xlsxwriter
from shutil import copyfile


def SplitFile(file_path, colpick, option):
    file = file_path
    extension = os.path.splitext(file)[1]
    filename = os.path.splitext(file)[0]
    pth = os.path.dirname(file)
    newfile = os.path.join(pth,filename+'_2'+extension)
    df = pd.read_excel(file)
    colpick = colpick
    cols = list(set(df[colpick].values))

    def SendToFile():
        for i in cols:
            df[df[colpick] == i].to_excel("{}/{}.xlsx".format(pth, i), sheet_name=i, index=False)
 
        return

    def SendToSheet():
        copyfile(file, newfile)
        for j in cols:
            writer = pd.ExcelWriter(newfile, engine='openpyxl')
            for myname in cols:
                mydf = df.loc[df[colpick] == myname]
                mydf.to_excel(writer, sheet_name=myname, index=False)
            writer.save()

            return
    
    if (option == "1"):
        SendToFile()
    
    elif (option == "2"):
        SendToSheet() 