import pandas as pd

learn_data = pd.read_excel("dataset.xlsx")
df = learn_data.pivot(index=['col_name_1', 'col_name_2', 'col_name_3', 'col_name_4', 'col_name_5'],
                      columns='row_name_converting_to_col', values=['value_col_1', 'value_col_2'])

df.to_excel('output.xlsx', sheet_name='Sheet_1') #export into an excel file
# df.to_csv('output_1.csv') #or csv

print(df.head(1))
