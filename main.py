import pandas as pd


# Чтение Excel-файла
df_excel = pd.read_excel('data.xlsx')


# Посмотреть первые 10 строк
print(df_excel.head(15))

print(df_excel.sample(15))

# Посмотреть информацию о таблице
print(df_excel.info())