import json
from game_impl import Game

def validate_request(request_data):
    """Validate the incoming request data for required fields."""
    if 'request' not in request_data:
        raise ValueError("Missing 'request' field.")
    if request_data['request'] not in ['query', 'singleton', 'growing', 'founding', 'merging']:
        raise ValueError("Invalid 'request' field.")

    if request_data['request'] in ['singleton', 'growing', 'founding', 'merging']:
        if 'row' not in request_data or 'column' not in request_data:
            raise ValueError("Missing 'row' or 'column' field for this request type.")
    if request_data['request'] in ['growing', 'founding', 'merging']:
        if 'label' not in request_data:
            raise ValueError("Missing 'label' field for this request type.")

def process_request(json_request):
    try:
        request_data = json.loads(json_request)
        validate_request(request_data)

        game = Game(board_data=None)  # Adjust initialization as needed

        request_type = request_data['request']
        row = request_data.get('row')
        column = request_data.get('column')
        label = request_data.get('label')

        if request_type == "query":
            response = game.inspect(row, column)
        elif request_type == "singleton":
            response = game.singleton(row, column)
        elif request_type == "growing":
            response = game.growing(row, column, label)
        elif request_type == "founding":
            response = game.founding(row, column, label, game.board.board_matrix)  # Pass necessary params
        elif request_type == "merging":
            response = game.merging(row, column, label)
        else:
            raise ValueError("Unhandled request type.")

        return json.dumps({response})
    except Exception as e:
        return json.dumps({"error": str(e)})

def read_json_file(file_path):
    """Reads a JSON file and returns its content as a dictionary."""
    with open(file_path, 'r') as file:
        return file.read()

# Path to the JSON file
# file_path = '/request.json'

# Read and process the JSON request from file
json_request = read_json_file('/Users/aditithakkar/Desktop/personal_oosd/OOSDproject/Project04/request.json')
response = process_request(json_request)
print(response)

