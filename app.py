from flask import Flask, jsonify,request
from new_graph_impl import LabeledGraphManager

app=Flask(__name__)

manager=LabeledGraphManager()

@app.route('/new', methods=['POST'])
def create_graph():
    data=request.json
    graph_name=data['name']
    low=data['low']
    high=data['high']

    result=manager.createGraph(graph_name, low, high)

    # return jsonify({"message": "Graph created successfully"}),200
    print("result: ",result)
    return result

@app.route('/add', methods=['POST'] )
def connect_nodes():
    data=request.json
    graph_name = data['name']
    from_node = data['from']
    to_node = data['to']
    cost = data['cost']

    result=manager.connectNodes(graph_name,from_node,to_node,cost)
    print("result: ",result)
    # return jsonify({"message":"Added edge successfully"}),200
    return result

@app.route('/join',methods=['POST'])
def merge_graphs():
    data=request.json
    graph1,graph2=data
    result=manager.mergeGraphs(graph1,graph2)
    return result,200

@app.route('/nodes/<graph_name>', methods=['GET'])
def get_nodes(graph_name):
    # data=request.json
    nodes=manager.getNodes(graph_name)
    return nodes,200

@app.route('/edges/<graph_name>',methods=['GET'])
def get_edges(graph_name):
    # data=request.json
    nodes=manager.getEdges(graph_name)
    return jsonify(nodes),200

@app.route('/path/<graph_name>/<from_node>/<to_node>',methods=['GET'])
def get_path(graph_name,from_node,to_node):
    paths = manager.ifFindPath(graph_name,from_node,to_node)
    return jsonify(paths),200
    # data=request.json
    # nodes=manager.getEdges(graph_name)
    # return jsonify(nodes),200

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5020,debug=True)