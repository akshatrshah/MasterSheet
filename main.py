import pandas as pd
import numpy as np
from func import myfunc, myfunc2


def nammer():
    dfmain = pd.read_excel('Master R&D.xlsx', sheet_name=None)
    df = dfmain['sheet1']
    sheet_names = pd.ExcelFile('Master R&D.xlsx').sheet_names
    sheet_names = [element.lower() for element in sheet_names]
    clients = df['CLIENT NAME'].tolist()
    baskets = df.columns.tolist()
    baskets.pop(0)
    return baskets

# main function takes user inputs from the first screen and finds for empty slots


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
