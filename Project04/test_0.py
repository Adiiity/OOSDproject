import json
from Client import read_json_file
from Client import process_request
def test_0():
    # input file
    input_json = read_json_file('board-tester/board-tests/in0.json')
    input_data= process_request(input_json)
    # expected output
    with open('board-tester/board-tests/out0.json','r') as file:
        expected_output = json.load(file)


    assert input_data == expected_output

    

    