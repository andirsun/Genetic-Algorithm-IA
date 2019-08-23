# Genetic-Algorithm-IA
Algoritmo genetico para la solucion de un problema de inteligencia artificial en python

Para la solucion del siguiente problema

Asignatura Sistemas Inteligentes
Representaci´on Mediante Grafos de Estados y
T´ecnica de B´usqueda
Agosto 14 de 2019
Este taller corresponde al 20% de la nota de la asignatura, se debe realizar de
forma individual. El archivo con la soluci´on del taller deber´a enviarse a la profesora por correo electr´onico a m´as tardar el jueves 22 de agosto, la sustentaci´on
ser´a el viernes 23 de agosto. El objetivo del taller es practicar:
• El dise˜no de agentes computacionales inteligentes
• La aplicaci´on de t´ecnicas de b´usqueda para controlar un agente inteligente
• La implementaci´on de algoritmos gen´eticos
1 Definici´on del problema
En una empresa de manufactura, han decido confiar a un agente inteligente la
programaci´on de la producci´on. Despu´es de analizar la naturaleza del proceso
productivo, se ha llegado a la siguiente definici´on del problema de optimizaci´on,
cuya soluci´on se quiere automatizar:
Sea J un conjunto de n trabajos y sea M un conjunto de m m´aquinas. Cada
trabajo i consiste de ni operaciones consecutivas, donde la j-esima operaci´on
del trabajo i, denotada Oij , puede ser procesada en cualquiera de las m´aquinas
pertenecientes al subconjunto Mij ⊆ M de m´aquinas elegibles.
Para cada operaci´on Oij , sea pijk su tiempo de procesamiento en la m´aquina
k ∈ Mij . El tiempo de puesta a punto de la m´aquina para iniciar cada tarea no
ser´a considerado en esta versi´on del problema.
Cada operaci´on debe completarse sin interrupci´on en la misma m´aquina
una vez inicia. Cada operaci´on se asigna a una s´ola m´aquina elegible. Las
m´aquinas no pueden realizar m´as de una operaci´on a la vez. Las operaciones que
componen un trabajo deben realizarse estrictamente en el orden establecido al
definir el trabajo. Todos los trabajos y m´aquinas est´an disponibles en el tiempo
1
cero. El problema consiste en asignar cada operaci´on a una m´aquina elegible, y
secuenciar las operaciones en las m´aquinas de manera que se minimice el tiempo
Cmax, requerido para terminar todos los trabajos.
2 Actividades a realizar
1. Caracterizar el agente computacional inteligente que va a resolver el problema.
2. Dibujar un esquema de la arquitectura del agente, la cual debe ser jer´arquica.
3. Especificar el flujo de datos entre capas y especificar m´odulos dentro de
cada capa. (Alguno de los m´odulos se encargar´a de hacer la asignaci´on de
operaciones a m´aquinas, este m´odulo deber´a ser un algoritmo gen´etico)
4. Identificar las consideraciones ´eticas que se tendr´an en cuenta en el dise˜no
del agente.
5. Dise˜nar el algoritmo gen´etico: definir la estructura del individuo, definir la
funci´on de aptitud (en ingl´es funci´on fitness), definir un plan para estimar
los par´ametros num´ericos, como n´umero de individuos por generaci´on,
n´umero de generaciones, probabilidad de mutaci´on. Para la estrategia de
cruce deber´an compararse el m´etodo de torneo y el de ruleta.
6. Implementar la soluci´on en un jupyter notebook, en python.
7. Analizar la calidad de las soluci´on obtenida por el algoritmo gen´etico.
3 Criterios de evaluaci´on
El informe del taller, que se debe incorporar en el mismo archivo de jupyter
notebook que el c´odigo, deber´a contener una corta introducci´on, los seis items
enumerados en la secci´on anterior, que corresponden a las actividades del taller,
una secci´on de conclusiones y finalmente la bibliograf´ıa que debe incluir no s´olo
los libros o art´ıculos consultados si no tambi´en las librer´as de software o funciones externas que se hayan usado en el c´odigo.
Criterios de evaluaci´on: Si se comprueba total dominio de la persona sobre
el dise˜no y la implementaci´on presentados se calificar´a seg´un los porcentajes
siguientes, pero si hay desconocimiento de la soluci´on por parte de quien la
presenta o indicios de que no es original, se solicitar´a el inicio de un proceso
disciplinario a la decanatura quien determinar´a la calificaci´on.
• Caracterizaci´on del agente y dise˜no de la arquitectura del agente (incluye
definici´on de flujos de datos y definici´on de m´odulos en cada capa): 10%
• Identificaci´on de las consideraciones ´eticas que se tendr´an en cuenta en el
dise˜no del agente. 15%
2
• Dise˜no del algoritmo gen´etico: 15%
• Implementaci´on del agente inteligente: 30%
• Evaluaci´on del desempe˜no del agente inteligente (incluye la evaluaci´on de
si se atendieron en la implementaci´on las consideraciones ´eticas identificadas en el dise˜no): 20%
• Informe y sustentaci´on: 10%
