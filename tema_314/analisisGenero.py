import pandas as pd # El as pd significa que le ponemos el alias pd, para no tener que escribir pandas cada vez.
import matplotlib.pyplot as plt

from conexionBD import conexionBD # mportamos la clase conexionBD

class analisisGenero:

    def __init__(self, conexion): # conexion es un parámetro que recibe la conexión a PostgreSQL
        self.conexion = conexion

    def obtener_genero(self): # metodo para Consultar la base de datos y obtener la cantidad de candidatos por género
        # Aquí estás creando una variable llamada consulta
        consulta = """ 
            SELECT id_genero, COUNT(*) AS cantidad
            FROM siac.tcandidato_judicial
            WHERE id_genero IN (1, 2)
            GROUP BY id_genero
            ORDER BY id_genero;
        """
        # GROUP BY id_genero para agrupar los registros según su género
        # ORDER BY id_genero Ordena los resultados por id_genero

        df = pd.read_sql(consulta, self.conexion) # utiliza Pandas para ejecutar una consulta SQL y convertir el resultado en un DataFrame

        return df # devuelve el datframe, esto permite que otro método pueda recibir los resultados, mostrar_grafica() va a recibirlos.

    def mostrar_grafica(self):

        df = self.obtener_genero()

        # cambiar los nums por nombres, un diccionario 
        nombres = {
            1 : "mujeres",
            2 : "hombres"
        }

        df["genero"] = df["id_genero"].map(nombres) # crea la columna para la tabla que vemos en la terminal, usar id_genero y utiliza el diccionario para converir 1 a mujeres ... y vemos cantidad y genero

        print(df) # imprimir dataframe

        plt.pie( # crea una gráfica circular, también conocida como gráfica de pastel.
            df["cantidad"], # Indica qué valores utilizará para determinar el tamaño de cada sección, los hombres y mujeres
            labels = df["genero"], # nombres que aparecerán en las secciones
            autopct = "%1.1f%%" # Indica que quieres mostrar el porcentaje en cada sección con un decimal
        )

        plt.title("candidaturas por género")
        plt.show()