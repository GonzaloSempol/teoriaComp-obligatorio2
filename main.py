class nodo:
    def __init__(self, nodo): #un nodo puede ser cualquier objeto, pero debe tener un atributo key enumerable
        self.nodo = nodo;
        self.adyacencias = set() #set de nodos, O(1) de insercion y busqueda
    
    def getKey(self): #El objeto debe tener un atributo key
        return self.nodo.get('key')
    
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
        

    

miGrafo = grafo()
nodo1 = nodo({'objetito': 'algo', 'key':'nodo1'})
nodo2 = nodo({'objetito': 'otra cosa', 'key':'nodo2'})
nodo3 = nodo({'objetito': 'otra cosa 2', 'key':'nodo3'})


miGrafo.insertarNodo(nodo1)
miGrafo.insertarNodo(nodo2)
miGrafo.insertarNodo(nodo3)
miGrafo.insertarArista('nodo1','nodo2')
miGrafo.insertarArista('nodo2','nodo3')

print('GRAFO:')
print(miGrafo.grafo)
print('pruebo traer nodo1 by key')
print((miGrafo.getNodoByKey('nodo1')).getKey())
print('pruebo traer nodo2 by key')
print((miGrafo.getNodoByKey('nodo2')).getKey())
print('ady nodo1:')
nodo1.printAdyacenciasByKey()
print('ady nodo2:')
nodo2.printAdyacenciasByKey()
print('ady nodo3:')
nodo3.printAdyacenciasByKey()





