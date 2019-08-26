##genetic function
import random
##Individiuos de l tipo [[(Machine,tiempo),(Machine,time)],[(machine,time)]]
def gen0():


def genetic(numGen,k):
    '''
    Entradas : 
    Salida : Un arreglo de individuos como conjunto solucion, donde estan los individuos que optimizan en mayor medida la solucion
    '''
    ### Primer paso: elegir la generacion 0 al azar 
    gen0=arr[:100]
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
    
    
    for iteracion in range(0,numGen):
        for indice in range(0,len(gen0mod),2):##para cojer parejas de dos individuos y mutarlas para generar las nuevas generaciones
            
            ## Factor de criterio de si voy a mutar dos indivuduos o no 
            prob  = random.randrange(100)
            if (prob>95 ): # dado el caso que le de al 5 porciento de probabilidad de mutacion entonces muto si no solo agrego a la nueva generacion

            ##agarro mis dos indivudos que voy a mutar
            ind1=gen0mod[indice]
            ind2=gen0mod[indice+1]

            ##corto mis individuos para mutarlos 
            cut= random.randrange(10) ##por donde voy a cortar los individuos
            startInd1= ind1[:len(ind1)//cut]
            startInd2= ind2[:len(ind2)//cut]
            
            endInd1= ind1[(len(ind1)//cut)+1:]
            endInd2= ind2[(len(ind2)//cut)+1:]
            ###Uno mis individuos y los muto
            newInd1= startInd1+endInd2
            newInd2= startInd2+endInd1
            ##modifico una variable al azar de uno de mis nuevos individuos en mis caso modificare la primera operacion del primer trabajo del individuo
            newInd1[0][0]= newInd1[0][0]+(random.randrange(10))##vario cada componente de mi individuo de manera aleatoria
            newInd1[0][0]= newInd1[0][1]+(random.randrange(10))
            newInd1[0][0]= newInd1[0][2]+(random.randrange(10))
            newInd1[0][0]= newInd1[0][3]+(random.randrange(10))
            ##le calculo sus aptitudes a mis nuevos 2 individuos
            gen0mod.append(newInd1)##meto los hijjos de la generacion junto con los padres
            gen0mod.append(newInd2)
        ##Al salir la nueva generacion mutada le calculo la aptitud a cada individuo y realizo el mismo procedimiento que con la generacion 0
        for individuo in gen0mod:
            apt = fitness(individuo)
            arrAptitud.append((iterador,apt))
        ## Tercer  paso : ordenar el arreglo de individos de menor a mayor aptitud y eliminar la mitad menos apta
        arrAptitud.sort(key=lamda x:x[1]) ##ordeno el arreglo por sus aptitudes de menor a mayor
        arrAptitud[len(arrAptitud)/2:] ##dejo solamente la mitad de la generacion de los individuos con mayor aptitud
        #newGenMod=[]
        for (ind,apt) in arrAptitud: ##asi saque a los individuos con las aptitudes mas bajas y deje los que me sirven
            temp=gen0.pop(ind)
            gen0mod.append(temp)
    
    return gen0mod

main():
    ## aca debo definir mi arreglo grande con toda mi poblacion
    arr = genPoblacion()
    solution=[]
    solution= genetic(arr,numGen,k)

main()