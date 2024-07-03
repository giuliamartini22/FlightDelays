from datetime import datetime

import networkx as nx

from model.model import Model

myModel = Model()
myModel.buildGraph(5)
myModel.printGraphDetails()

v0 = myModel.getAllNodes()[0]
connessa = list(nx.node_connected_component(myModel._grafo, v0))
v1 = connessa[10]

pathD = myModel.trovaCamminoDijkstra(v0,v1)
pathBFS = myModel.trovaCamminoBFS(v0, v1)
pathDFS = myModel.trovaCamminoDFS(v0, v1)

print("Metodo di dijkstra")
print(*pathD, sep='\n')
print("-----------------")
print("Metodo di BFS")
print(*pathBFS, sep='\n')
print("-----------------")
print("Metodo di DFS")
print(*pathDFS, sep='\n')

tic = datetime.now()
bestPath, bestScore = myModel.getCamminoOttimo(v0, v1, 5)
print("-----------------")
print(f"Cammino ottimo ha peso = {bestScore}")
print(*bestPath, sep='\n')