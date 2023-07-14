import pandas as pd
import win32com.client as win32
from main import formula_generator


def change_baskets_for_client(name, items, total):
    dfmain = pd.read_excel('Master R&D.xlsx', sheet_name=None)
    df = dfmain['sheet1']
    dfhome = dfmain['home']
    column_indices_to_keep = [0, 1, 2, 3, 4, 5]
    dfhome = dfhome.iloc[:, column_indices_to_keep]
    # sheet1
    new_row_data = {}
    for column in df.columns:
        if column in items:
            new_row_data[column] = column
        else:
            new_row_data[column] = 'n'
    new_row_data['CLIENT NAME'] = name
    df = df.append(new_row_data, ignore_index=True)
    # new client
    columns_to_fill = [0, 2, 5]
    dfhome.iloc[:-1, columns_to_fill] = dfhome.iloc[:-1,
                                                    columns_to_fill].fillna(method='ffill')
    # print(dfhome)
    altered_dfhome = dfhome[dfhome['Strategy'].isin(items)]
    altered_dfhome = altered_dfhome.reset_index()
    allocated_total = int(total)
    altered_dfhome['Weightage'] = (
        altered_dfhome['Weightage']).round(0)
    altered_dfhome = altered_dfhome.drop('index', axis=1)
    new_row2 = pd.DataFrame(
        [['Total', None, None, None, allocated_total, None]], columns=altered_dfhome.columns)
    altered_dfhome = altered_dfhome.append(new_row2, ignore_index=True)
    altered_dfhome = formula_generator(altered_dfhome)
    # print(altered_dfhome)
    with pd.ExcelWriter("Master R&D.xlsx", mode="a", engine="openpyxl", if_sheet_exists='overlay') as writer:
        df.to_excel(writer, sheet_name="sheet1", index=False)
    with pd.ExcelWriter("Master R&D.xlsx", mode="a", engine="openpyxl", if_sheet_exists='replace') as writer:
        altered_dfhome.to_excel(writer, sheet_name=name, index=False)
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    workbook = excel.Workbooks.Open(
        "D:\AKSHAT\internship_clone\mastering\Master R&D.xlsx")
    workbook.Save()
    workbook.Close()
    excel.Quit()


# change_baskets_for_client(
#     'akshat', ['ETF', 'Buyback ', 'BNH based on Quant'], 500)

# change_baskets_for_client(
#     'keycap', ['ETF', 'Buyback '], 500)
