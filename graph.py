# from project02.Interface import LabeledGraphManager
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
        # detecting the triangle formation if the edge will be added
        for node in self.graph:
            if node != sourceNode and node != targetNode:
                if self.isNeighborOrNot(sourceNode, node) and self.isNeighborOrNot(node, targetNode):
                    cost1 = self.getEdgeCost(sourceNode, node)
                    cost2 = self.getEdgeCost(node, targetNode)
                    if not (cost1 + cost2 >= traversalCost and cost1 + traversalCost >= cost2 and cost2 + traversalCost >= cost1):
                        raise ValueError("Triangle inequality not satisfied")
                        # return

        # adding the edge when all three triangle inequality theorems are satisfied
        self.graph[sourceNode].append([targetNode, traversalCost])

    def isNeighborOrNot(self, node1: str, node2: str):
        return any(neighbor == node2 for neighbor, _ in self.graph[node1])

    def getEdgeCost(self, node1: str, node2: str):
        for neighbor, cost in self.graph.get(node1, []):
            if neighbor == node2:
                return cost
        # returns infinity if no direct edge exists
        return float('inf')


    def mergeGraphs(self, graph1: 'LabeledGraphManager', graph2: 'LabeledGraphManager'):
        try:
            # Check if the graphs have disjoint sets of nodes
            common_nodes = set(graph1.graph.keys()) & set(graph2.graph.keys())
            if common_nodes:
                raise ValueError("Both graphs should have disjoint sets of nodes.")

            # Check if the cost interval condition is satisfied
            total_cost_graph2 = 0
            for node_neighbors_graph2 in graph2.graph.values():
                for neighbor, cost in node_neighbors_graph2:
                    total_cost_graph2 += cost

            total_cost_graph1 = 0
            for node_neighbors_graph1 in graph1.graph.values():
                for neighbor, cost in node_neighbors_graph1:
                    total_cost_graph1 += cost

            if total_cost_graph1 > total_cost_graph2:
                raise ValueError("Total cost of edges in graph1 should be in the same cost interval as graph 2.")

            # Merge the graphs by updating graph2's adjacency list
            for node, neighbors in graph1.graph.items():
                graph2.createNode(node)
                for neighbor, cost in neighbors:
                    graph2.connectNodes(node, neighbor, cost)

            return graph2

        except Exception as errorMSG:
            print(errorMSG)

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