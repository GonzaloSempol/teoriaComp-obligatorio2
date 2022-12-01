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
    def dfs(self, keyNodoV): 
        resultado = []
        vInicial=self.getNodoByKey(keyNodoV); #Buscamos el nodo inicial       
        if vInicial is not None : #Si existe el nodo inicial
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

    #Implementación de dfs iterativa
    def bfs(self, keyNodoV): 
        resultado = []
        vInicial=self.getNodoByKey(keyNodoV); #Buscamos el nodo inicial       
        if vInicial is not None : #Si existe el nodo inicial
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
        

    

miGrafo = grafo()
nodo0 = nodo({'objetito': 'algo', 'key':'0'})
print(nodo0)
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
print('pruebo traer nodo1 by key')
print((miGrafo.getNodoByKey('1')).getKey())
print('pruebo traer nodo2 by key')
print((miGrafo.getNodoByKey('2')).getKey())
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





