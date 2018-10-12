import random
def player_turn(board_values, player_piece):
	no_replace = False
	while no_replace == False:
		player_input = input("Enter the coordinates of your move: ")
		try:
			if int(player_input[0]) > 3 or int(player_input[2]) > 3:
				print("Sorry, this number is out of range.")
			elif int(player_input[0]) < 1 or int(player_input[2]) < 1:
				print("Sorry, this number is out of range.")
			else:
				no_replace = True
		except:
			print("Sorry, this input doesn't have the numbers in the right place.")
	if board_values[int(player_input[0]) - 1][int(player_input[2]) - 1] != " ":
		print("Sorry, thats already taken. Try again!")
		player_go = False
		return player_go
	else:
		board_values[int(player_input[0]) - 1][int(player_input[2]) - 1] = player_piece
		no_replace = True
		player_go = True
		return player_go
def computer_turn(board_values, computer_piece):
	no_replace = False
	randnum1 = random.randint(0, 2)
	randnum2 = random.randint(0, 2)
	while no_replace == False:
		randindex = board_values[randnum1][randnum2]
		if randindex == " ":
			no_replace = True
			board_values[randnum1][randnum2] = computer_piece
		else:
			randnum1 = random.randint(0, 2)
			randnum2 = random.randint(0, 2)
def show_board(board_values):
	print(("{}|{}|{}\n-----\n{}|{}|{}\n-----\n{}|{}|{}").format(board_values[0][0], board_values[0][1], board_values[0][2], board_values[1][0], board_values[1][1], board_values[1][2], board_values[2][0], board_values[2][1], board_values[2][2]))
board_values = [
[" ", " ", " "],
[" ", " ", " "],
[" ", " ", " "]
]
lose = False
while True:
	player_piece = input("Enter X or O here to decide your piece: ")
	player_piece = player_piece.upper()
	if player_piece != 'X' and player_piece != 'O':
		print("Sorry, this is not an X or O. Try again.")
	else:
		break
if player_piece == 'X':
	computer_piece = 'O'
else:
	computer_piece = 'X'
while lose == False:
	player_go = True
	player_go = player_turn(board_values, player_piece)
	x_or_y = player_piece
	win = "Player wins!"
	for x in range(2):
		if board_values[0][0] == x_or_y and board_values[0][1] == x_or_y and board_values[0][2] == x_or_y:
			print(win)
			show_board(board_values)
			lose = True
			break
		if board_values[0][0] == x_or_y and board_values[1][0] == x_or_y and board_values[2][0] == x_or_y:
			print(win)
			show_board(board_values)
			lose = True
			break
		if board_values[0][0] == x_or_y and board_values[1][1] == x_or_y and board_values[2][2] == x_or_y:
			print(win)
			show_board(board_values)
			lose = True	
			break
		if board_values[0][2] == x_or_y and board_values[1][2] == x_or_y and board_values[2][2] == x_or_y:
			print(win)
			show_board(board_values)
			lose = True
			break
		if board_values[2][0] == x_or_y and board_values[2][1] == x_or_y and board_values[2][2] == x_or_y:
			print(win)
			show_board(board_values)
			lose = True
			break
		if board_values[2][0] == x_or_y and board_values[1][1] == x_or_y and board_values[0][2] == x_or_y:
			print(win)
			show_board(board_values)
			lose = True
			break
		if board_values[0][1] == x_or_y and board_values[1][1] == x_or_y and board_values[2][1] == x_or_y:	
			print(win)
			show_board(board_values)
			lose = True
			break
		if board_values[1][0] == x_or_y and board_values[1][1] == x_or_y and board_values[1][2] == x_or_y:
			print(win)
			show_board(board_values)
			lose = True	
			break
		x_or_y = computer_piece
		win = "Computer wins!"
	if (board_values[0][0] == 'X' or board_values[0][0] == 'O') and\
	  (board_values[0][1] == 'X' or board_values[0][1] == 'O') and\
	  (board_values[0][2] == 'X' or board_values[0][2] == 'O') and\
	  (board_values[1][0] == 'X' or board_values[1][0] == 'O') and\
	  (board_values[1][1] == 'X' or board_values[1][1] == 'O') and\
	  (board_values[1][2] == 'X' or board_values[1][2] == 'O') and\
	  (board_values[2][0] == 'X' or board_values[2][0] == 'O') and\
	  (board_values[2][1] == 'X' or board_values[2][1] == 'O') and\
	  (board_values[2][2] == 'X' or board_values[2][2] == 'O'):
		print("It's a draw!")
		show_board(board_values)
		break
	if player_go:		
		computer_turn(board_values, computer_piece)
	show_board(board_values)
	

