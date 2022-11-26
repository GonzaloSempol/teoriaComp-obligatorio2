class nodo:
    nodo = {} 
    adyacencias = set() #set de nodos, O(1) de insercion y busqueda

    def __init__(self, nodo): #un nodo puede ser cualquier objeto, pero debe tener un atributo key enumerable
        self.nodo = nodo;
    def getKey(self): #El objeto debe tener un atributo key
        return self.nodo.get('key')
    def insertarAdyacencia(self, nodoDest):
        self.adyacencias.add(nodoDest)
    def getAdyacencias(self):
        return self.adyacencias


class grafo:
    grafo = {} #O(1) de insercion y busqueda
    def insertarNodo(self,nodo):
        self.grafo.update({nodo.getKey():nodo})
    def getNodoByKey(self, keyNodo):
        return self.grafo.get(keyNodo)
    def insertarArista(self, keyNodoOrigen, keyNodoDestino):
        nodoOrigen = (self.getNodoByKey(keyNodoOrigen))
        print('nodo origen')
        print(nodoOrigen)
        nodoDestino = (self.getNodoByKey(keyNodoDestino))
        print('nodo destino')
        print(nodoDestino)
        nodoOrigen.insertarAdyacencia(nodoDestino)
        nodoDestino.insertarAdyacencia(nodoOrigen)

    

miGrafo = grafo()
nodo1 = nodo({'objetito': 'algo', 'key':'pepe'})
nodo2 = nodo({'objetito': 'otra cosa', 'key':'pepe2'})
nodo3 = nodo({'objetito': 'otra cosa 2', 'key':'pepe3'})


miGrafo.insertarNodo(nodo1)
miGrafo.insertarNodo(nodo2)
miGrafo.insertarNodo(nodo3)
miGrafo.insertarArista('pepe','pepe2')
miGrafo.insertarArista(nodo2.getKey(),nodo3.getKey())

print('GRAFO:')
print(miGrafo.grafo)
print((miGrafo.getNodoByKey('pepe')).getKey())
print((miGrafo.getNodoByKey('pepe2')).getKey())

adyacencias = miGrafo.getNodoByKey('pepe').getAdyacencias()
print(adyacencias)
adybykey = map(lambda x: (x.getKey()) ,(adyacencias))
print('ady de pepe')
list(map(print,adybykey))

