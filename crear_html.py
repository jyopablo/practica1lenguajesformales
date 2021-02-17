from analizador import *
def crear(nombre):
	crear=open(nombre+".html","w")
	crear.write("<html lang=\"en\">")
	crear.write("<head>")
	crear.write("<meta charset=\"UTF-8\">")
	crear.write("<meta name=\"viewport\" content=\"width=, initial-scale=1.0\">")
	crear.write("<link rel=\"stylesheet\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css\" integrity=\"sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh\" crossorigin=\"anonymous\">")
	crear.write("<title>"+nombre+"</title>")	
	crear.write("</head>")
	crear.write("<body>")
	crear.write("<div class=\"container\"><h1>Tabla de datos</h1></div>")
	crear.write("<div class=\"container px-4\"><div class=\"row gx-5\"><div class=\"col\"><div class=\"p-3 border bg-light\">Nombre:Juan Pablo Gonzalez Leal</div></div><div class=\"col\"><div class=\"p-3 border bg-light\">Carne:201901374</div></div></div></div><br><br><br>")
	crear.write("<div class=\"container\"><div class=\"row\"><div class=\"col-sm\"><table class=\"table table-striped\"><thead><tr><th scope=\"col\"><h2>Lista de todos los datos</h2></th></tr></thead><tbody>")
	
	for a in lista:
		crear.write("<tr><td>"+a+" </td></tr>")

	crear.write("</tbody></table><br>")
	crear.write("<table class=\"table table-striped\"><thead><tr><th scope=\"col\"><h2>Lista de datos Ordenados</h2></th></tr></thead><tbody>")
	for b in listas_ordenadas:
		crear.write("<tr><td>"+b+" </td></tr>")

	crear.write("</tbody></table><br>")
	crear.write("<table class=\"table table-striped\"><thead><tr><th scope=\"col\"><h2>Lista de busqueda de datos</h2></th></tr></thead><tbody>")	
	for c in lista_busquedas:
		crear.write("<tr><td>"+c+" </td></tr>")

	crear.write("</tbody></table></div></div></div>")	
	crear.write("<script src=\"https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js\" integrity=\"sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6\" crossorigin=\"anonymous\"></script>")
	crear.write("<script src=\"https://code.jquery.com/jquery-3.4.1.slim.min.js\" integrity=\"sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n\" crossorigin=\"anonymous\"></script>")
	crear.write("<script src=\"https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js\" integrity=\"sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo\" crossorigin=\"anonymous\"></script>")
	crear.write("</body>")
	crear.write("</html>")
	crear.close()
	print('archivo creado')
