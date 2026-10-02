# librerias
import pandas as pd

# clase conexion a la base de datos
from tema_314.conexionBD import conexionBD
# Clase para escribir datos en CSV y Excel
class escrituraBD:
    def __init__(self):
        self.bd = conexionBD()
        self.conexion = self.bd.conexion

    def guardar_distritos(self):
        consulta = """
        SELECT * FROM siac.tdistrito_judicial
        """

        # obtener datos de postgresql
        df = pd.read_sql(consulta, self.conexion)

        # escribir CSV
        df.to_csv("tdistrito_judicial.csv", index = False)

        # escribir Excel
        df.to_excel("tdistrito_judicial.xlsx", index = False)

        # cerrar conexion
        self.bd.cerrar()


# ejecutar 
escritura = escrituraBD()
escritura.guardar_distritos()

     

       
    