# Project Documentation

This project consists of multiple components that work together to implement a board game simulation. Below is an overview of the components and instructions on how to run the code.

## Components Overview

- `Client.py`: This script acts as the client interface for interacting with the game. It sends requests to the game engine and displays responses to the user.
- `game_library.py`: Contains the definitions of core classes such as `Tile`, `Hotel`, and `Board`. These classes are fundamental to the game's operation, representing the game board, tiles, and hotels.
- `game_impl.py`: Implements the game logic, including the initialization of the game state, processing player actions, and managing the game's rules.
- `Interface.py`: Located in the `Administrator` folder, this script provides an interface for administrative tasks and advanced game interactions.
- `request.json`: A sample JSON file that contains a request format for interacting with the game. It can be used to test the game's functionality through the client.

## Directory Structure

```plaintext
.
├── Administrator/
│   └── Interface.py
├── Client.py
├── game_impl.py
├── game_library.py
└── request.json
```

## Running the Code

1. **Starting the Game**: Ensure that Python 3.x is installed on your system.
2. **Client Interface**: Run `Client.py` to start interacting with the game. This script sends requests to the game engine and displays the game's state.
   ```shell
   python Client.py
   ```
3. **Administrative Interface**: To access administrative features or advanced game settings, navigate to the `Administrator` folder and run `Interface.py`.
   ```shell
   cd Administrator
   python Interface.py
   ```
4. **Custom Requests**: You can modify `request.json` to send custom game actions through the client interface. This file should contain valid JSON corresponding to the game's API.

5. **Testing**: The test input and expected output json files are placed inside `Project04/board-tester/board-tests` directory. In order to run a test, navigate to the project directory and run the command `pytest test_N.py` where N is the test sequence number. All the testing scripts are place at the root directory level.
