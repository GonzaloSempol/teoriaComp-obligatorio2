class nodo:
    def __init__(self, nodo): #un nodo puede ser cualquier objeto, pero debe tener un atributo key enumerable
        self.nodo = nodo
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