##Fitness Function 
##La estructura de mi individuo esta dada por una lista de listas en la cual en cada sublista hay una tupla con las caracteristicas (maquina,operacion,t inicio, tfinal)
##el castigo por tiempo se acumula dependiendo de la cantidad de unidades que se pase o que le falte al valor k
def fitness(arr,k):
    fouls=0
    # aca castigo o recompenso por tiempo
    maxTime=0
    for task in arr:##Recorro cada trabajo en el arreglo de los trabajos y vero si se pasa del tiempo
        for op in task:
            #print(maxTime,k)
            if op[3]>maxTime:##es para actualizar el maximo en cada operacion
                maxTime=op[3]
                #print("el maximo va en",maxTime) 
            if maxTime > k:##veo en cada iteracion si el tiempo maximo que llevan las operaciones no se ha pasado del tiempo 
                #print("es mayor")
                score = 100/(maxTime-k)
                if maxTime==(k+1): score=50 ##dado el caso que la diferencia de tiempo se pase por 1 sola unidad entonces para que la division no de 100, le quemo el valor de 75, ya que si se pasa de 2 unidades en adelante funciona bien
                if maxTime==(k+2): score=49
                return score
            else:
                if (maxTime==1): score=100
                else: score = 50+((100/maxTime))
                if (maxTime==2): score=99  
               
    
    return score
    operations=[]
    times=[]
    for task in arr:
        for op in task:
            operations.append(op[1])
            times.append((op[0],op[2],op[3]))
        print(times)
        copy = operations[:]
        copy.sort()
        if operations != copy:
            fouls+=1

    ##for tupl in times:


        
    
            


    


def main():
    ex=[[(1,2,3,4),(2,3,1,3)],[(1,2,3,4),(4,5,6,7),(5,3,1,2)],[(1,5,6,9)]]
    #ex=[[(1,2,0,12)]]    
    ##
    k=10 ##Tiempo que se quiere optimizar 
    aptitud = fitness(ex,k)
    #fitness(ex,k)
    print("la aptitud es de :",aptitud)

main()
    