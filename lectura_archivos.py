# usamos pandas para la lectura
import pandas as pd

# leer archivo candidato_judicial.csv
tcandidatos_csv = pd.read_csv('candidato_judicial.csv')
print(tcandidatos_csv)


print("CSV")
print("Cantidad de columnas:", len(tcandidatos_csv.columns)) # imprime el texto 'Cantidad de columnas:' y después cuenta cuántas columnas tiene tcandidatos
print("Nombre de las columnas:")
# para cada columna que existe en tcandidatos.columns, 
#guardar temporalmente su nombre en la variable columna y después imprimirlo:
for columna in tcandidatos_csv.columns: #.columns es para acceder a las columnas
    print(columna)


print("*"*140)

# leer el archivoExcel
tcandidatos_xlsx = pd.read_excel("candidato_judicial.xlsx")
print(tcandidatos_xlsx)

print("XLSX")
print("cantidad de columnas: ", len(tcandidatos_xlsx.columns))
print("Nombres de las columnas:")
# para cada columna que existe en tcandidatos.columns, 
#guardar temporalmente su nombre en la variable columnas y después imprimirlo
for columnas in tcandidatos_xlsx.columns:
    print(columnas)

# *************************VER FILAS***********************************************************************
print("\n","*"*140)
# Mostrar todas las columnas
pd.set_option('display.max_columns', None)

# imprimir las primeras 10 filas del archivo:
print("\nprimeras 10 filas de candidato_judicial.csv:","\n",tcandidatos_csv.head(10))
# imprimir las ultimas filas del archivo:
print("\nultimas 10 filas de candidato_judicial.csv:","\n",tcandidatos_csv.tail(10))

# mostrar solo las filas y columnas:
print("\nFilas y columnas de candidato_judicial.csv: ",tcandidatos_csv.shape)

# mostrar fila en especifico:
print("\nFila 0 específica de candidato_judicial.csv:","\n",tcandidatos_csv.iloc[0]) # ver la primera fila, pero puedes poner cualquier número de fila, por ejemplo 400, 2, 3, etc.

# ver varias filas especificas:
print("\nVarias filas específicas, 0, 5 y 10 de candidato_judicial.csv:","\n",tcandidatos_csv.iloc[[0, 5, 10]]) # muestra los registros que están en esas filas

# ver rango de filas:
print("\nRango de filas 10 a 20de candidato_judicial.csv:","\n",tcandidatos_csv.iloc[10:20]) # esto muestra desde la posición 10 hasta antes de la 20