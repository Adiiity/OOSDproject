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

                    # elif graph_description["tag"] == "path":
                    #     print("the command to be executed is create graph")

                except Exception as errorMSG:
                    print(errorMSG)
        



# run the code
def main():
    # Create a Client instance
    client_instance = Client()

    # Execute commands based on the initialized graph
    client_instance.execute_commands([{ "tag" : "graph", "name" : "G1", "edges" : [{ "from" : "A", "to" : "B" , "cost" : 1 },{ "from" : "A", "to" : "C" , "cost" : 2 }, { "from" : "B", "to" : "C" , "cost" : 3 }] },
{ "tag" : "graph", "name" : "G2", "edges" : [{ "from" : "A", "to" : "B" , "cost" : 1 },{ "from" : "A", "to" : "C" , "cost" : 2 }, { "from" : "B", "to" : "C" , "cost" : 3 }] }])
    # client_instance.execute_commands({ "tag" : "graph", "name" : "G1", "edges" : [{ "from" : "A", "to" : "B" , "cost" : 1 },{ "from" : "A", "to" : "C" , "cost" : 2 }, { "from" : "B", "to" : "C" , "cost" : 3 }] })
    
if __name__ == "__main__":
    main()


# [{ "tag" : "graph", "name" : "G1", "edges" : [{ "from" : "A", "to" : "B" , "cost" : 1 },{ "from" : "A", "to" : "C" , "cost" : 2 }, { "from" : "B", "to" : "C" , "cost" : 3 }] },
# { "tag" : "graph", "name" : "G1", "edges" : [{ "from" : "A", "to" : "B" , "cost" : 1 },{ "from" : "A", "to" : "C" , "cost" : 2 }, { "from" : "B", "to" : "C" , "cost" : 3 }] }]