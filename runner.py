from pickle import TRUE
import sys
import time

import tictactoe as ttt

user = None
board = ttt.initial_state()

print()
print()
print("Tic Tac Toe")
print()

def printBoard():
  for i in range(3):
      output = ""
      for j in range(3):
        output += board[i][j] if board[i][j] else " "
        if j < 2:
          output += "|"
      print(output)
      if i < 2:
        print("-----")
  print()

printBoard()
while True:
  # Let user choose a player.
  if user is None:
    # Check if button is clicked
      choice = input("Play as x or o: ").lower()
      print()
      if choice == "x":
        time.sleep(0.2)
        user = ttt.X
      else:
        time.sleep(0.2)
        user = ttt.O

  else:
    game_over = ttt.terminal(board)
    player = ttt.player(board)
      
    # Check for AI move
    if user != player and not game_over:
      print("Computer thinking...")
      time.sleep(0.5)
      move = ttt.minimax(board)
      board = ttt.result(board, move)

    # Check for a user move
    if user == player and not game_over:
      print(f"Play as {user}:")
      working = True;
      while(working):
        x = input("Enter column number (0-2): ")
        y = input("Enter row number (0-2): ")
        if x.isnumeric() and y.isnumeric():
          x = int(x)
          y = int(y)
          if x < 3 and x >= 0 and y < 3 and y >= 0 and board[y][x] == ttt.EMPTY:
            board = ttt.result(board, (y, x))
            working = False

    printBoard()

    if game_over:
      winner = ttt.winner(board)
      if winner is None:
        print("Game Over: Tie.")
      else:
        print(f"Game Over: {winner} wins.")
      print()
      if input("Play again (y/n): ") == "y":
        time.sleep(0.2)
        user = None
        board = ttt.initial_state()
      else:
        break

print("Good bye")
