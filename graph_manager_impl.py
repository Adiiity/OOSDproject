# from project02.labeled_graph_manager import LabeledGraphManager

from labeled_graph_manager import LabeledGraphManager


class LabeledGraphManager:
    def __init__(self):
        # A dictionary to store multiple graphs, each identified by a unique name
        self.graphs = {}

    def createGraph(self, graphName: str, edgesList: []):
        # Ensure a new graph is created or an existing graph is fetched based on the graphName
        if graphName not in self.graphs:
            self.graphs[graphName] = {}
        self.graph = self.graphs[graphName]

        try:
            for edge in edgesList:
                node_1 = edge["from"]
                print(node_1)
                self.createNode(node_1)
                node_2 = edge["to"]
                print(node_2)
                self.createNode(node_2)
                self.connectNodes(node_1, node_2, edge["cost"])
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


    def mergeGraphs(self, graphName1: str, graphName2: str):
        try:
            if graphName1 not in self.graphs or graphName2 not in self.graphs:
                raise ValueError("Both graph names must exist.")

            graph1 = self.graphs[graphName1]
            # print(graph1)
            graph2 = self.graphs[graphName2]

            # Check if the graphs have disjoint sets of nodes
            common_nodes = set(graph1.keys()) & set(graph2.keys())
            if common_nodes:
                raise ValueError("Both graphs should have disjoint sets of nodes.")

            # Calculate total cost for each graph
            total_cost_graph1 = sum(cost for neighbors in graph1.values() for _, cost in neighbors)
            total_cost_graph2 = sum(cost for neighbors in graph2.values() for _, cost in neighbors)

            # Check if total costs are in the same interval
            if total_cost_graph1 > total_cost_graph2:
                raise ValueError("Total cost of edges in graph1 should be in the same cost interval as graph 2.")

            # Merge the graphs
            for node, neighbors in graph1.items():
                if node not in graph2:
                    graph2[node] = []
                for neighbor, cost in neighbors:
                    graph2[node].append([neighbor, cost])

            # Update the merged graph in the graphs dictionary
            self.graphs[graphName2] = graph2
            print("Merged")
            return graph2
        except Exception as errorMSG:
            print(errorMSG)


    def ifFindPath(self, sourceNode: str, targetNode: str, adjList: {}):

        allPaths = []
        currentPath = []

        self.dfs(sourceNode,targetNode, currentPath,allPaths,adjList)
        print(allPaths)
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

