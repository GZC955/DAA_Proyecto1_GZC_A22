from Node import *
from Edge import *

class Graph:

    def __init__(self,directed,autocycles,graph_name):
        '''
        directed: True or False about the graph's direction
        autocycles: True or False about the autocycles on the graph existence
        graph_name: Created Graph's name
        '''
        self.name = graph_name
        self.nodes = {}
        self.edges = {}
        self.directed = False
        self.autocycles = False
        self.visited = False
    
    def addNode (self,name):
        '''
        Adding a new node to the node's graph dictionary
        name: New node name
        '''
        node = self.nodes.get(name)

        if node is None: # Check if the node already exists
            node = Node(name)
            self.nodes[name] = node # Add a new node

        return node

    def addEdge(self,name,node0,node1,weight):
        '''
        Adding a new edge to the edge's graph dictionary
        name: Edge name
        node0: source node
        node1: target node
        weight: Edge weight value if it is necessary
        '''
        ed = self.edges.get(name)
        
        if ed is None: # Check if the edge already exists
            n0 = self.addNode(node0)
            n1 = self.addNode(node1)
            ed = Edge(name,n0,n1,weight) # Creaating the edge object
            self.edges[name] = ed # Adding values to the edge dictionary

            n0.neighbors.append(n1) # Adding to each node their respective neigbors and edges list
            n1.neighbors.append(n0)

            n0.edges.append(ed)
            n1.edges.append(ed)

        return ed

    def getNode(self,name):
        '''
        Getting the Node as an object not just the name
        name: Node's name
        '''
        return self.nodes.get(name)

    def getDegree(self,node):
        '''
        Evaluate the quantity of neighbors on an specific node in the graph
        node: Node of interest name
        '''
        n = self.getNode(node)
        if n is None:
            return 0
        
        return len(n.neighbors)

    def getRandEdge(self):
        '''
        Get a random edge on the graph
        '''
        return random.choice(list(self.edges.values()))

    def printNodes(self):
        '''
        Printing the Graph nodes in console to verify functionality
        '''
        n = self.nodes.items()
        print(n)

    def printEdges(self):
        '''
        Printing the Graph edges in console to verify functionality
        '''
        e = self.edges.items()
        print(e)
    
    def toGVFormat(self):
        '''
        Create the GV file to show results on Gephi
        '''
        val = 'digraph '+ str(self.name) + ' {\n'
        for i in self.nodes.values():
            val += str(i.id) + ';'
        for e in self.edges.values():
            n0 = e.n0.id
            n1 = e.n1.id
            val += n0 + ' -> ' + n1 + ';\n'
        val += '}\n'
        with open ("./Graphs_Data/" + self.name +".gv","w") as gv:
          gv.write(val) 
