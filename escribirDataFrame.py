import pandas as pd

# crear un dataframe de ejemplo

# Crearlo
data = {'Name' : ['John', 'Anna', 'Peter'],
        'Age' : [28, 24, 33],
        'Country' : ['USA', 'Sweden', 'Germany']}
# Guardarlo 
df = pd.DataFrame(data)

# Escribir el dataframe data en un archivo CSV y XLSX sin índice
df.to_csv('data0.csv', index=False)
df.to_excel('data0.xlsx', index=False)

# Escribir el dataframe data en un archivo CSV y XLSX
df.to_csv('data.csv')
df.to_excel('data.xlsx')