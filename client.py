from graph import LabeledGraphManager
import json

class Client:

    def __init__(self):
        print("Client has started")
        # this is dict that holds all the graphs that belong to this client
        self.graphList = {}

    def execute_commands(self, input_graph):
        
                try:

                     #  Passing graph_description as input to the function parameters. Useful for testing
                    graph_description = input_graph
                    print(graph_description)
                    for command in graph_description:
                        tag = command["tag"]
                        print("Current TAG is :" , tag)
                        print("Current command description  is :" , command)

                        if tag == "graph":
                            print("\n COMMAND TO BE EXECUTED : ",tag)
                        
                            graph_name = command["name"]
                            if graph_name in self.graphList:
                                raise Exception(f"Graph with the name ", graph_name, " already exists.")
                            else:
                                # print("ELSE BLOCK")
                            #adding new graph name as key to graphList and an empty list to hold adj. list
                                self.graphList[graph_name] = []

                                # create a new object of class Graph
                                new_graph = LabeledGraphManager()
                                
                                # storing the result of createGraph in get_created_graph
                                get_created_graph = new_graph.createGraph(command["edges"])
                                # print(self.graphList)
                                # print(get_created_graph)
                                
                                # add this to the graph_name:[] in the overall dict
                                self.graphList[graph_name].append({"Adjacency List" : get_created_graph})
                                
                                print(self.graphList)
                                print()
                                print()
                                print()
                                print()
                    # elif graph_description["tag"] == "join":
                    #     print("the command to be executed is create graph")

                        elif tag == "path":
                            new_graph = LabeledGraphManager()
                            print("the command to be executed is path")
                            # print("executed")
                            # print(self.graphList)
                            sourceNode = command["from"]
                            
                            targetNode = command["to"]

                            pathsDescription=[]
                            for graph in self.graphList:
                                # print(self.graphList[graph])
                                # print(graph)
                                # print(sourceNode,targetNode)
                                for adjList in self.graphList[graph]:
                                    # print(graph,adjList)
                                    # print(graph, adjList["Adjacency List"])
                                    if sourceNode in adjList["Adjacency List"] and  targetNode in adjList["Adjacency List"] :
                                        # print(f"{sourceNode} is a key in the Adjacency List.")
                                        resultantEdgesPath = new_graph.ifFindPath(sourceNode,targetNode,adjList["Adjacency List"],graph)
                            # print( "result",result)     
                            for path in resultantEdgesPath:
                                individual_path = {"tag": "cost", "edges" : path}
                                pathsDescription.append(individual_path)
                            print("Path desc",pathsDescription)
                                
                                    
                                    


                except Exception as errorMSG:
                    print(errorMSG)
        



# run the code
def main():
    # Create a Client instance
    my_client = Client()

    # Execute commands based on the initialized graph
    my_client.execute_commands([
        { "tag" : "graph", "name" : "G1", "edges" : [{ "from" : "A", "to" : "B" , "cost" : 1 },{ "from" : "A", "to" : "C" , "cost" : 2 }, { "from" : "B", "to" : "C" , "cost" : 3 }] },
{"tag" : "path", "from" : "A", "to" : "C" },

])
    # client_instance.execute_commands({ "tag" : "graph", "name" : "G1", "edges" : [{ "from" : "A", "to" : "B" , "cost" : 1 },{ "from" : "A", "to" : "C" , "cost" : 2 }, { "from" : "B", "to" : "C" , "cost" : 3 }] })
    
if __name__ == "__main__":
    main()


# [{ "tag" : "path", [{ "from" : "A", "to" : "C" }] }
# { "tag" : "graph", "name" : "G1", "edges" : [{ "from" : "A", "to" : "B" , "cost" : 1 },{ "from" : "A", "to" : "C" , "cost" : 2 }, { "from" : "B", "to" : "C" , "cost" : 3 }] }]