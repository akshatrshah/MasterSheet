import pandas as pd
import win32com.client as win32
from main import formula_generator
import os


def change_weightage(client_name, values):
    dfmain = pd.read_excel('Master R&D.xlsx', sheet_name=None)
    df = dfmain[client_name]
    df['Weightage'] = df['Strategy'].replace(values)

    dfmain = pd.read_excel('Master R&D.xlsx', sheet_name=None)
    df = formula_generator(df)
    with pd.ExcelWriter("Master R&D.xlsx", mode="a", engine="openpyxl", if_sheet_exists='overlay') as writer:
        df.to_excel(writer, sheet_name=client_name, index=False)
    current_dir = os.getcwd()

# Construct the full file path for the Excel workbook
    file_path = os.path.join(current_dir, "Master R&D.xlsx")

    # Initialize Excel application
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    workbook = excel.Workbooks.Open(file_path)
    workbook.Save()
    workbook.Close()
    excel.Quit()


# change_weightage(client_name='axt', values={
#                  'Result Conviction ': 11, 'BNH based on Upsdie': 12})
