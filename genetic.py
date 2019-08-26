##genetic function
import random
##Individiuos de l tipo [[(Machine,tiempo),(Machine,time)],[(machine,time)]]
def gen0(individuos,maquinas,trabajos,operaciones):
    '''
    Entradas : el numero de individos que voy a generar y un numero de maquinas las cuales son las elegibles para armas los individuos con las operaciones 
    salidas: un arreglo con puros individuos corresponde a la generacion0, ejemplo de una salida cualquiera : [[(Machine,tiempo),(Machine,time)],[(machine,time)]]
    '''
    gen0=[]
    for i in range(0,individos)
        ind = []
        for tr in range(0,trabajos):
            trabajo= []
            for operacion in range(0,operaciones):
                #armo una operacion 
                op = (random.randrange(numMaquinas) , random.randrange(10))
                #añado la operacion al trabajos
                trabajo.append(op)
            ##Añado la el trabajo al individuo
            ind.append(trabajo)
        ##añado el individuo creado con sus trabajos al la generacion 0
        gen0.append(ind)
    return gen0

def aptitud(gen0,k):
    arrAptitud=[]
    for individuo in gen0:
        apt = fitness(individuo,k)
        arrAptitud.append((iterador,apt))
    return arrAptitud

def masAptos(gen0,arrAptitud):
    arrAptitud.sort(key=lamda x:x[1]) ##ordeno el arreglo por sus aptitudes de menor a mayor
    arrAptitud[len(arrAptitud)/2:] ##dejo solamente la mitad de la generacion de los individuos con mayor aptitud
    gen0mod=[]
    for (ind,apt) in arrAptitud: ##asi saque a los individuos con las aptitudes mas bajas y deje los que me sirven
        temp=gen0.pop(ind)
        gen0mod.append(temp)
    return gen0mod


def ruleta(arrAptitud):
  sumatoria = 0
  prob=[]
  probAcumulada=[]
  for i in range(len(arrAptitud)):
    sumatoria+=arrAptitud[i][0]
  for i in range(len(arrAptitud)):
    pi=arrAptitud[i][0]/sumatoria
    prob.append(pi)
  for i in range(len(prob)):
    pa=0
    for j in range(i):
      pa+=prob[j]
    probAcumulada.append(pa)
  p=random.uniform(0,1)
  iterador,indice,flag=0,0,False
  while iterador!=len(pac) and flag==False:
    if p>probAcumulada[iterador-1] and p<=probAcumulada[iterador]:
      indice=iterador
      flag=True
    iterador+=1
  return indice

def corteYmutado(ind1,ind2,gen,maquinas,tiempo):
    ##corto mis individuos para mutarlos 
    cut= random.randrange(len(ind1)) ##por donde voy a cortar los individuos, selecciono como un valor random entre el len del objeto
    startInd1= ind1[:len(ind1)//cut]
    startInd2= ind2[:len(ind2)//cut]
    endInd1= ind1[(len(ind1)//cut)+1:]
    endInd2= ind2[(len(ind2)//cut)+1:]
    ###Uno mis individuos y los muto
    hijo1= startInd1+endInd2##individuo mutado numero 1
    hijo2= startInd2+endInd1##indivoduo mutado numero 2
    ## Factor de criterio de si voy a mutar dos indivuduos 
    prob = random.randrange(100)
    if (prob>95 ): # dado el caso que le de al 5 porciento de probabilidad de mutacion entonces muto si no solo agrego a la nueva generacion
        hijoAmutar= random.randrange(0,2)
        variableAmutar = random.random(0,2)
        ##Muto
        if(variableAmutar==1):
            hijoAmutar[0][variableAmutar]= newInd1[0][variableAmutar]+(random.randrange(maquinas))##muto la maquina
        else:
            hijoAmutar[0][variableAmutar]= newInd1[0][variableAmutar]+(random.randrange(10))##muto el tiemo

    else:
        ##le calculo sus aptitudes a mis nuevos 2 individuos
        gen.append(newInd1)##meto los hijjos de la generacion junto con los padres
        gen.append(newInd2)

def genetic(numGen,k,numMaquinas,individuos,trabajo,operaciones,tiempo):
    '''
    Entradas : 
    Salida : Un arreglo de individuos como conjunto solucion, donde estan los individuos que optimizan en mayor medida la solucion
    '''
    ## Primer paso: generar la generacion 0 
    gen0=gen0(individuos,numMaquinas,trabajos,operaciones) ##esto me retorna la generacion 0 con ese numero de elementos 
    for iteracion in range(0,numGen):
        ## Segundo Paso : Evaluar su aptitud 
        arrAptitud=aptitud(gen0,k) 
        ## Tercer  paso : ordenar el arreglo de individos de menor a mayor aptitud y eliminar la mitad menos apta
        gen=masAptos(gen0,arrAptitud)
        ## Cuarto Paso : Realizar el cruce de los individuos 
        ind1= ruleta(arrAptitud)
        ind2= ruleta(arrAptitud)
        #agarro mis dos indivudos que voy a cortar
        padre1=gen0mod[ind1]
        padre2=gen0mod[ind2]
        newGen=[] 
        newGen=corteYmutado(padre1,padre2,gen0,numMaquinas,tiempo)##de aca me salen todas las combinaciones 
        gen0=newGen ##asi para arrancar de nuevo el cicl
    return gen0
            
main():
    solution=[]
    solution= genetic(arr,numGen,k)

main()