# Connect4AI - Play Connect4 with a Minimax AI

This is a Connect4 game implementation where you can play against a computer that uses the minimax algorithm to choose its moves.

## How to Play

1. Clone the repository to your local machine.
2. Open a terminal window and navigate to the cloned repository.
3. Run `python3 main.py` to start the game.
4. Follow the prompts in the terminal to choose whether you want to play as Player 1 or Player 2, and to choose the depth of the minimax algorithm (i.e., the number of moves ahead the computer should consider).
5. Play the game by typing the column number (1-7) where you want to drop your piece.
6. The game ends when one player connects four pieces in a row, or the board is filled with no winner.

## How the Minimax AI Works

The minimax algorithm is a recursive algorithm that searches through the game tree to find the best move for the current player. Each node in the tree represents a possible game state, and the algorithm assigns a score to each node based on the value of the terminal node that it leads to (i.e., a win, loss, or draw).

The algorithm works as follows:

1. If the current node is a terminal node (i.e., the game has ended), return the score.
2. If the current node is a maximizing node (i.e., it is the computer's turn), return the maximum score of its child nodes.
3. If the current node is a minimizing node (i.e., it is the player's turn), return the minimum score of its child nodes.

By recursively applying this algorithm to each possible move, the computer can determine the best move to make based on the current state of the game.

## Contributors

- [Mehrab Hossain](https://github.com/m3hrab) - [Contributions](https://github.com/m3hrab/Connect4AI/commits?author=m3hrab)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
