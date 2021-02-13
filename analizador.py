listaABC=['A','B','C','D','E','F','G','H','I','K','L','M','Ñ','O','P','Q','R','S','T','U','V',
           'W','X','Y','Z']
lista=[]  
lista_contador=[] 
lista_identificador=[] 
lista_numeros_global=[] 
lista_ordenado=[] 
lista_busqueda=[]
numeros_busqueda=[]          

def analizar(cadena,contador):
	##array_identificador=cadena.split('=')
	lista_numeros=[]
	contador_posicion=0
	posicion=""
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
					cajon3=cajon3
					paso3=True
				elif caracter=="B":
					cajon4=cajon4
					paso4=True
			else:
				if caracter==",":
					lista_numeros.append(int(cajon2))
					cajon2=""
				else:
					cajon2=cajon2+caracter
		elif paso3==True:
			if caracter=="B":
				paso3=False
				paso4=True
			else:
				cajon3="ORDENADOS"
		elif paso4==True:
			verificar2=caracter.isdigit()
			if verificar2==True:
				cajon6=cajon6+caracter
			else:	
				cajon5="BUSQUEDA POSICIONES="
	

	lista_numeros.append(int(cajon2))			
	if cajon5=="BUSQUEDA POSICIONES=":
		for x in lista_numeros:
			intStr=int(cajon6)
			contador_posicion += 1
			if x==intStr:
				posicion=posicion+str(contador_posicion-1)+","
		if posicion=="":
		    posicion="NO ENCONTRADO"    			   
		cajon6=posicion
	
	if cajon3=="ORDENADOS":
		ordenar=sorted(lista_numeros)
		cajon2=str(ordenar)
		lista_numeros.clear()


	lista.append(str(contador)+". "+cajon+cajon3+"="+cajon2+cajon4+cajon5+cajon6)

    






            
