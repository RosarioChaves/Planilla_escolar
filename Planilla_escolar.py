def calculo_promedio(*notas):
    suma=0
    promedio=0
    for i in notas:
        suma+=i
    promedio=round(suma/len(notas),2)
    return promedio


while True:
    opci=int(input("\n1. Añadir alumos\n2. Ver planilla\n3. Ver estado de los estudiantes\n4. Salir\n"))
    if opci==1:
        archivo = open('listado.txt', 'a')#si le pongo W se "reinicia" la planilla
        num_personas = int(input("Ingrese la cantidad de alumnos a añadir: "))

        for i in range(num_personas):
            nombre = input("Nombre: ").title()#pone la 1er letra en mayuscula
            apellido = input("Apellido: ").title()
            dni = input("DNI: ")

            notas = []
            for i in range(6):
                nota = float(input(f"Ingrese la nota {i+1}: "))#Crea lista con notas
                notas.append(nota)
            
            promedio=calculo_promedio(*notas)#llamamos la funcion para el calculo de promedio

            if promedio<=6: #Clasifica segun la nota 
                estado="Desaprobado"
            else: estado="Aprobado"

            archivo.write(f"{nombre} {apellido}; {dni} ; {notas}; {promedio} ; {estado}\n")
        archivo.close()

    if opci==2:

        archivo=open('listado.txt', 'r')  #r para lectura
        listado=archivo.read()  #Leer el contenido del archivo y lo asigna a la variante listado
        archivo.close() 

        print(f"-----------------------   PLANILLA DE CALIFICACIONES   -----------------------\n{listado}")
        print("-------------------------------------------------------------------------------")
        archivo.close()

    if opci==3:
        archivo=open('listado.txt', 'r')  # Abrir en modo 'r' para lectura
        print("____________________________\nEstado de los alumnos:\n")
        for linea in archivo:
            datos=linea.strip().split(";")
            estado=datos[-1]  # Obtener el estado desde los datos
            print(f"{datos[0]}:{estado}")
        print("_____________________________")
        archivo.close()
    if opci==4:
        print("Se cerrará el programa...")
        break