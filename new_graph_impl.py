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
            # return {"error": "low and high values must be non-negative and non-zero."}

        if graphName not in self.graphs:
            self.graphs[graphName] = {"low": low, "high": high,"nodes": {}, "edges": []}

            response = jsonify({"low":self.graphs[graphName]["low"],"high":self.graphs[graphName]["high"],"edges":self.graphs[graphName]["edges"]})
            return response
            # return {"low":self.graphs[graphName]["low"],"high":self.graphs[graphName]["high"],"edges":self.graphs[graphName]["edges"]}
        else:
            error_response = {"error":"Graph already exists."}
            return jsonify(error_response)
            # return {"error":"Graph already exists."}

    def createNode(self, graphName: str, nodeLabel: str):
        if nodeLabel not in self.graphs[graphName]["nodes"]:
            self.graphs[graphName]["nodes"][nodeLabel] = []

    def connectNodes(self, graphName: str, sourceNode: str, targetNode: str, traversal_cost: float):
        graph = self.graphs.get(graphName)
        if not graph:
            return {"error": "Graph not found"}

        traversalCost = float(traversal_cost)
        #the new cost of new edge should be in cost interval
        if traversalCost < graph["low"] or traversalCost > graph["high"]:
            return {"error": "Edge weight should lie between the cost intervals."}

        #if node does not exist than should create
        if sourceNode not in graph["nodes"]:
            self.createNode(graphName, sourceNode)
        if targetNode not in graph["nodes"]:
            self.createNode(graphName, targetNode)

        #to check if edge exists already
        for neighbour, _ in graph["nodes"][sourceNode]:
            if neighbour == targetNode:
                return {"error": "Edge already exists."}

        triangle_detected = False
        for node in graph["nodes"]:
            # checking the common node in the triangle to detect triangle formation
            if node != sourceNode and node != targetNode:
                if (node in [neighbour for neighbour, _ in graph["nodes"].get(sourceNode, [])] or
                sourceNode in [neighbour for neighbour, _ in graph["nodes"].get(node, [])]) and \
               (node in [neighbour for neighbour, _ in graph["nodes"].get(targetNode, [])] or
                targetNode in [neighbour for neighbour, _ in graph["nodes"].get(node, [])]):

                # triangle detected, now checking triangle inequality
                    cost1 = self.getEdgeCost(graphName, sourceNode, node)
                    # print("cost1: ",cost1)
                    cost2 = self.getEdgeCost(graphName, node, targetNode)
                    # print("cost2: ",cost2)

                    cost3 = traversalCost  # new cost to check the trioangle inequality
                    # print("cost3: ",cost3)

                    if cost1 + cost2 >= cost3 and cost1 + cost3 >= cost2 and cost2 + cost3 >= cost1:
                        triangle_detected = True
                        break
                    else:
                        # print("Triangle inequality not satisfied")
                        return {"error": "Triangle inequality not satisfied"}

        if not triangle_detected:
            # If no triangle is detected or triangle inequality is satisfied, add the edge
            graph["nodes"][sourceNode].append((targetNode, traversalCost))
            graph["edges"].append({"from": sourceNode, "to": targetNode, "cost": traversalCost})
            response = {"low":graph["low"],"high":graph["high"],"edges":graph["edges"]}
            return response


    def getEdgeCost(self, graphName: str, node1: str, node2: str):
        graph = self.graphs.get(graphName, {})
        #checking direct connection
        for neighbor, cost in graph["nodes"].get(node1, []):
            if neighbor == node2:
                return cost
        #checking reverse connection
        for neighbor, cost in graph["nodes"].get(node2, []):
            if neighbor == node1:
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

        #delete graph2
        del self.graphs[graphName2]

        # expected response format
        edges_description = [{"from": edge["from"], "to": edge["to"], "cost": str(edge["cost"])} for edge in graph1["edges"]]
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
                edges_list.append({"from": edge["from"], "to": edge["to"], "cost": str(edge["cost"])})

            return edges_list
        else:
            error_response = {"error": "Graph not found"}
            return jsonify(error_response)

    def ifFindPath(self,graphName: str, sourceNode: str, targetNode: str):
        allPathDescription = []
        # check if graphList has the searched graphName
        if graphName not in self.graphs:
            error_response = jsonify({"error" : "Graph not found."})
            return error_response
        # all the adj lists of the given graph
        graph_adj_list = self.graphs[graphName]["nodes"]
        # print("adj list = ",graph_adj_list)
        givenGraph = self.graphs[graphName]
        # a path exists only if both src and tgt are there in the adj list

        if not (sourceNode in graph_adj_list and targetNode in graph_adj_list):
            # error_response = jsonify({"error" : "The given nodes are not present in the given graph."})
            # return error_response
            return {"error" : "The given nodes are not present in the given graph."}

        # store all the path in a list and perform dfs
        allPaths = []
        currentPath = []
        self.dfs_helper(sourceNode, targetNode, currentPath, allPaths, graph_adj_list)

        # print("ALL POSSIBLE PATHS IN THE GRAPH", allPaths)

        # iterate through each path in all paths to get the edge desc
        for eachPath in allPaths:
                    pathDescription = []
                    for i in range(len(eachPath) - 1):
                        start, end = eachPath[i], eachPath[i+1]
                        for neighbor, cost in graph_adj_list[start]:
                            if neighbor == end:
                                edgeDescription = {"from": start, "to": end, "cost": str(cost)}
                                pathDescription.append(edgeDescription)
                    allPathDescription.append(pathDescription)
        # print("DETAILED ALL PATHS EDGE DESC:",allPathDescription)

        response = []
        # our allPathDescription is a list of dicts lists. We need to send only list of dicts
        for itemList in allPathDescription:
            for edgeDescription in itemList:
                response.append(edgeDescription)
        # print("RESPONSE ", response)
        return response

    def dfs_helper(self, sourceNode, targetNode, current_path, all_paths,adj_list):

        current_path.append(sourceNode)

        if sourceNode == targetNode:
            temp_path_list = list(current_path)
            all_paths.append(temp_path_list)
        else:
            for neighbour, _ in adj_list[sourceNode]:
                if neighbour not in current_path:
                    self.dfs_helper(neighbour, targetNode, current_path, all_paths, adj_list)

        current_path.pop()

# # Initialize the graph manager
# manager = LabeledGraphManager()

# # # Create two graphs with their cost intervals
# manager.createGraph("Graph1", 1, 10)
# # # manager.createGraph("Graph2", 5, 15)

# # # Add nodes and edges to Graph1
# manager.connectNodes("Graph1", "A", "B", 2)
# manager.connectNodes("Graph1", "B", "C", 3)
# manager.connectNodes("Graph1", "A", "C", 5)


# # Add nodes and edges to Graph2 with disjoint nodes from Graph1
# # manager.connectNodes("Graph2", "D", "E", 4)
# # manager.connectNodes("Graph2", "E", "F", 5)

# # Attempt to merge Graph2 into Graph1
# # result = manager.mergeGraphs("Graph1", "Graph2")
# result=manager.graphs["Graph1"]
# print(result)
# # print(manager.getNodes("Graph1"))
# print(manager.getEdges("Graph1"))
