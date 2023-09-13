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
    rows = len(board)
    cols = len(board[0])
    numX = 0
    numO = 0

	# In the initial game state, X gets the first move. 
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == X:
                numX += 1
            elif board[i][j] == O:
                numO += 1
	
    if numX == numO:
        return X
    else:
        return O
	          				
	# Subsequently, the player alternates with each additional move.

    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()	 # empty set initialization

    rows = len(board)
    cols = len(board[0])

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == EMPTY:
                actions_set.add((i,j))
                
    return actions_set
	
    # raise NotImplementedError

class ActionError(Exception):
    pass
	
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_board = player(board)
    # print(player_board)
    # print(action)
    # print(isinstance(action,tuple))
    # print(len(action))
    # print(board[action[0]][action[1]])
    if not( isinstance(action,tuple) and len(action)==2 and board[action[0]][action[1]]==EMPTY ):
        raise ActionError("action format is not valid") 
        
    else:
        board_deepcopy = copy.deepcopy(board)
        board_deepcopy[action[0]][action[1]] = player_board
        return board_deepcopy
	
    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # se analiza solo el jugador que no es player(board)
    player_board = player(board)
    
    if player_board == X:
        player_win = O
    else:
        player_win = X
        
    rows = len(board)
    cols = len(board[0])
    numplayer_win = 0

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == player_win:
                numplayer_win += 1
	
    if numplayer_win < 3:
        return None
    else:
        # analizamos ahora las 3 filas, 
        # 3 columnas y 2 diagonales
        
        # DIAG 1
        sumd1 = 0
        for i in range(rows):
            if board[i][i] == player_win:
                sumd1 += 1
        if sumd1 == 3:
            return player_win
 
        # DIAG 2
        sumd2 = 0
        for i in range(rows):
            if board[i][cols-1-i] == player_win:
                sumd2 += 1
        if sumd2 == 3:
            return player_win

        # FILAS
        for i in range(rows):
            sumrow = 0
            for j in range(cols):
                if board[i][j] == player_win:
                    sumrow += 1
            if sumrow == 3:
                return player_win
        
        # COLUMNAS
        for j in range(cols):
            sumcol = 0
            for i in range(rows):
                if board[i][j] == player_win:
                    sumcol += 1
            if sumcol == 3:
                return player_win    
    
        return None
        
    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # game over because someone has won the game 
    # or because all cells are filled without anyone winning
    
    if winner(board) is not None:
        return True
    else:
        # find an empty cell in the board, if any, and exit
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == EMPTY:
                    return False
        
        return True

    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # assume utility will only be called on a board if terminal(board) is True 
    
    player_win = winner(board)
    if player_win == X:
        return 1
    elif player_win == 0:
        return -1
    else:
        return 0
        
    # raise NotImplementedError

# now we work this shit ...
def maxvalue(board):
    """Function Max-Value(state)
    v = -∞
    if Terminal(state):
    return Utility(state)
    for action in Actions(state):
    v = Max(v, Min-Value(Result(state, action)))
    """
    v = -1000
    if terminal(board):
        return utility(board)
    else:
        for action in actions(board):
            v = max(v, minvalue(result(board, action)))
        return v
    
def minvalue(board):
    """Function Max-Value(state)
    Function Min-Value(state):
    v = ∞
    if Terminal(state):
    return Utility(state)
    for action in Actions(state):
    v = Min(v, Max-Value(Result(state, action)))
    return v
    """
    v = 1000
    if terminal(board):
        return utility(board)
    else:
        for action in actions(board):
            v = min(v, maxvalue(result(board, action)))
        return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Given a state s 
    # The maximizing player picks action a in Actions(s) that produces the highest value of 
    # Min-Value(Result(s, a));
    # The minimizing player picks action a in Actions(s) that produces the lowest value of 
    # Max-Value(Result(s, a))
    
    player_board = player(board)
    if player_board == X:
        vmax = -1000
        for action in actions(board):
            v = minvalue(result(board, action))
            if v > vmax:
                actionmax = action
                v = vmax
        return actionmax
        
    else:
        vmin = 1000
        for action in actions(board):
            v = maxvalue(result(board, action))
            if v < vmin:
                actionmin = action
                v = vmin
        return actionmin
    
#    raise NotImplementedError
