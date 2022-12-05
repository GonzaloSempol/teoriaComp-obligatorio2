from grafo import grafo
from nodo import  nodo




#Casos de prueba


###############################
#Grafo G1######################
###############################

G1 = grafo()
#Nodos
G1nodo0 = nodo({'objeto': 'algo', 'key':'0'})
G1nodo1 = nodo({'objetito': 'algo 2', 'key':'1'})
G1nodo2 = nodo({'objetito': 'otra cosa', 'key':'2'})
G1nodo3 = nodo({'objetito': 'otra cosa 2', 'key':'3'})
G1nodo4 = nodo({'key':'4'})
G1nodo5 = nodo({'key':'5'})
G1nodo6 = nodo({'key':'6'})
G1nodo7 = nodo({'key':'7'})
G1nodo8 = nodo({'key':'8'})
G1nodo9 = nodo({'key':'9'})
#Insertar nodos
G1.insertarNodo(G1nodo0)
G1.insertarNodo(G1nodo1)
G1.insertarNodo(G1nodo2)
G1.insertarNodo(G1nodo3)
G1.insertarNodo(G1nodo4)
G1.insertarNodo(G1nodo5)
G1.insertarNodo(G1nodo6)
G1.insertarNodo(G1nodo7)
G1.insertarNodo(G1nodo8)
G1.insertarNodo(G1nodo9)
#Aristas
G1.insertarArista('0','7')
G1.insertarArista('7','1')
G1.insertarArista('7','6')
G1.insertarArista('1','5')
G1.insertarArista('1','2')
G1.insertarArista('2','9')
G1.insertarArista('2','4')
G1.insertarArista('6','4')
G1.insertarArista('6','8')
G1.insertarArista('5','4')
G1.insertarArista('9','4')
G1.insertarArista('4','3')

#Casos de prueba grafo G1
print('GRAFO G1:')
G1.render("Grafo G1, cierre la ventana para continuar")

print('G1: DFS desde nodo  2:')
print(G1.dfs('2', True))
print('G1: Camino dfs desde nodo no existente 04:')
print(G1.dfs('04'))
print('G1: BFS desde nodo 2:')
print(G1.bfs('2', True))
print('G1: BFS desde nodo no existente 04:')
print(G1.bfs('04'))
print('G1: Componentes conexas')
print(G1.componentes_conexas())
print('G1: Cantidad Componentes conexas')
print(G1.cantidad_componentes_conexas())
print('G1: Es Conexo?')
print(G1.es_conexo())
print('G1: Camino mas corto 0-9')
print(G1.camino_mas_corto('0','9'))
print('G1: Largo Camino mas corto 0-9')
print(G1.largo_camino_mas_corto('0','9'))
print('G1: Camino [0,7,6,4] es mas corto?')
print(G1.verificar_camino_mas_corto(['0','7','6','4']))



###############################
#Grafo G2######################
###############################

G2 = grafo()
#Nodos
G2nodo0 = nodo({'otro objeto': 'algo', 'key':'0'})
G2nodo1 = nodo({'objetito 2': 'algo 2', 'key':'1'})
G2nodo2 = nodo({'objetito 3': 'otra cosa', 'key':'2'})
G2nodo3 = nodo({'objetito 4': 'otra cosa 2', 'key':'3'})
G2nodo4 = nodo({'key':'4'})
G2nodo5 = nodo({'key':'5'})
G2nodo6 = nodo({'key':'6'})
G2nodo7 = nodo({'key':'7'})
G2nodo8 = nodo({'key':'8'})
G2nodo9 = nodo({'key':'9'})
#Insertar nodos
G2.insertarNodo(G2nodo0)
G2.insertarNodo(G2nodo0)
G2.insertarNodo(G2nodo1)
G2.insertarNodo(G2nodo2)
G2.insertarNodo(G2nodo3)
G2.insertarNodo(G2nodo4)
G2.insertarNodo(G2nodo5)
G2.insertarNodo(G2nodo6)
G2.insertarNodo(G2nodo7)
G2.insertarNodo(G2nodo8)
G2.insertarNodo(G2nodo9)
#Aristas
G2.insertarArista('1','6')
G2.insertarArista('6','0')
G2.insertarArista('0','2')
G2.insertarArista('2','4')
G2.insertarArista('5','3')
G2.insertarArista('5','7')
G2.insertarArista('8','9')

print('GRAFO G2:')
G2.render("Grafo G2, cierre la ventana para continuar")
print("G2: BFS desde nodo 3:")
print(G2.bfs('0', True))
print("G2: DFS desde nodo 3:")
print(G2.dfs('0', True))
print("G2: Componentes conexas:")
print(G2.componentes_conexas())
print("G2: Cantidad Componentes conexas:")
print(G2.cantidad_componentes_conexas())
print("G2: Es conexo:")
print(G2.es_conexo())
print("G2: Largo camino mas corto 9-1:")
print(G2.largo_camino_mas_corto('9','1'))

###############################
#Grafo G3######################
###############################

G3 = grafo()
#Nodos
G3nodo0 = nodo({'otro objeto': 'algo', 'key':'0'})
G3nodo1 = nodo({'objetito 2': 'algo 2', 'key':'1'})
G3nodo2 = nodo({'objetito 3': 'otra cosa', 'key':'2'})
G3nodo3 = nodo({'objetito 4': 'otra cosa 2', 'key':'3'})
G3nodo4 = nodo({'key':'4'})
G3nodo5 = nodo({'key':'5'})
G3nodo6 = nodo({'key':'6'})
G3nodo7 = nodo({'key':'7'})
G3nodo8 = nodo({'key':'8'})
G3nodo9 = nodo({'key':'9'})
#Insertar nodos
G3.insertarNodo(G3nodo0)
G3.insertarNodo(G3nodo0)
G3.insertarNodo(G3nodo1)
G3.insertarNodo(G3nodo2)
G3.insertarNodo(G3nodo3)
G3.insertarNodo(G3nodo4)
G3.insertarNodo(G3nodo5)
G3.insertarNodo(G3nodo6)
G3.insertarNodo(G3nodo7)
G3.insertarNodo(G3nodo8)
G3.insertarNodo(G3nodo9)
#Aristas
G3.insertarArista('0','2')
G3.insertarArista('0','3')
G3.insertarArista('0','5')
G3.insertarArista('0','8')
G3.insertarArista('2','3')
G3.insertarArista('2','7')
G3.insertarArista('5','4')
G3.insertarArista('4','1')
G3.insertarArista('1','6')
G3.insertarArista('8','6')
G3.insertarArista('3','9')
G3.insertarArista('6','9')

print('GRAFO G3:')
G3.render("Grafo G3, cierre la ventana para continuar")
print("G3: BFS desde nodo 0:")
print(G3.bfs('0', True))
print("G3: DFS desde nodo 0:")
print(G3.dfs('0', True))
print("G3: Componentes conexas:")
print(G3.componentes_conexas())
print("G3: Cantidad Componentes conexas:")
print(G3.cantidad_componentes_conexas())
print("G3: Es conexo:")
print(G3.es_conexo())
print("G3: Largo camino mas corto:")
print(G3.largo_camino_mas_corto('4','3'))
print("G3: Camino mas corto 4-3:")
print(G3.camino_mas_corto('4','3'))
print("G3: Verificar camino mas corto ['4','5','0','3']:")
print(G3.verificar_camino_mas_corto(['4','5','0','3']))
print("G3: Verificar camino mas corto ['4','1','6','9','3']:")
print(G3.verificar_camino_mas_corto(['4','1','6','9','3']))

