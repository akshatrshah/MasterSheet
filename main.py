import pandas as pd
import numpy as np
from func import myfunc, myfunc2


def formula_generator(df):
    result_rows = df.index[df['Strategy'] == 'Total'].tolist(
    )
    for index, row in df.iloc[:-1].iterrows():
        total_cell_reference = f"E{result_rows[0]+2}"
        allocated_cell_reference = f"B{row.name+2}/F{row.name+2}"
        df.at[row.name,
              'Total Allocation'] = f"={total_cell_reference}*C{row.name+2}/100"
        df.at[row.name,
              'Allocated'] = f"={allocated_cell_reference}"
    return df


def nammer():
    dfmain = pd.read_excel('Master R&D.xlsx', sheet_name=None)
    df = dfmain['sheet1']
    sheet_names = pd.ExcelFile('Master R&D.xlsx').sheet_names
    sheet_names = [element.lower() for element in sheet_names]
    clients = df['CLIENT NAME'].tolist()
    baskets = df.columns.tolist()
    baskets.pop(0)
    return baskets


def get_clients():
    dfmain = pd.read_excel('Master R&D.xlsx', sheet_name=None)
    df = dfmain['sheet1']
    sheet_names = pd.ExcelFile('Master R&D.xlsx').sheet_names
    return sheet_names


def get_corresponding_baskets(client_name):
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
    if client_name in data_dict:
        values = data_dict[client_name]
        filtered_values = [value for value in values if value != 'n']
        return filtered_values
    else:
        return []


# main function takes user inputs from the first screen and finds for empty slots or fill the nan with Script name


def main(stock_name, number):
    number = number-1
    dfmain = pd.read_excel('Master R&D.xlsx', sheet_name=None)
    df = dfmain['sheet1']
    baskets = nammer()

    data_dict = {}
    for index, row in df.iterrows():
        key = row.iloc[0]
        values = row.iloc[1:].tolist()
        data_dict[key] = values
    string_to_drop = 'n'
    data_dict = {key: [value for value in values if value !=
                       string_to_drop] for key, values in data_dict.items()}

    update_clients = []
    for key, value in data_dict.items():
        for i in value:
            if baskets[number] == i:
                update_clients.append(key)
    if stock_name != '':
        myfunc2(update_clients, baskets[number], stock_name)
    else:
        myfunc(update_clients, baskets[number], stock_name)
    return baskets
