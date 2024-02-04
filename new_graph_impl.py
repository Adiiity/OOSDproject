from labeled_graph_manager import LabeledGraphManager


class LabeledGraphManager:
    def __init__(self):
        # a dictionary to store multiple graphs, each identified by a unique name
        self.graphs = {}

    def createGraph(self, graphName: str, low: str, high: str):
        low=float(low)
        high=float(high)

        # to check negative input
        if low < 0 or high < 0:
            return "Error: 'low' and 'high' values must be non-negative."

        if graphName not in self.graphs:
            self.graphs[graphName] = {"nodes": {}, "edges": [], "cost": (low, high)}
            return self.graphs[graphName]
        else:
            return "Graph already exists."

    def createNode(self, graphName: str, nodeLabel: str):
        if nodeLabel not in self.graphs[graphName]["nodes"]:
            self.graphs[graphName]["nodes"][nodeLabel] = []

    def connectNodes(self, graphName: str, sourceNode: str, targetNode: str, traversalCost: float) -> None:
        #checking if graph is there in the graphs
        graph = self.graphs.get(graphName)
        if not graph:
            print({"error": "Graph not found"})
            return

        # checking if both nodes exist in the graph
        if sourceNode not in graph["nodes"]:
            self.createNode(graphName, sourceNode)
        if targetNode not in graph["nodes"]:
            self.createNode(graphName, targetNode)

        # Triangle inequality check
        try:
            for node in graph["nodes"]:
                if node != sourceNode and node != targetNode and \
                   self.isNeighborOrNot(graphName, sourceNode, node) and self.isNeighborOrNot(graphName, node, targetNode):
                    cost1 = self.getEdgeCost(graphName, sourceNode, node)
                    cost2 = self.getEdgeCost(graphName, node, targetNode)
                    if not (cost1 + cost2 >= traversalCost and cost1 + traversalCost >= cost2 and cost2 + traversalCost >= cost1):
                        raise ValueError("Triangle inequality not satisfied")

            # add nodes and edges if triangle inequality is satisfied
            graph["nodes"][sourceNode].append((targetNode, traversalCost))
            edgeDescription = {"from": sourceNode, "to": targetNode, "cost": traversalCost}
            graph["edges"].append(edgeDescription)
            # print("Edge added successfully")
            # return graph
            return {"from": sourceNode, "to": targetNode, "cost": traversalCost}
        except ValueError as e:
            print({"error": e.args[0]})

    #checking common node to check triangle formation
    def isNeighborOrNot(self, graphName: str, node1: str, node2: str):
        graph = self.graphs.get(graphName)
        if not graph:
            return False
        for neighbor, _ in graph["nodes"].get(node1, []):
            if neighbor == node2:
                return True
        return False

    #function for getting edge cost that can help to check triangle inequality
    def getEdgeCost(self, graphName: str, node1: str, node2: str):
        graph = self.graphs.get(graphName)
        if not graph:
            return float('inf')
        for neighbor, cost in graph["nodes"].get(node1, []):
            if neighbor == node2:
                return cost
        return float('inf')

    def mergeGraphs(self, graphName1: str, graphName2: str):

        if graphName1 not in self.graphs or graphName2 not in self.graphs:
            return {"error": "Both graph names must exist."}

        graph1 = self.graphs[graphName1]
        print("graph 1: ",graph1)
        graph2 = self.graphs[graphName2]
        print("graph 2: ",graph2)


        # checking for disjoint node sets

        if not set(graph1["nodes"]).isdisjoint(graph2["nodes"]):
            return {"error": "Graphs must have disjoint sets of nodes."}

        # checking for same cost interval
        if not (graph1["cost"][0] <= graph2["cost"][1] and graph1["cost"][1] >= graph2["cost"][0]):
            return {"error": "Graph cost intervals are not same."}

        # Merge the graphs

        for node, neighbors in graph2["nodes"].items():
            graph1["nodes"][node] = neighbors
        graph1["edges"].extend(graph2["edges"])

        # update graph1 in graphs
        self.graphs[graphName1] = graph1
        print("After graph 1: ",graph1)

        # expected response format
        edges_description = [{"from": edge["from"], "to": edge["to"], "cost": edge["cost"]} for edge in graph1["edges"]]
        return {"low": graph1["cost"][0], "high": graph1["cost"][1], "edges": edges_description}

    #get nodes function for GET method
    def getNodes(self, graphName: str):
        nodes_list = []
        if graphName in self.graphs:
            for node in self.graphs[graphName]["nodes"]:
                nodes_list.append({"node": node})
            return nodes_list
        else:
            return {"error": "Graph not found"}

    #get edges function for GET method
    def getEdges(self, graphName: str):
        edges_list = []
        if graphName in self.graphs:
            print(self.graphs)
            print(graphName)
            for edge in self.graphs[graphName]["edges"]:
                # print("edge: ",edge)
                edges_list.append({"from": edge["from"], "to": edge["to"], "cost": edge["cost"]})

            return edges_list
        else:
            return {"error": "Graph not found"}

    def ifFindPath(self, sourceNode: str, targetNode: str, graphList: {}):
        allPathDescription = []

        for graph_name, graph_adj_list in graphList.items():
            if sourceNode in graph_adj_list and targetNode in graph_adj_list:
                allPaths = []
                currentPath = []
                self.dfs_helper(sourceNode, targetNode, currentPath, allPaths, graph_adj_list)

                for eachPath in allPaths:
                    eachPathDescription = []
                    for i in range(len(eachPath) - 1):
                        start, end = eachPath[i], eachPath[i+1]
                        for neighbor, cost in graph_adj_list[start]:
                            if neighbor == end:
                                edgeDescription = {"from": start, "to": end, "cost": cost}
                                eachPathDescription.append(edgeDescription)

                    allPathDescription.append(eachPathDescription)

        return allPathDescription

    def dfs_helper(self, sourceNode, targetNode, current_path, all_paths, current_adj_list):
        current_path.append(sourceNode)

        if sourceNode == targetNode:
            temp_path_list = list(current_path)
            all_paths.append(temp_path_list)
        else:
            for neighbour, _ in current_adj_list[sourceNode]:
                if neighbour not in current_path:
                    self.dfs_helper(neighbour, targetNode, current_path, all_paths, current_adj_list)

        current_path.pop()

# Initialize the graph manager
manager = LabeledGraphManager()

# Create two graphs with their cost intervals
manager.createGraph("Graph1", 1, 10)
# manager.createGraph("Graph2", 5, 15)

# Add nodes and edges to Graph1
manager.connectNodes("Graph1", "A", "B", 5)
manager.connectNodes("Graph1", "B", "C", 6)
manager.connectNodes("Graph1", "A", "C", 10)


# Add nodes and edges to Graph2 with disjoint nodes from Graph1
# manager.connectNodes("Graph2", "D", "E", 4)
# manager.connectNodes("Graph2", "E", "F", 5)

# Attempt to merge Graph2 into Graph1
# result = manager.mergeGraphs("Graph1", "Graph2")
# result=manager.graphs["Graph1"]
# print(result)
# print(manager.getNodes("Graph1"))
print(manager.getEdges("Graph1"))
