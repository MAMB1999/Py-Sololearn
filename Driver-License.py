"""Tienes que obtener una nueva licencia de conducir y presentarte en la oficina al mismo tiempo que otras 4 personas.  La oficina dice que verán a todos en orden alfabético y les tomará 20 minutos procesar cada nueva licencia.  Todos los agentes están disponibles ahora y cada uno puede ver a un cliente a la vez.  ¿Cuánto tiempo tardará en salir de la oficina con su nueva licencia?

 Tarea
 Dado el nombre de todos los que aparecieron al mismo tiempo, determine cuánto tiempo llevará obtener su nueva licencia.

 Formato de entrada
 Su entrada será una cadena de su nombre, luego un número entero de la cantidad de agentes disponibles y, por último, una cadena de los otros cuatro nombres separados por espacios.

 Formato de salida
 Producirá un número entero de la cantidad de minutos que le tomará obtener su licencia.

 Entrada de muestra
 'Eric'
 2
 'Adam Caroline Rebecca Frank'

 Salida de muestra
 40"""
persona = input()
empleado = int(input())
llegados = str(input())
llegados = llegados.split(" ")
llegados.append(persona)
llegados = sorted(llegados)
lista = []
con,con2 = 0,0
while  con < len(llegados):
		lista.append([])
		for z in range(empleado):
			   if con < len(llegados):
			  	 lista[con2].append(llegados[con])
			  	 con += 1
			   else:
			   	break
		con2 += 1
		
for w in range(len(lista)):
	if persona in lista[w]:
		print((w+1)*20)
		break