from conexionBD import conexionBD # Importamos la clase conexionBD que creamos anteriormente. Esta clase es la encargada de establecer y cerrar la conexión con PostgreSQL.
from analisisGenero import analisisGenero # importamos la clase que es la encargada de hacer la consulta, obtener los datos y generar la gráfica
'''
Aquí creamos un objeto de la clase conexionBD y lo guardamos en la variable bd.

Al crear el objeto, automáticamente se ejecuta su __init__().

Por lo tanto, en este momento:

Se establece la conexión con PostgreSQL.
'''
bd = conexionBD() # Aquí creamos un objeto de la clase analisisGenero y le pasamos bd.conexion, la conexión que acabamos de abrir.

analisis = analisisGenero(bd.conexion) # objeto llamado analisis de la clase analisisGenero. Crea el objeto analisis y da la conexión que tiene bd

analisis.mostrar_grafica() # Crear el objeto analisis y dale la conexión que tiene bd

bd.cerrar