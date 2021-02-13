from tkinter import *
from tkinter import filedialog
import analizador as analizador
from analizador import *

def imprimir():
	while True:
		print('_____________Menu_____________')
		print('1. Cargar archivos')
		print('2. Desplegar Listas ordenadas')
		print('3. Desplegar busquedas')
		print('4. Desplegar todas')
		print('5. Salir')
		print('______________________________')
		opcion=int(input('ELIJA UNA OPCION'))
		if opcion==1:
			cargar_archivo()
		elif opcion==2:
			desplegar_lista()
		elif opcion==3:
			desplegar_busqueda()
		elif opcion==4:
			desplegar_todas()
		elif opcion==5:	
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
    for i in lista:
    	print(i)

def desplegar_lista():
	print('desplegar_lista')

def desplegar_busqueda():
	print('desplegar_busqueda')

def desplegar_todas():	
    print('desplegar_todas')    	

imprimir()   
