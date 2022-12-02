import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

class nodo:
    def __init__(self, nodo): #un nodo puede ser cualquier objeto, pero debe tener un atributo key enumerable
        self.nodo = nodo;
        self.adyacencias = set() #set de nodos, O(1) de insercion y busqueda
        self.visitado=False #Atributo que se utiliza en algoritmos para controlar si un nodo fue visitado
    
    #Redefinimos el print para que muestre la clave al imprimir un nodo
    def __repr__(self):
        return self.getKey()     

    def getKey(self): #El objeto debe tener un atributo key
        return self.nodo.get('key')
    
    def setVisitado(self):
        self.visitado = True #setear visitado
    def setNoVisitado(self):
        self.visitado = False #setear no visitado
    def esVisitado(self):
        return self.visitado

    def insertarAdyacencia(self, nodoDest):
        self.adyacencias.add(nodoDest)
    
    def getAdyacencias(self):
        return self.adyacencias
    
    def printAdyacenciasByKey(self):     
        adybykey = map(lambda x: (x.getKey()), (self.adyacencias))
        list(map(print,adybykey))
    
    

class grafo:
    def __init__(self): 
        self.grafo = {} #O(1) de insercion y busqueda
    
    def insertarNodo(self,nodo):
        self.grafo[nodo.getKey()] = nodo
    
    def getNodoByKey(self, keyNodo):
        return self.grafo.get(keyNodo)
    
    def insertarArista(self, keyNodoOrigen, keyNodoDestino):
        nodoOrigen = (self.getNodoByKey(keyNodoOrigen))
        nodoDestino = (self.getNodoByKey(keyNodoDestino))
        nodoOrigen.insertarAdyacencia(nodoDestino)
        nodoDestino.insertarAdyacencia(nodoOrigen)
    
    def setearNodosSinVisitar(self):
        for key in self.grafo : #Para todas las keys
            self.getNodoByKey(key).setNoVisitado() #Obtengo el nodo y lo seteo sin visitar

    
    #Implementación de dfs iterativa
    #limpiarVisitados indica si se debe recorrer la estructura del grafo para dejarlo como sin visitar
    def dfs(self, keyNodoV, limpiarVisitados=True): 
        resultado = []
        vInicial=self.getNodoByKey(keyNodoV); #Buscamos el nodo inicial       
        if vInicial is not None : #Si existe el nodo inicial
            if limpiarVisitados:
                self.setearNodosSinVisitar(); #Seteamos todos los nodos como sin visitar
            stack = []
            stack.append(vInicial)
            while(stack != []):
                v=stack.pop(0)
                if not v.esVisitado() :
                    v.setVisitado()
                    resultado.append(v)
                for vAdy in (v.getAdyacencias()) :
                    if not vAdy.esVisitado() :
                        stack.insert(0, vAdy) #insertamos al comienzo
        
        return resultado

    #Implementación de bfs iterativa
    #limpiarVisitados indica si se debe recorrer la estructura del grafo para dejarlo como sin visitar
    #Tener la opcion de no hacerlo permite reutilizar bfs para hallar componentes conexas
    def bfs(self, keyNodoV, limpiarVisitados=True): 
        resultado = []
        vInicial=self.getNodoByKey(keyNodoV); #Buscamos el nodo inicial       
        if vInicial is not None : #Si existe el nodo inicial
            if limpiarVisitados:
                self.setearNodosSinVisitar(); #Seteamos todos los nodos como sin visitar
            queue = []
            queue.append(vInicial)
            while(queue != []):
                v=queue.pop(0)
                if not v.esVisitado() :
                    v.setVisitado()
                    resultado.append(v)
                for vAdy in (v.getAdyacencias()) :
                    if not vAdy.esVisitado() :
                        queue.append(vAdy) #insertamos al final
        
        return resultado

    #Utilizamos bfs desde cada nodo, sin limpiar los nodos visitados para hallar una lista de componentes conexas
    def componentes_conexas(self):
        resultado=[]
        self.setearNodosSinVisitar() #limpiamos por unica vez los nodos, colocandolos sin visitar
        for key in self.grafo:
            #hacemos el bfs con la opcion de colocar los nodos sin visitar en False desde cada nodo 
            #y agregamos el cubrimiento resultante (componente conexa) a la lista de listas
            cubrimiento = self.bfs(key,False) 
            #Si no es vacio, lo agrego como otra comp conexa
            if cubrimiento != []:
                resultado.append(cubrimiento) 

        return resultado

    def cantidad_componentes_conexas(self):
        return len(self.componentes_conexas())

    def es_conexo(self):
        return self.cantidad_componentes_conexas() == 1
    
    def render(self):
        #Para que no sea distinto cada vez
        random.seed(1)
        np.random.seed(1)

        G=nx.Graph()
        G.add_nodes_from(self.grafo.keys())
        aristas = set()
        for key in self.grafo.keys():
            nodo=self.getNodoByKey(key)
            for ady in nodo.getAdyacencias():
                G.add_edge(nodo.getKey(), ady.getKey())
        
        pos=nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color="skyblue", font_size=18, width=6, node_size=300)

    

miGrafo = grafo()
nodo0 = nodo({'objetito': 'algo', 'key':'0'})
nodo1 = nodo({'objetito': 'algo', 'key':'1'})
nodo2 = nodo({'objetito': 'otra cosa', 'key':'2'})
nodo3 = nodo({'objetito': 'otra cosa 2', 'key':'3'})
nodo4 = nodo({'key':'4'})
nodo5 = nodo({'key':'5'})
nodo6 = nodo({'key':'6'})
nodo7 = nodo({'key':'7'})
nodo8 = nodo({'key':'8'})
nodo9 = nodo({'key':'9'})

miGrafo.insertarNodo(nodo0)
miGrafo.insertarNodo(nodo1)
miGrafo.insertarNodo(nodo2)
miGrafo.insertarNodo(nodo3)
miGrafo.insertarNodo(nodo4)
miGrafo.insertarNodo(nodo5)
miGrafo.insertarNodo(nodo6)
miGrafo.insertarNodo(nodo7)
miGrafo.insertarNodo(nodo8)
miGrafo.insertarNodo(nodo9)

miGrafo.insertarArista('0','7')
miGrafo.insertarArista('7','1')
miGrafo.insertarArista('7','6')
miGrafo.insertarArista('1','5')
miGrafo.insertarArista('1','2')
miGrafo.insertarArista('2','9')
miGrafo.insertarArista('2','4')
miGrafo.insertarArista('6','4')
miGrafo.insertarArista('6','8')
miGrafo.insertarArista('5','4')
miGrafo.insertarArista('9','4')
miGrafo.insertarArista('4','3')

print('GRAFO:')
print(miGrafo.grafo)
print('ady nodo1:')
nodo1.printAdyacenciasByKey()
print('ady nodo2:')
nodo2.printAdyacenciasByKey()
print('ady nodo3:')
nodo3.printAdyacenciasByKey()

print('Camino dfs 2:')
print(miGrafo.dfs('2'))
print('Camino dfs 04:')
print(miGrafo.dfs('04'))
print('Camino bfs 2:')
print(miGrafo.bfs('2'))
print('Camino bfs 04:')
print(miGrafo.bfs('04'))


print('Componentes conexas')
print(miGrafo.componentes_conexas())
print('Cantidad Componentes conexas')
print(miGrafo.cantidad_componentes_conexas())
print('Es Conexo')
print(miGrafo.es_conexo())
miGrafo.render()
plt.show()




