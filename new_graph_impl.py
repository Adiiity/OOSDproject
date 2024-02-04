from labeled_graph_manager import LabeledGraphManager
from flask import jsonify


class LabeledGraphManager:
    def __init__(self):
        # a dictionary to store multiple graphs, each identified by a unique name
        self.graphs = {}

    def createGraph(self, graphName: str, low: str, high: str):

        low = float(low)
        high = float(high)
        # to check negative input
        if not (low > 0 and high >  0):
            error_response = {"error": "low and high values must be non-negative and non-zero."}
            return jsonify(error_response)

        if graphName not in self.graphs:
            self.graphs[graphName] = {"low": low, "high": high,"nodes": {}, "edges": []}
            
            response = jsonify({"low":self.graphs[graphName]["low"],"high":self.graphs[graphName]["high"],"edges":self.graphs[graphName]["edges"]})
            return response
        else:
            error_response = {"error":"Graph already exists."}
            return jsonify(error_response)

    def createNode(self, graphName: str, nodeLabel: str):
        if nodeLabel not in self.graphs[graphName]["nodes"]:
            self.graphs[graphName]["nodes"][nodeLabel] = []

    def connectNodes(self, graphName: str, sourceNode: str, targetNode: str, traversal_cost: str):
        #checking if graph is there in the graphs
        graph = self.graphs.get(graphName)
        # print("GRAPH",graph)
        
        
        if not graph:
            # print({"error": "Graph not found"})

            error_response = jsonify({"error": "Graph not found"}),404
            return error_response
        
        # validate edge cost with interval
        low_interval = float(graph["low"])
        high_interval = float(graph["high"])
        traversalCost = float(traversal_cost)
        if not  (traversalCost >= low_interval and traversalCost <= high_interval):
            error_response = {"error": "edge weight should lie between the cost intervals."}
            return jsonify(error_response)
        # checking if both nodes exist in the graph
        if sourceNode not in graph["nodes"]:
            self.createNode(graphName, sourceNode)
        if targetNode not in graph["nodes"]:
            self.createNode(graphName, targetNode)

        # check if there is already an edge between source and destination
        # print("GRAPH is", graph)

        neighbour_present = False
        for neighbour, _ in graph["nodes"][sourceNode]:
            if neighbour == targetNode:
                neighbour_present = True
                break
        
        if neighbour_present is True:
            error_response = {"error": "edge already exists."}
            return jsonify(error_response)
        
        # Triangle inequality check
        try:
            for node in graph["nodes"]:
                if node != sourceNode and node != targetNode and self.isNeighborOrNot(graphName, sourceNode, node) and self.isNeighborOrNot(graphName, node, targetNode):
                    cost1 = self.getEdgeCost(graphName, sourceNode, node)
                    cost2 = self.getEdgeCost(graphName, node, targetNode)
                    if not (cost1 + cost2 >= traversalCost and cost1 + traversalCost >= cost2 and cost2 + traversalCost >= cost1):
                        # print("Traingle failed")
                        error_response = {"error": "Triangle inequality not satisfied"}
                        return error_response

            # add nodes and edges if triangle inequality is satisfied
            graph["nodes"][sourceNode].append((targetNode, traversalCost))
            edgeDescription = {"from": sourceNode, "to": targetNode, "cost": traversalCost}
            graph["edges"].append(edgeDescription)
            # print("Edge added successfully")
            # return graph
            # return {"from": sourceNode, "to": targetNode, "cost": traversalCost}
            response = jsonify({"low":graph["low"],"high":graph["high"],"edges":graph["edges"]}),200
            return response
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
            error_response = {"error": "Graphs must have disjoint sets of nodes."}
            return jsonify(error_response)

        # checking for same cost interval
        if not (graph1["low"] <= graph2["high"] and graph1["high"] >= graph2["low"]):

            error_response = {"error": "Graph cost intervals are not same."}
            return jsonify(error_response)

        # Merge the graphs

        for node, neighbors in graph2["nodes"].items():
            graph1["nodes"][node] = neighbors
        graph1["edges"].extend(graph2["edges"])

        # update graph1 in graphs
        self.graphs[graphName1] = graph1
        print("After graph 1: ",graph1)

        # expected response format
        edges_description = [{"from": edge["from"], "to": edge["to"], "cost": edge["cost"]} for edge in graph1["edges"]]
        response = {"low": graph1["low"], "high": graph1["high"], "edges": edges_description}
        return jsonify(response)

    #get nodes function for GET method
    def getNodes(self, graphName: str):
        nodes_list = []
        if graphName in self.graphs:
            for node in self.graphs[graphName]["nodes"]:
                nodes_list.append({"node": node})
            response = nodes_list
            return response
        else:
            error_response = {"error": "Graph not found"}
            return jsonify(error_response)

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
            error_response = {"error": "Graph not found"}
            return jsonify(error_response)

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
# manager = LabeledGraphManager()

# # Create two graphs with their cost intervals
# manager.createGraph("Graph1", 1, 10)
# # manager.createGraph("Graph2", 5, 15)

# # Add nodes and edges to Graph1
# manager.connectNodes("Graph1", "A", "B", B)
# manager.connectNodes("Graph1", "B", "C", 9)
# manager.connectNodes("Graph1", "A", "C", 3)


# Add nodes and edges to Graph2 with disjoint nodes from Graph1
# manager.connectNodes("Graph2", "D", "E", 4)
# manager.connectNodes("Graph2", "E", "F", 5)

# Attempt to merge Graph2 into Graph1
# result = manager.mergeGraphs("Graph1", "Graph2")
# result=manager.graphs["Graph1"]
# print(result)
# print(manager.getNodes("Graph1"))
# print(manager.getEdges("Graph1"))
