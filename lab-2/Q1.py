#Q1 Solution of Assignment 2
from matplotlib import pyplot as plt
class UndirectedGraph:
    def __init__(self, numberOFvertices = None):
        self.numberOFvertices= numberOFvertices
        self.adjucencyList={}
        #self.NumberOFedges=0P
#following below method is for counting the no.of edges,nodes and prnting a message about the graph
    def __str__(self):
        info=[] #to keep the message strings in the list
        count2=0  #counting the number of edges (2 times each as (a,b) and (b,a) are same)
        #following below loop is for counting the no.of edges
        for x in self.adjucencyList:  
            count2 = count2 + len(self.adjucencyList[x]) 
        num_of_edges = int(count2/2) #why?! ans : see the above comment
    #following below is for counting the number of nodes and printing details of graph

        #when no. of vertices is not given
        if self.numberOFvertices == None: #if no. of vertices is not given
            self.numberOFvertices = len(self.adjucencyList.keys()) #equating no. of vertices to no.of nodes
        #when no. of vertices is given, we have to add nodes(which are free) with empty adjucent node list
        else:
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
# following function is for ploting degree distribution of the graph        
    def plotDegDist(self):
        if self.numberOFvertices == None:
            self.numberOFvertices = len(self.adjucencyList.keys()) #equating no. of vertices with no. of nodes
        x=[] #intializing a empty list for x-axis values
        count_deg_occur=[] #for counting no. of vertices corresponding to each possible degrees
        for i in range(self.numberOFvertices):
            x.append(i)
            count_deg_occur.append(0) #initially setting 0 ccurance for each degree 
        #when no. of vertices given is given,adding nodes(which are free) with empty adjucent node list
        for i in range(self.numberOFvertices):
            if i not in self.adjucencyList.keys():
                self.adjucencyList[i]=[]                
        #foll: below counting no. of occurance of each possible degree                
        for i in self.adjucencyList.keys():
            #print(self.adjucencyList[i])
            for j in range(self.numberOFvertices):
                if len(self.adjucencyList[i]) == j:
                    count_deg_occur[j] += 1
       #creating y-values corresponding to x-values for ploting             
        y=[]            
        for i in range(self.numberOFvertices):
            y.append(count_deg_occur[i]/self.numberOFvertices) #y[i] is ''fraction of node'' for i-degree          
        #foll: below, calculating average node degree
        total_degree=0
        for i in self.adjucencyList.keys():
            total_degree = len(self.adjucencyList[i]) + total_degree
        avg_node_degree = total_degree/len(self.adjucencyList.keys())
        #ploting degree distribution og graph
        plt.title('Node degree distribution')
        plt.plot(x, y ,'bo', label='Actual degree distribution')
        plt.xlabel('Node degree')
        plt.ylabel('Fraction of node')
        plt.axvline(avg_node_degree , color='r', label='avg node degree')
        plt.grid()
        plt.legend()
        plt.show()
       
g = UndirectedGraph()
g = g + 10
g = g + (11, 12)
print(g)


