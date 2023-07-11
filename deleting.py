# Logic for CLEAR SCRIPT
import pandas as pd
import win32com.client as win32


def getting_data_dict():
    dfmain = pd.read_excel('Master R&D.xlsx', sheet_name=None)
    df = dfmain['sheet1']
    data_dict = {}
    for index, row in df.iterrows():
        key = row.iloc[0]
        values = row.iloc[1:].tolist()
        data_dict[key] = values
    string_to_drop = 'n'
    data_dict = {key: [value for value in values if value !=
                       string_to_drop] for key, values in data_dict.items()}
    return data_dict


def deleting_cells(basket_name):
    dfmain = pd.read_excel('Master R&D.xlsx', sheet_name=None)
    dfhome = dfmain['home']
    dfhome = dfhome.fillna(method='ffill')
    appropriate_rows_from_home = dfhome[dfhome['Strategy'] == basket_name]
    available_stocks = list(set(appropriate_rows_from_home['Script'].tolist()))
    return available_stocks


def deleting_the_specific_stock(stock_name, basket_name):
    dfmain = pd.read_excel('Master R&D.xlsx', sheet_name=None)
    data_dict = getting_data_dict()
    useful_clients = []
    for i in data_dict:
        if basket_name in data_dict[i]:
            useful_clients.append(i)
    for i in useful_clients:
        df = dfmain[i]
        column_indices_to_keep = [0, 1, 2, 3, 4, 5]
        df = df.iloc[:, column_indices_to_keep]
        columns_to_fill = [0, 2, 5]
        df.iloc[:-1, columns_to_fill] = df.iloc[:-1,
                                                columns_to_fill].fillna(method='ffill')
        df.at[df.loc[(df['Strategy'] == basket_name) & (
            df['Script'] == stock_name)].index[0], 'Script'] = ''
        result_rows = df.index[df['Strategy'].isin(['total', 'Total', 'TOTAL'])].tolist(
        )
        for index, row in df.iloc[:-1].iterrows():
            total_cell_reference = f"E{result_rows[0]+2}"
            allocated_cell_reference = f"B{row.name+2}/F{row.name+2}"
            df.at[row.name,
                  'Total Allocation'] = f"={total_cell_reference}*C{row.name+2}/100"
            df.at[row.name,
                  'Allocated'] = f"={allocated_cell_reference}"

        # print(df)
        with pd.ExcelWriter("Master R&D.xlsx", mode="a", engine="openpyxl", if_sheet_exists='replace') as writer:
            df.to_excel(writer, sheet_name=i, index=False)

    excel = win32.gencache.EnsureDispatch('Excel.Application')
    workbook = excel.Workbooks.Open(
        "D:\AKSHAT\internship_clone\mastering\Master R&D.xlsx")
    workbook.Save()
    workbook.Close()
    excel.Quit()


# deleting_the_specific_stock('VBL', 'Split (Corporate Action)')
