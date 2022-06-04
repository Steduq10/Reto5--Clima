import csv
import json

def clima ():
    cabecera = []  #Creamos un lista vacia para la cabecera
    registros = [] #Creamos un lista vacia para los registros
    with open('data.csv', 'r') as csvfile:   #Importamos el archico csv
        data = csv.reader(csvfile)

        cabecera = next(data)

        for fila in data:
            registros.append(fila)

    #print(cabecera)
    #print(registros)
    #print(len(registros))
    #Creamos las listas que almacenarán los datos para cada una de las locaciones
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []

    for i in registros:
        if (i[1]) == '1':
            datos = [i[2],i[3]]
            l1.append(datos)
        elif (i[1]) == '2':
            datos = [i[2],i[3]]
            l2.append(datos)
        elif (i[1]) == '3':
            datos = [i[2],i[3]]
            l3.append(datos)
        elif (i[1]) == '4':
            datos = [i[2],i[3]]
            l4.append(datos)
        elif (i[1]) == '5':
            datos = [i[2],i[3]]
            l5.append(datos)
    #print(f'locacion 1: {l1}')
    #print(f'locacion 2: {l2}')
    #print(f'locacion 3: {l3}')
    #print(f'locacion 4: {l4}')
    #print(f'locacion 5: {l5}')

    temperatura1 = []
    temperatura2 = []
    temperatura3 = []
    temperatura4 = []
    temperatura5 = []

    #print('Temperaturas')
    for i in l1:
        valor = i[0]
        temperatura1.append(valor)
    #print(temperatura1)
    #print(len(temperatura1))
    for i in l2:
        valor = i[0]
        temperatura2.append(valor)
    #print(temperatura2)
    #print(len(temperatura2))
    for i in l3:
        valor = i[0]
        temperatura3.append(valor)
    #print(temperatura3)
    #print(len(temperatura3))
    for i in l4:
        valor = i[0]
        temperatura4.append(valor)
    #print(temperatura4)
    #print(len(temperatura4))
    for i in l5:
        valor = i[0]
        temperatura5.append(valor)
    #print(temperatura5)
    #print(len(temperatura5))
    #print('Presiones')
    presion1 = []
    presion2 = []
    presion3 = []
    presion4 = []
    presion5 = []

    for i in l1:
        valor = i[1]
        presion1.append(valor)
    #print(presion1)

    for i in l2:
        valor = i[1]
        presion2.append(valor)
    #print(presion2)

    for i in l3:
        valor = i[1]
        presion3.append(valor)
    #print(presion3)

    for i in l4:
        valor = i[1]
        presion4.append(valor)
    #print(presion4)

    for i in l5:
        valor = i[1]
        presion5.append(valor)
    #print(presion5)

    #Convertimos los valores de la lista temperatura a int

    intTemperatura1 = [int(i) for i in temperatura1]
    intTemperatura2 = [int(i) for i in temperatura2]
    intTemperatura3 = [int(i) for i in temperatura3]
    intTemperatura4 = [int(i) for i in temperatura4]
    intTemperatura5 = [int(i) for i in temperatura5]

    #Calculamos el valor promedio de las temperaturas y las presiones en cada una de las locaciones
    #print('Temperaturas promedio')

    promTemp1 = sum(intTemperatura1)/len(intTemperatura1)
    promTemp1 = round(promTemp1, 1)
    promTemp2 = sum(intTemperatura2) / len(intTemperatura2)
    promTemp2 = round(promTemp2, 1)
    promTemp3 = sum(intTemperatura3) / len(intTemperatura3)
    promTemp3 = round(promTemp3, 1)
    promTemp4 = sum(intTemperatura4) / len(intTemperatura4)
    promTemp4 = round(promTemp4, 1)
    promTemp5 = sum(intTemperatura5) / len(intTemperatura5)
    promTemp5 = round(promTemp5, 1)
    '''
    suma = 0
    for i in intTemperatura1:

        suma += i
        
        promTemp1 = suma / (len(intTemperatura1))
        promTemp1 = round(promTemp1, 1)
    #print(promTemp1)

    suma = 0
    for i in intTemperatura2:

        suma += i
        promTemp2 = suma / (len(intTemperatura2))
        promTemp2 = round(promTemp2, 1)
    #print(promTemp2)

    suma = 0
    for i in intTemperatura3:

        suma += i
        promTemp3 = suma / (len(intTemperatura3))
        promTemp3 = round(promTemp3, 1)
    #print(promTemp3)

    suma = 0
    for i in intTemperatura4:

        suma += i
        promTemp4 = suma / (len(intTemperatura4))
        promTemp4 = round(promTemp4, 1)
    #print(promTemp4)

    suma = 0
    for i in intTemperatura5:

        suma += i
        promTemp5 = suma / (len(intTemperatura5))
        promTemp5 = round(promTemp5, 1)
    #print(promTemp5)

    
    '''

    #print('Presiones promedio')

    intPresion1 = [int(i) for i in presion1]
    intPresion2 = [int(i) for i in presion2]
    intPresion3 = [int(i) for i in presion3]
    intPresion4 = [int(i) for i in presion4]
    intPresion5 = [int(i) for i in presion5]
    '''
    suma = 0
        for i in intPresion1:
    
            suma += i
            promPre1 = suma / (len(intPresion1))
            promPre1 = round(promPre1, 1)
        #print(promPre1)
    
        suma = 0
        for i in intPresion2:
    
            suma += i
            promPre2 = suma / (len(intPresion2))
            promPre2 = round(promPre2, 1)
        #print(promPre2)
    
        suma = 0
        for i in intPresion3:
    
            suma += i
            promPre3 = suma / (len(intPresion3))
            promPre3 = round(promPre3, 1)
        #print(promPre3)
    
        suma = 0
        for i in intPresion4:
    
            suma += i
            promPre4 = suma / (len(intPresion4))
            promPre4 = round(promPre4, 1)
        #print(promPre4)
    
        suma = 0
        for i in intPresion5:
    
            suma += i
            promPre5 = suma / (len(intPresion5))
            promPre5 = round(promPre5, 1)
        #print(promPre5)
    '''
    promPre1 = sum(intPresion1)/len(intPresion1)
    promPre1 = round(promPre1, 1)
    promPre2 = sum(intPresion2) / len(intPresion2)
    promPre2 = round(promPre2, 1)
    promPre3 = sum(intPresion3) / len(intPresion3)
    promPre3 = round(promPre3, 1)
    promPre4 = sum(intPresion4) / len(intPresion4)
    promPre4 = round(promPre4, 1)
    promPre5 = sum(intPresion5) / len(intPresion5)
    promPre5 = round(promPre5, 1)

    #Creamos una lista con los valores de las temperaturas y las presiones

    locacion1 = [promTemp1,promPre1]
    locacion2 = [promTemp2,promPre2]
    locacion3 = [promTemp3,promPre3]
    locacion4 = [promTemp4,promPre4]
    locacion5 = [promTemp5,promPre5]

    #print(locacion1)
    #print(locacion2)
    #print(locacion3)
    #print(locacion4)
    #print(locacion5)

    locacionTotal = [locacion1,locacion2,locacion3,locacion4,locacion5]

    #Creamos el diccionario que tendra por clave, el # de la locación y por valor la lista de temp y presion promedio
    diccionario = {}

    j = 1
    while j <= 5:
        for i in range(len(locacionTotal)):
            diccionario[j] = locacionTotal[i]
            j +=1
    #print(diccionario)
    datos = json.dumps(diccionario)
    print(datos)
    id = []
    local = []
    temperaturas = []
    presiones = []
    for i in registros:
        dato = i[2]
        temperaturas.append(dato)

    for i in registros:
        dato = i[0]
        id.append(dato)

    for i in registros:
        dato = i[1]
        local.append(dato)

    for i in registros:
        dato = i[3]
        presiones.append(dato)

    intId = [int(i) for i in id]
    intLocal = [int(i) for i in local]
    intTemperaturas = [int(i) for i in temperaturas]
    intPresiones = [int(i) for i in presiones]

    intRegistros = []

    for i in range(len(registros)):
        nuevo = [intId[i],intLocal[i],intTemperaturas[i],intPresiones[i]]
        intRegistros.append(nuevo)
    #print(intRegistros)
    tempAbove = []
    for i in intRegistros:
        if (i[1]) == 1:

            if i[2] < promTemp1:
                dato = "NO"
                tempAbove.append(dato)
            elif i[2] == promTemp1:
                dato = "IGUAL"
                tempAbove.append(dato)
            elif i[2] > promTemp1:
                dato = "SI"
                tempAbove.append(dato)
        elif i[1] == 2:

            if i[2] < promTemp2:
                    dato = "NO"
                    tempAbove.append(dato)
            elif i[2] == promTemp2:
                    dato = "IGUAL"
                    tempAbove.append(dato)
            elif i[2] > promTemp2:
                    dato = "SI"
                    tempAbove.append(dato)

        elif (i[1]) == 3:

            if i[2] < promTemp3:
                    dato = "NO"
                    tempAbove.append(dato)
            elif i[2] == promTemp3:
                    dato = "IGUAL"
                    tempAbove.append(dato)
            elif i[2] > promTemp3:
                    dato = "SI"
                    tempAbove.append(dato)
        elif (i[1]) == 4:

            if i[2] < promTemp4:
                    dato = "NO"
                    tempAbove.append(dato)
            elif i[2] == promTemp4:
                    dato = "IGUAL"
                    tempAbove.append(dato)
            elif i[2] > promTemp4:
                    dato = "SI"
                    tempAbove.append(dato)

        elif (i[1]) == 5:

            if i[2] < promTemp5:
                    dato = "NO"
                    tempAbove.append(dato)
            elif i[2] == promTemp5:
                    dato = "IGUAL"
                    tempAbove.append(dato)
            elif i[2] > promTemp5:
                    dato = "SI"
                    tempAbove.append(dato)

    #print(tempAbove)
    #print(len(tempAbove))
    presAbove = []
    for i in intRegistros:
        if (i[1]) == 1:

            if i[3] < promPre1:
                dato = "NO"
                presAbove.append(dato)
            elif i[3] == promPre1:
                dato = "IGUAL"
                presAbove.append(dato)
            elif i[3] > promPre1:
                dato = "SI"
                presAbove.append(dato)
        elif i[1] == 2:

            if i[3] < promPre2:
                dato = "NO"
                presAbove.append(dato)
            elif i[3] == promPre2:
                dato = "IGUAL"
                presAbove.append(dato)
            elif i[3] > promPre2:
                dato = "SI"
                presAbove.append(dato)

        elif (i[1]) == 3:

            if i[3] < promPre3:
                dato = "NO"
                presAbove.append(dato)
            elif i[3] == promPre3:
                dato = "IGUAL"
                presAbove.append(dato)
            elif i[3] > promPre3:
                dato = "SI"
                presAbove.append(dato)
        elif (i[1]) == 4:

            if i[3] < promPre4:
                dato = "NO"
                presAbove.append(dato)
            elif i[3] == promPre4:
                dato = "IGUAL"
                presAbove.append(dato)
            elif i[3] > promPre4:
                dato = "SI"
                presAbove.append(dato)

        elif (i[1]) == 5:

            if i[3] < promPre5:
                dato = "NO"
                presAbove.append(dato)
            elif i[3] == promPre5:
                dato = "IGUAL"
                presAbove.append(dato)
            elif i[3] > promPre5:
                dato = "SI"
                presAbove.append(dato)
    #print(len(presAbove))
    #print(presAbove)

    cabecera.append('above_avg_temp')
    cabecera.append('above_avg_pres')
    #print(cabecera)



    registrosNuevos = []
    for i in range(len(intRegistros)):
        nuevo = [intId[i],intLocal[i],intTemperaturas[i],intPresiones[i],tempAbove[i],presAbove[i]]
        registrosNuevos.append(nuevo)

    with open('data_nuevo.csv','w') as nuevocsv:
        escritor = csv.writer(nuevocsv)

        escritor.writerow(cabecera)

        escritor.writerows(registrosNuevos)

    with open('data_nuevo.csv','r') as salida:
        salida.read()
        #print(salida.read())

clima()