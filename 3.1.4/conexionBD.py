import psycopg # Importa la librería psycopg, que permite que Python se comunique con PostgreSQL

class conexionBD:  # creando una clase llamada ConexionBD. La clase sirve como una especie de molde para manejar la conexión
    # def es una palabra reservada de python que es para definir una funcion: método que pertenece  una clase
    def __init__(self): # __init__ Se ejecuta automáticamente cuando creas un objeto de una clase.
        # self es una referencia al objeto actual.
        self.conexion = psycopg.connect( # psycopg.connect() le dice a psycopg: establecer una conexión con un servidor PostgreSQL, Y el resultado de esa conexión se guarda en: self.conexion
            host = "localhost",
            port = 5432,
            dbname = "siac",
            user = "postgres",
            password = "123"
        ) # se cierra psycopg.connect(...)

        print("conexión exitosa a postgresql")

    def cerrar(self): # Creas un método llamado cerrar. Su propósito es cerrar la conexión.

        self. conexion.close() # es cómo: ya terminé de utilizarla, ciérrala, se usa cuado usamos bd.cerrar()

        print("conexion cerrada")

'''
Esta clase es la encargada de manejar la conexión entre Python y PostgreSQL. 
Primero importamos psycopg, que nos permite comunicarnos con PostgreSQL. 

Después tenemos el método __init__, que se ejecuta automáticamente cuando creamos un objeto de ConexionBD. 
Ahí utilizamos psycopg.connect() y le damos los datos del servidor, el puerto, la base de datos y las credenciales. 
La conexión se guarda en self.conexion, para que podamos utilizarla posteriormente desde otras clases. Finalmente tenemos cerrar(), 
que nosotros ejecutamos cuando ya terminamos de trabajar con la base de datos y que utiliza close() para cerrar la conexión.

self es una referencia al objeto actual. En este caso, self.conexion significa que estamos guardando la conexión como una propiedad 
del objeto ConexionBD, para poder acceder a ella después.

__init__ Es un método especial de Python que se ejecuta automáticamente cuando creamos un objeto de la clase. 
Nosotros lo utilizamos para abrir la conexión desde el momento en que creamos ConexionBD

'''