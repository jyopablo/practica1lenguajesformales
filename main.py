from tkinter import *
from tkinter import filedialog
import analizador as analizador

def cargar_archivo():
    contador = 0  
    ruta=filedialog.askopenfilename(title="abrir")
    archivo=open(ruta)
    for linea in archivo.readlines():
            archivo_sin_espacios=linea.replace(" ","")
            analizador.analizar(archivo_sin_espacios)
            contador += 1              
    archivo.close()


cargar_archivo()    
