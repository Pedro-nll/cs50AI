"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    counter = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != EMPTY:
                counter += 1
    
    if counter % 2 == 0:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    ans = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                ans.add((i, j))
    return ans


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    valid_actions = actions(board)
    
    if action not in valid_actions:
        raise ValueError("Invalid action")
    
    next_player = player(board)
    
    board_copy = copy.deepcopy(board)
    
    board_copy[action[0]][action[1]] = next_player
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        # Check row
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        # Check column
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == "X":
        return 1
    elif win == "O":
        return -1
    return 0
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    play = player(board)
    
    if play == X:
        _, best_act = max_value(board)
    else:
        _, best_act = min_value(board)
    
    return best_act


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = 2
    best_act = None
    for a in actions(board):
        r, _ = max_value(result(board, a))
        if r < v:
            v = r
            best_act = a
    return v, best_act

def max_value(board):
    if terminal(board):
        return utility(board), None
    
    v = -2
    best_act = None
    for a in actions(board):
        r, _ = min_value(result(board, a))
        if r > v:
            v = r
            best_act = a
    return v, best_act