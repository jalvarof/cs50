# py para probar las funciones de tictactoe.py

from tictactoe import *

board = initial_state()

print(board)

print('Turno de ' + player(board))

print(winner(board))

available_actions = actions(board)

print( available_actions )

print('Acciones disponibles = ', str(len(available_actions)))

board[1][1] = X     # 1st action
board[1][0] = O     # best action
board[2][2] = X     # best action
board[0][2] = O     # best action
board[2][0] = X     # best action
board[0][0] = O     # best action
# board[2][1] = X     # best action   wins!! :)

print(board)

print('Turno de ' + player(board))

available_actions = actions(board)

print( available_actions )

print('Acciones disponibles = ', str(len(available_actions)))

for action in available_actions:
    print('Accion actual: ' + str(action))
    resboard = result(board,action)
    print(resboard)
    print(utility(resboard))

nextaction = minimax(board)
print('Best action = ', str(nextaction))
resboard = result(board,nextaction)
print(resboard)
print(utility(resboard))
