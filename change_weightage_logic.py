import pandas as pd

from main import formula_generator


def change_weightage(client_name, values):
    dfmain = pd.read_excel('Master R&D.xlsx', sheet_name=None)
    df = dfmain[client_name]
    df['Weightage'] = df['Strategy'].map(values)
    df = formula_generator(df)
    with pd.ExcelWriter("Master R&D.xlsx", mode="a", engine="openpyxl", if_sheet_exists='overlay') as writer:
        df.to_excel(writer, sheet_name=client_name, index=False)


# change_weightage(client_name='axt', values={
#                  'Result Conviction ': 11, 'BNH based on Upsdie': 12})
