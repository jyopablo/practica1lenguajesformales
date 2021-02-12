listaABC=['A','B','C','D','E','F','G','H','I','K','L','M','Ñ','O','P','Q','R','S','T','U','V',
           'W','X','Y','Z']
lista=[]           
lista_buscar=[]
def analizar(cadena):
	##array_identificador=cadena.split('=')
	cajon=""
	cajon1=""
	cajon2=""
	cajon3=""
	cajon4=""
	cajon5=""
	cajon6=""
	paso1=True
	paso2=False
	paso3=False
	paso4=False
	for i in cadena:
		caracter=i
		if paso1==True:
			if caracter=="=":
				paso1=False
				paso2=True
				cajon=cajon+":"
			
			else:
				cajon=cajon+caracter
		elif paso2==True:
			verificar=caracter in listaABC
			if verificar==True:
				paso2=False
				if caracter=="O":
					cajon3=cajon3+caracter
					paso3=True
				elif caracter=="B":
					cajon4=cajon4+caracter
					paso4=True
			else:	
				cajon2=cajon2+caracter
		elif paso3==True:
			if caracter=="B":
				paso3=False
				paso4=True
				cajon4=cajon4+caracter
			else:
				cajon3=cajon3+caracter
				cajon3="ORDENADOS"
		elif paso4==True:
			verificar2=caracter.isdigit()
			if verificar2==True:
				cajon6=cajon6+caracter
			else:	
				cajon5=cajon5+caracter
				cajon5="BUSQUEDA POSICIONES="
				
	lista.append(cajon+cajon3+"="+cajon2+cajon4+cajon5+cajon6)	
	lista_buscar.append(cajon6)		
	print(lista)			
			



            
