import nodo
#Para Render
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random


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
    def dfs(self, keyNodoV, render=False, limpiarVisitados=True): 
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
                    if(render):
                        self.render("DFS (" + keyNodoV + "): "  + ','.join(map(str,resultado)),0.7, v.getKey())
                    resultado.append(v)
                for vAdy in (v.getAdyacencias()) :
                    if not vAdy.esVisitado() :
                        stack.insert(0, vAdy) #insertamos al comienzo
        if(render):
            self.render("DFS (" + keyNodoV + "): "  + ','.join(map(str,resultado)) + " Completo",2, v.getKey())
        return resultado

    #Implementación de bfs iterativa
    #limpiarVisitados indica si se debe recorrer la estructura del grafo para dejarlo como sin visitar
    #Tener la opcion de no hacerlo permite reutilizar bfs para hallar componentes conexas
    def bfs(self, keyNodoV, render=False, limpiarVisitados=True): 
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
                    if(render):
                        self.render("BFS (" + keyNodoV + "): "  + ','.join(map(str,resultado)),0.7, v.getKey())
                    resultado.append(v)
                for vAdy in (v.getAdyacencias()) :
                    if not vAdy.esVisitado() :
                        queue.append(vAdy) #insertamos al final

        if(render):
            self.render("BFS (" + keyNodoV + "): "  + ','.join(map(str,resultado)) + " Completo",2, v.getKey())     
        return resultado
    

    #Utilizamos bfs desde cada nodo, sin limpiar los nodos visitados para hallar una lista de componentes conexas
    def componentes_conexas(self):
        resultado=[]
        self.setearNodosSinVisitar() #limpiamos por unica vez los nodos, colocandolos sin visitar
        for key in self.grafo:
            #hacemos el bfs con la opcion de colocar los nodos sin visitar en False desde cada nodo 
            #y agregamos el cubrimiento resultante (componente conexa) a la lista de listas
            cubrimiento = self.bfs(key,False, False) 
            #Si no es vacio, lo agrego como otra comp conexa
            if cubrimiento != []:
                resultado.append(cubrimiento) 

        return resultado

    def cantidad_componentes_conexas(self):
        return len(self.componentes_conexas())

    def es_conexo(self):
        return self.cantidad_componentes_conexas() == 1
    
    def camino_mas_corto(self, keyNodoOrigen, keyNodoDestino):
        self.setearNodosSinVisitar()
        nodoOrigen = self.getNodoByKey(keyNodoOrigen)
        queueCaminos = [] #Lista de caminos recorridos hasta ahora
        queueCaminos.append([nodoOrigen])
        while(queueCaminos != []):
            caminoActual = (queueCaminos.copy().pop(0)) #Exploro el primer camino
            nodoActual = caminoActual.copy().pop() #El ultimo elemento, del 1er camino de la lista de caminos
            nodoActual.setVisitado() #lo visitamos
            for nAdy in nodoActual.getAdyacencias():
                if not nAdy.esVisitado():
                    nuevoCamino = caminoActual.copy()
                    nuevoCamino.append(nAdy)
                    queueCaminos.append(nuevoCamino)
                    if nAdy.getKey() == keyNodoDestino:
                        return nuevoCamino
            queueCaminos.pop(0)
        
        

        return [] #El camino no existe

    def largo_camino_mas_corto(self, keyNodoOrigen, keyNodoDestino):
        caminoMasCorto = self.camino_mas_corto(keyNodoOrigen, keyNodoDestino)
        if caminoMasCorto == []:
            return 0
        else:
            return len(caminoMasCorto) - 1
    
    
    def esCaminoValido(self, camino):
        if (camino == []):
            return False
        copiaCamino = camino.copy()
        keyNodoActual = copiaCamino.pop(0)
        while(copiaCamino != []):
            keyNodoSiguiente = copiaCamino.pop(0)
            nodoActual = self.getNodoByKey(keyNodoActual)
            nodoSiguiente = self.getNodoByKey(keyNodoSiguiente)
            if nodoSiguiente is None or nodoActual is None:
                return False
            listaAdyacencias = nodoActual.getAdyacencias()
            if nodoSiguiente not in listaAdyacencias:
                return False
            keyNodoActual = keyNodoSiguiente
        return True

    def verificar_camino_mas_corto(self, camino):
        if self.esCaminoValido(camino): #verificar que exista ese camino de A->B
            origen = camino.copy().pop(0)
            destino = camino.copy().pop()
            return (len(camino) -1) == self.largo_camino_mas_corto(origen, destino) #Retornamos True si su largo es optimo
        else:
            return False

    def render(self, titulo="",tiempo=0, nodoActual=[]):
        #Para que no sea distinto cada vez
        random.seed(10)
        np.random.seed(10)
        plt.clf()

        G=nx.Graph()
        nodosVisitados=[]
        nodosSinVisitar=[]
        for key in self.grafo:
            nodo=self.getNodoByKey(key)
            if nodo.esVisitado():
                if(nodoActual != nodo and nodoActual != []):
                    nodosVisitados.append(nodo.getKey())
            else:
                if(nodoActual != nodo and nodoActual != []):
                    nodosSinVisitar.append(nodo.getKey())
 
        G.add_nodes_from(self.grafo.keys())    

        for key in self.grafo.keys():
            nodo=self.getNodoByKey(key)
            for ady in nodo.getAdyacencias():
                G.add_edge(nodo.getKey(), ady.getKey())
           
        pos=nx.spring_layout(G)
        plt.title(titulo)
        nx.draw(G, pos,  with_labels=True, node_color='skyblue', nodelist=nodosVisitados, font_size=18, width=5, node_size=400)
        nx.draw(G, pos, with_labels=True, node_color='grey', nodelist=nodosSinVisitar, font_size=18, width=5, node_size=400)
        nx.draw(G, pos, with_labels=True, node_color='lightgreen', nodelist=nodoActual, font_size=18, width=5, node_size=400)
        if(tiempo > 0):
            plt.pause(tiempo)
        else:
            nx.draw(G, pos, with_labels=True, node_color='grey', font_size=18, width=5, node_size=400)
            plt.show()
        