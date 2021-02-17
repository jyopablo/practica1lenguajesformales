from tkinter import *
from tkinter import filedialog
import analizador as analizador
import crear_html as crear_html
from analizador import *

def imprimir():
	while True:
		print('_____________Menu_____________')
		print('1. Cargar archivos')
		print('2. Desplegar Listas ordenadas')
		print('3. Desplegar busquedas')
		print('4. Desplegar todas')
		print('5. Desplegar todas a archivo')
		print('6. Salir')
		print('______________________________')
		opcion=int(input('ELIJA UNA OPCION'))
		if opcion==1:
			lista.clear()
			listas_ordenadas.clear()
			lista_busquedas .clear()
			cargar_archivo()
		elif opcion==2:
			desplegar_ordenados()
		elif opcion==3:
			desplegar_busqueda()
		elif opcion==4:
			desplegar_todas()
		elif opcion==5:		
			desplegar_todas_archivo()
		elif opcion==6:
		    break	



def cargar_archivo():
    contador = 0  
    ruta=filedialog.askopenfilename(title="abrir")
    archivo=open(ruta)
    for linea in archivo.readlines():
            archivo_sin_espacios=linea.replace(" ","")
            analizador.analizar(archivo_sin_espacios,contador)
            contador += 1              
    archivo.close()
    print('Datos Cargados')
    

def desplegar_ordenados():
	for i in listas_ordenadas:
		print(i)
 
def desplegar_busqueda():
	for j in lista_busquedas:
		print(j)

def desplegar_todas():	
    for k in lista:
    	print(k)    	

def desplegar_todas_archivo():
	nombre_archivo=input('Nombre archivo:')
	crear_html.crear(nombre_archivo)
	

imprimir()   
