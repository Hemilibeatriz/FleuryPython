# -*- coding: utf-8 -*-
"""Fleury.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12nlps5tJC3XYhx84bUBk0JZuerxqayfy
"""

from collections import defaultdict 

#Classe Grafo
class Graph: 

    def __init__(self,vertices): 
        self.V= vertices #No. de vertices 
        self.graph = defaultdict(list) # default dictionary para armazenar o grafo
        self.Time = 0

    # Adiciona aresta (não direcionada)
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        self.graph[v].append(u) 

    #Função para remover a aresta u-v do grafo
    def rmvEdge(self, u, v): 
        for index, key in enumerate(self.graph[u]): 
            if key == v: 
                self.graph[u].pop(index) 
        for index, key in enumerate(self.graph[v]): 
            if key == u: 
                self.graph[v].pop(index) 

  ### Importante - auxiliar para verificar pontes ###
  # Função baseada no DFS para contar os vértices alcançaveis por meio do vértice V.
    def DFSCount(self, v, visited): 
        count = 1
        visited[v] = True
        for i in self.graph[v]: 
            if visited[i] == False: 
                count = count + self.DFSCount(i, visited)        
        return count 

    # Função que verifica se a aresta u-v pode ser considerada uma aresta no Tour de Euler
    def isValidNextEdge(self, u, v): 
        # A aresta u-v é valida em um dos seguintes casos: 

        # 1) Se v é o único vértice adjacente a u
        if len(self.graph[u]) == 1: 
            return True
        else: 
            ''' 
            2) Caso existam múltiplos vértices adjacentes u-v
            verificar se não é uma ponte
                
      Para checarmos se é uma ponte: 

            2.a) contamos os vértices alcançaveis a partir de u'''  
            visited =[False]*(self.V) 
            count1 = self.DFSCount(u, visited) 

            '''2.b) Remove a aresta (u, v) e após remover verificamos a quantidade de vértices alcançaveis a partir de u novamente'''
            self.rmvEdge(u, v) 
            visited =[False]*(self.V) 
            count2 = self.DFSCount(u, visited) 

            #2.c) Retornamos a aresta ao grafo, pois ela só foi removida para verificar se formavam-se pontes
            self.addEdge(u,v) 

            # 2.d) Se count1 é maior que count2, então a aresta (u, v) é uma ponte e não pode ser removida retornando falso.
            return False if count1 > count2 else True


    # Printa o tour de Euler tour começando pelo vértice u 
    def printEulerUtil(self, u): 
        #Recorre para todos os vértices adjacentes a este vértice
        for v in self.graph[u]: 
            #Se a vertice u-v não for removida e for uma próxima borda válida
            if self.isValidNextEdge(u, v): 
                print("%d-%d " %(u,v)), 
                self.rmvEdge(u, v) 
                self.printEulerUtil(v) 


    
    '''The main function that print Eulerian Trail. It first finds an odd 
degree vertex (if there is any) and then calls printEulerUtil() 
to print the path '''
    def printEulerTour(self): 
        #encontre um vertice com grau impar 
        u = 0
        for i in range(self.V): 
            if len(self.graph[i]) %2 != 0 : 
                u = i 
                break
        # Imprimir tour começando do vértice ímpar 
        print ("\n") 
        self.printEulerUtil(u)

# Create a graph given in the above diagram 
g1 = Graph(4) 
g1.addEdge(0, 1) 
g1.addEdge(0, 2) 
g1.addEdge(1, 2) 
g1.addEdge(2, 3) 
g1.printEulerTour() 


g2 = Graph(3) 
g2.addEdge(0, 1) 
g2.addEdge(1, 2) 
g2.addEdge(2, 0) 
g2.printEulerTour() 

g3 = Graph (5) 
g3.addEdge(1, 0) 
g3.addEdge(0, 2) 
g3.addEdge(2, 1) 
g3.addEdge(0, 3) 
g3.addEdge(3, 4) 
g3.addEdge(3, 2) 
g3.addEdge(3, 1) 
g3.addEdge(2, 4) 
g3.printEulerTour()