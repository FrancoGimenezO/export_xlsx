# Importar librerias

# herramienta popular para trabajar con archivos Excel (.xlsx)
import openpyxl

# PANDAS: Para crear una tabla Excel en Python, podemos utilizar la librería pandas, que proporciona una forma sencilla de trabajar con datos tabulares y exportarlos a un archivo Excel.
import pandas as pd

#entradas de datos

nombres = input ("Ingrese sus nombres: ")
# Para obtener el primer nombre para el NICKNAME debemos utilizarel la funciòn "aqui va la variable nombres en este caso".split()
nombre0 = nombres.split()

apellidos = input ("Ingrese sus apellidos: ")
# Para obtener el primer apellido es lo mismo
apellido0 = apellidos.split()

f_nac = input ("Ingrese su fecha de nacimiento: ")
CI = int (input ("Ingrese su numero de documento: "))

datos = ("Nombre completo: " + nombres + apellidos + "\n" + "Fecha de nacimiento: " + f_nac + "\n" + "Cedula de Identidad Nº" + str ( CI))

print ("Tus datos son: " + "\n" + datos)

# Crear EXCEL FILE

# Estos 'datos' son los nombres de cada columna con sus respectivos contenidos
# Para combinar dos variables se debe hacer como en 'NOMBRE COMPLETO'
datos_xlsx = {
    'NOMBRE COMPLETO': [nombres + " " + apellidos],
    'NICKNAME': [nombre0[0] + "." + apellido0[0]],
    'FECHA DE NACIMIENTO': [f_nac],
    'CI': [CI]

}

# Creamos el dataframe
df = pd.DataFrame(datos_xlsx)

# Asignamos el nombre al archivo
nombre_archivo = 'tabla_de_datos.xlsx'

#combertimos el 'df' DataFrame en excel siempre escribir el index=False
df.to_excel(nombre_archivo, index=False)

print ("El archivo se guardo correctamente como: " + nombre_archivo + ".")