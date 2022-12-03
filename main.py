from grafo import grafo
from nodo import  nodo

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
print('Camino mas corto 0-9')
print(miGrafo.camino_mas_corto('0','9'))
print('Largo Camino mas corto 0-9')
print(miGrafo.largo_camino_mas_corto('0','9'))
print('[0, 4] es mas corto?')
print(miGrafo.verificar_camino_mas_corto(['0','7','6','4']))







#Agregar casos de prueba
#Crear una lista, no se chequea de buena manera que los dos nodos existan