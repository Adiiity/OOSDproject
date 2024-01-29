import json
from typing import Dict
# from labeled_graph_manager import graph_manager_impl
from graph_manager_impl import LabeledGraphManager

# from project02.Interface import LabeledGraphManager

class GraphClient:
    def __init__(self, graph_manager: LabeledGraphManager):
        self.graph_manager = graph_manager

    def reading_file(self, file_path: str) -> None:
        with open(file_path, 'r') as file:
            commands = json.load(file)
        for command in commands:
            self.tag_command(command)

    def tag_command(self, command: Dict) -> None:
        tag = command.get("tag")
        if tag == "graph":
            self.graph_command(command)
        elif tag == "join":
            self.join_command(command)
        elif tag == "path":
            self.path_command(command)

    def graph_command(self, command: Dict) -> None:
        graphName = command.get("name")
        edges = command.get("edges", [])
        try:
            self.graph_manager.createGraph(graphName, edges)
        except ValueError as e:
            print({"error": str(e)})

    def join_command(self, command: Dict) -> None:
        addGraph = command.get("add")
        toGraph = command.get("to")
        try:
            self.graph_manager.mergeGraphs(addGraph, toGraph)
        except ValueError as e:
            print({"error": str(e)})

    def path_command(self, command: Dict) -> None:
        source_node = command.get("from")
        target_node = command.get("to")
        try:
            path_descriptions = self.graph_manager.ifFindPath(source_node, target_node, self.graph_manager.graphs)
            if path_descriptions:
                print({"tag": "paths", "paths": path_descriptions})
            else:
                print({"error": "No path found"})
        except ValueError as e:
            print({"error": str(e)})

# Instantiate LabeledGraphManager
graph_manager = LabeledGraphManager()

# Instantiate GraphClient with the graph manager
client = GraphClient(graph_manager)

# Path to the demo.json file
file_path = "demo.json"

# Read and process the file
client.reading_file(file_path)








