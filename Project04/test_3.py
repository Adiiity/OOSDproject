import json
from Client import read_json_file
from Client import process_request
def test_3():
    # input file
    input_json = read_json_file('board-tester/board-tests/in3.json')
    input_data= process_request(input_json)
    # expect output
    with open('board-tester/board-tests/out3.json','r') as file:
        expected_output = json.load(file)


    assert json.loads(input_data )== expected_output

    

    