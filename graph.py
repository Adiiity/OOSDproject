# { "tag" : "graph", "name" : "G1", "edges" : [{ "from" : "A", "to" : "B" , "cost" : 1 },{ "from" : "A", "to" : "C" , "cost" : 2 }, { "from" : "B", "to" : "C" , "cost" : 3 }] }
# { "tag" : "graph", "name" : "G2", "edges" : [{ "from" : "A", "to" : "B" , "cost" : 1 },{ "from" : "A", "to" : "C" , "cost" : 2 }, { "from" : "B", "to" : "C" , "cost" : 3 }] }
class LabeledGraphManager:
    def __init__(self):
        #  an list to store all the vertices of our current graph
        self.graph = {}
        
    def createGraph(self, edgesList: []) :
        # create labelled nodes 
        # create an edge between the nodes
        #  it take edgesList from the input
      try:      
        # we are extracting the edges data from edgeList.
        # print("Values of edgesList:", edgesList)
        for edge in edgesList:
        # create a node for from and to iteratively.
            node_1 = edge["from"]
            self.createNode(node_1)
            node_2 = edge["to"]
            self.createNode(node_2)
            # connect node_1 -> node_2 to nodes
            # CHECK FOR TRIANGLE INEQUALITY
            self.connectNodes(node_1,node_2,edge["cost"])
        return self.graph

      except Exception as errorMSG:
          print(errorMSG)
        
        
    
    def createNode(self, nodeLabel: str) -> None:
        # we create key for our node in the list and assign an empty list to hold neighbours 
        if nodeLabel not in self.graph:
            self.graph[nodeLabel] = []
            
            
    def connectNodes(self, sourceNode: str, targetNode: str, traversalCost: float) -> None:
        # get the neighbours list of current node from graph list
        sourceNode_neighbours = self.graph[sourceNode]
        # for each node -> the neighbour will be a pair of [label, weight]
        node_pair = [targetNode, traversalCost]
        sourceNode_neighbours.append(node_pair)
        # return self.graph

    # def ifFindPath(self,sourceNode, targetNode):
        