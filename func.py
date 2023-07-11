import pandas as pd
import numpy as np
import win32com.client as win32
import warnings

warnings.filterwarnings("ignore")

# myfunc works to find all the empty slots in the all clients in the corresponding baskets


def myfunc(update_clients, basket_name, stock_name):
    print("Basket Name: "+basket_name.upper() + " allocation available: ")
    for i in update_clients:
        dfmain = pd.read_excel('Master R&D.xlsx', sheet_name=None)
        df = dfmain[i]
        # print(df)
        column_indices_to_keep = [0, 1, 2, 3, 4, 5]
        df = df.iloc[:, column_indices_to_keep]
        columns_with_merged_cells = [0, 1, 2, 5]
        df.iloc[:, columns_with_merged_cells] = df.iloc[:,
                                                        columns_with_merged_cells].fillna(method='ffill')
        column_name = 'Strategy'
        value_to_find = basket_name
        mask = df[column_name] == value_to_find
        filtered_rows = df[mask][df[mask].isnull().any(axis=1)]
        content = filtered_rows['Allocated'].to_list()
        content = [round(num, 2) for num in content]
        content = [str(num)
                   for num in content if pd.notnull(num)]  # Remove NaN values
        content = ' '.join(content)
        if content:
            print('Client Name: '+i.capitalize() + "  " + content)

# myfunc2 called when you want to put the stock name in please of nan values


def myfunc2(update_clients, basket_name, stock_name):
    for i in update_clients:
        dfmain = pd.read_excel('Master R&D.xlsx', sheet_name=None)
        df = dfmain[i]

        column_indices_to_keep = [0, 1, 2, 3, 4, 5]
        df = df.iloc[:, column_indices_to_keep]
        columns_to_fill = [0, 2, 5]
        df.iloc[:-1, columns_to_fill] = df.iloc[:-1,
                                                columns_to_fill].fillna(method='ffill')
        column_name = 'Strategy'
        script_column_name = 'Script'
        value_to_find = basket_name
        replace_flag = False

        for index, row in df.iloc[:-1].iterrows():
            if row[column_name] == value_to_find and pd.isnull(row[script_column_name]):
                if not replace_flag:
                    df.at[index, script_column_name] = stock_name
                    replace_flag = True
                else:
                    break
        # print(df)
        result_rows = df.index[df['Strategy'] == 'total'].tolist()
        # print(result_rows)
        for index, row in df.iloc[:-1].iterrows():
            total_cell_reference = f"E{result_rows[0]+2}"
            allocated_cell_reference = f"B{row.name+2}/F{row.name+2}"
            df.at[row.name,
                  'Total Allocation'] = f"={total_cell_reference}*C{row.name+2}/100"
            df.at[row.name,
                  'Allocated'] = f"={allocated_cell_reference}"
        with pd.ExcelWriter("Master R&D.xlsx", mode="a", engine="openpyxl", if_sheet_exists='overlay') as writer:
            df.to_excel(writer, sheet_name=i, index=False)
        # print(df)
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    workbook = excel.Workbooks.Open(
        "D:\AKSHAT\internship_clone\mastering\Master R&D.xlsx")
    workbook.Save()
    workbook.Close()
    excel.Quit()
