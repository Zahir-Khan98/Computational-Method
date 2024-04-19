#Q4 Solution of Assignment 2

from matplotlib import pyplot as plt
import random
class UndirectedGraph:
    def __init__(self, numberOFvertices = None):
        self.numberOFvertices= numberOFvertices
        self.adjucencyList={}
        #self.NumberOFedges=0
#following below method is for counting the no.of edges,nodes and prnting a message about the graph
    def __str__(self):
        info=[] #to keep the message strings in the list
        count2=0  #initializing with 0, for counting the number of edges (2 times each as (a,b) and (b,a) are same)
        #following below method is for counting the no.of edges
        for x in self.adjucencyList:  
            count2 = count2 + len(self.adjucencyList[x]) 
        num_of_edges = int(count2/2) #why?! ans : see the above comment
    #following below is for counting the number of nodes and printing details of graph
        #when no. of vertices is not given
        if self.numberOFvertices == None: #if no. of vertices is not given
            self.numberOFvertices = len(self.adjucencyList.keys()) #equating no. of vertices to no.of nodes
        #when no. of vertices given is given, we have to add nodes(which are free) with empty adjucent node list
        for i in range(1, self.numberOFvertices+1):
            if i not in self.adjucencyList.keys():
                self.adjucencyList[i]=[] 
        info.append("Graph with "  + str(self.numberOFvertices) + " nodes and " + str(num_of_edges) + 
                  " edges. Neighbours of nodes are below")
        for i in self.adjucencyList.keys():
            info.append("\n Node " +str(i) + ":" + str("{" + ", ".join([str(x) for x in self.adjucencyList[i]]) + "}"))
        return "\n".join(info) 

    def addNode(self, nodeIndex): #method for adding nodes
        self.nodeIndex = nodeIndex
        if self.numberOFvertices != None: #when number of vertices given
            #checking if no. of vertices is <= or not and node is 
            if nodeIndex <= self.numberOFvertices:
                if nodeIndex not in self.adjucencyList: 
                    self.adjucencyList[nodeIndex] = [] #assigning a empty list to that node for adjucent nodes
            else:
                try:
                    raise Exception('Node index cannot exceed number of nodes')
                except Exception as excptn:
                    print(type(excptn))
                    print(excptn)
        elif nodeIndex not in self.adjucencyList: # For a free graph 
            self.adjucencyList[nodeIndex] = [] #assigning a empty list to that node for adjucent nodes
        return self
    def addEdge(self, u, v): #adding edges
        #if self.numberOFvertices == None: #when no. of vertices is not given
            #assigning a empty list to those nodes for adjucent nodes
        self.addNode(u)
        self.addNode(v)
            
            #adding adjucent nodes (dictionary values)
        self.adjucencyList[u].append(v)
        self.adjucencyList[v].append(u)
       
        return self
    def __add__(self,component): #add operator function for adding node [g+10] and edges [g+(1,4)]
        if type(component) == int: #when adding node
            g.addNode(component)
        if type(component) == tuple: #when adding edge
            l=list(component)
            g.addEdge(l[0],l[1])
        return self  
    #foll: below we are generating random graph G(n,p)
class EERRandomGraph(UndirectedGraph):
    def __init__(self,numberOFvertices):
        self.vertices=numberOFvertices
        self.adjucencyList={}
        self.prob=0
        UndirectedGraph.__init__(self,self.vertices)
    def sample(self,prob):
        self.prob=prob
        for i in range(1,self.vertices+1):
            self.adjucencyList[i]=[] #creating empty adjucency edge list
        for i in range(1,self.vertices):
            for j in range(i+1,self.vertices+1):
                r =random.random() 
                if r <prob: 
         #our given prob: value is greater than a random prob: value , so we'll add the edge           
                    self.adjucencyList[i].append(j)
                    self.adjucencyList[j].append(i)
        return self

    def oneTwoComponentSizes(self):
        sets=[]
        #creating n (= number of verticees) empty sets for n vertices named "sets[0]",.."sets[n-1]"
        for i in range(self.numberOFvertices):
            sets.append(set())  
        for i in range(self.numberOFvertices):
            sets[i].add(i+1)   # adding element for each vertex to the corresponding set
                               #it will result " sets = [{1},{2},...,{n}]"
        for i in self.adjucencyList.keys():
            for x in self.adjucencyList[i]:
                sets[i-1].add(x) #adding adjucency vertices of vertex 'i' in set {i}
        for i in range(len(sets)):     
            for j in range(len(sets)):
                
                   #if in intersection of two set is non-empty, union them, because two
                 #sets are non empty means the vertices of those sets belongs to same component
                 
               if len(sets[i].intersection(sets[j])) != 0:
                   sets[i].update(sets[j])  #it work as "A.update(B)" > A=A U B.

        #foll: below we are finding length of two largest component
        
        length_set = set()  #to find length of each component and making a set named 'length_set'
        for i in range(len(sets)):
            l=len(sets[i]) 
            length_set.add(l)   
        two_largest_component_length_list=[] 
        firstMax=max(length_set)
        two_largest_component_length_list.append(firstMax)
        length_set.remove(firstMax)
        secondMax= max(length_set)
        two_largest_component_length_list.append(secondMax)
        return two_largest_component_length_list
'''     
g = UndirectedGraph(6)
g = g + (1, 2)
g = g + (3, 4)
g = g + (6, 4)
print(g.oneTwoComponentSizes())

'''
g = EERRandomGraph(100)
g.sample(0.01)
print(g.oneTwoComponentSizes())





