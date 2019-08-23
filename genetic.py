def genetic(arr):
    '''
    Entradas : El arreglo arr es un conjunto de individups , cada individuo a su vez es un arreglo de arreglos de tuplas de 4 elementos
    Salida : Un arreglo de individuos como conjunto solucion, donde estan los individuos que optimizan en mayor medida la solucion
    '''
    ### Primer paso: elegir la generacion 0 al azar 
    gen0=arr[0:100]
    ## Segundo Paso : Evaluar su aptitud 
    arrAptitud=[] ## se llenara con las 100 aptitudes de los individuos
    iterador = 0
    for individuo in gen0:
        apt = fitness(individuo)
        arrAptitud.append((iterador,apt))
    ## Tercer  paso : ordenar el arreglo de individos de menor a mayor aptitud y eliminar la mitad menos apta
    arrAptitud.sort(key=lamda x:x[1]) ##ordeno el arreglo por sus aptitudes de menor a mayor
    arrAptitud[len(arrAptitud)/2:] ##dejo solamente la mitad de la generacion de los individuos con mayor aptitud
    gen0mod=[]
    for (ind,apt) in arrAptitud: ##asi saque a los individuos con las aptitudes mas bajas y deje los que me sirven
        temp=gen0.pop(ind)
        gen0mod.append(temp)
    ## Cuarto Paso : Realizar el cruce de los individuos 
    newGen=[]
    for iteracion in range(0,4):
        for indice in range(0,len(gen0mod),2):##para cojer parejas de dos individuos y mutarlas para generar las nuevas generaciones
            ##agarro mis dos indivudos que voy a mutar
            ind1=gen0mod[indice]
            ind2=gen0mod[indice+1]
            ##corto mis individuos para mutarlos 
            startInd1= ind1[:len(ind1)//2]
            startInd2= ind2[:len(ind2)//2]

            endInd1= ind1[(len(ind1)//2)+1:]
            endInd2= ind2[(len(ind2)//2)+1:]
            ###Uno mis individuos y los muto
            newInd1= startInd1+endInd2
            newInd2= startInd2+endInd1
            ##modifico una variable al azar de uno de mis nuevos individuos en mis caso modificare la primera operacion del primer trabajo del individuo
            newInd1[0][0]= newInd1[0][0]+1
            newInd1[0][0]= newInd1[0][1]+1
            newInd1[0][0]= newInd1[0][2]+1
            newInd1[0][0]= newInd1[0][3]+1
            ##le calculo sus aptitudes a mis nuevos 2 individuos
            newGen.append(newInd1)
            newGen.append(newInd2)
        ##Al salir la nueva generacion mutada le calculo la aptitud a cada individuo y realizo el mismo procedimiento que con la generacion 0
        for individuo in newGen:
            apt = fitness(individuo)
            arrAptitud.append((iterador,apt))
        ## Tercer  paso : ordenar el arreglo de individos de menor a mayor aptitud y eliminar la mitad menos apta
        arrAptitud.sort(key=lamda x:x[1]) ##ordeno el arreglo por sus aptitudes de menor a mayor
        arrAptitud[len(arrAptitud)/2:] ##dejo solamente la mitad de la generacion de los individuos con mayor aptitud
        newGenMod=[]
        for (ind,apt) in arrAptitud: ##asi saque a los individuos con las aptitudes mas bajas y deje los que me sirven
            temp=gen0.pop(ind)
            newGenMod.append(temp)
    
    return newGenMod

main():
    ## aca debo definir mi arreglo grande con toda mi poblacion
    solution=[]
    solution= genetic(arr)

main()