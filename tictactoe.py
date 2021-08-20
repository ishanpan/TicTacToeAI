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
    x = 0
    o = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x=x+1
            elif board[i][j] == O:
                o=o+1
    if x>o:
        return O
    elif o>x:
        return X
    elif x==o:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    legal_moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                legal_moves.add((i,j))
    
    return legal_moves
            
    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Raise exception if index out of range or cell is already taken
    if action[0] not in range(0, 3) or action[1] not in range(0, 3) or board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid move")

    # Let player whose turn it is to make their move on the board
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board

    



    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                winner=winner+1
            elif board[i][j] == O:
                winner=winner-1
        
        if winner == 3:
            return X
        elif winner == -3:
            return O
        else:
            winner = 0
    
    for j in range(3):
        for i in range(3):
            if board[i][j] == 'X':
                winner=winner+1
            elif board[i][j] == 'O':
                winner=winner-1
        
        if winner == 3:
            return X
        elif winner == -3:
            return O
        else:
            winner = 0
        
    if (board[0][0]==board[1][1]==board[2][2]==X):
         return X
    elif (board[0][0]==board[1][1]==board[2][2]==O):
        return O

    if (board[0][2]==board[1][1]==board[2][0]==X):
         return X
    elif (board[0][2]==board[1][1]==board[2][0]==O):
        return O

    
    return None
    
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if winner(board) != None:
        return True
    
    # All cells were filled
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True





def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winnerg = winner(board)

    if winnerg == X:
        return 1
    elif winnerg == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board):
        return None

    if player(board) == X:
        bestMove = -math.inf
        
        
        for move in actions(board):
            valueProducedByMoveMax = mini(result(board,move))

            if valueProducedByMoveMax > bestMove:
                bestMove = valueProducedByMoveMax
                action = move
        

    
    elif player(board) == O:
        bestMove = math.inf
    
        
        for move in actions(board):
            valueProducedByMoveMini = maxi(result(board,move))
            
            if valueProducedByMoveMini < bestMove:
                bestMove = valueProducedByMoveMini
                action = move

        
    return action



def mini(board):

    if terminal(board):
        return utility(board)

    v = math.inf
    for move in actions(board):
        v = min(v, maxi(result(board,move)))
    return v

        


def maxi(board):
    
    if terminal(board):
        return utility(board)
    v = -math.inf
    for move in actions(board):
        v = max(v, mini(result(board,move)))
    
    return v



    

