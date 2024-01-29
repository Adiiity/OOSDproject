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


    def ifFindPath(self, sourceNode: str, targetNode: str, adjList: {}):

        allPaths = []
        currentPath = []

        self.dfs(sourceNode,targetNode, currentPath,allPaths,adjList)
        
        allPathDescription = []
        
        for eachPath in allPaths:
            
            eachPathDescription =[]

            iterable = 0
            start = eachPath[iterable]
            end = eachPath[iterable+1]
            
            while(iterable < len(eachPath)):
                for neighbours,cost in adjList[start]:
                    if neighbours == end:
                        edgeDescription ={"from" : start,"to": end,"cost": cost}
                        eachPathDescription.append(edgeDescription)
                nextStart = iterable+1
                nextEnd = iterable+2
                if nextStart < len(eachPath) and nextEnd < len(eachPath):
                    start = eachPath[iterable+1]
                    end = eachPath[iterable+2]
                    iterable+=1
                else:
                    break
            
            allPathDescription.append(eachPathDescription)
            
        return allPathDescription

        
    
    def dfs(self, sourceNode: str, targetNode: str, current_path: [], all_paths: [], adjacencyList: {} ):
        
        current_path.append(sourceNode)

        if sourceNode == targetNode:
            temp_path_list = list(current_path)

            all_paths.append(temp_path_list)
        else:
            for neighbour, traversalCost in adjacencyList[sourceNode]:
                self.dfs(neighbour, targetNode, current_path, all_paths, adjacencyList)

        current_path.pop()
