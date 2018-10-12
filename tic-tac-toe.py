import random
def player_turn(board_values):
	no_replace = False
	while no_replace == False:
		player_input = input("Enter the coordinates of your move: ")
		if board_values[int(player_input[0]) - 1][int(player_input[2]) - 1] != " ":
			print("Sorry, thats already taken. Try again!")
		else:
			board_values[int(player_input[0]) - 1][int(player_input[2]) - 1] = 'X'
			no_replace = True
def computer_turn(board_values):
	no_replace = False
	randnum1 = random.randint(0, 2)
	randnum2 = random.randint(0, 2)
	while no_replace == False:
		randindex = board_values[randnum1][randnum2]
		if randindex == " ":
			no_replace = True
			board_values[randnum1][randnum2] = 'O'
		else:
			randnum1 = random.randint(0, 2)
			randnum2 = random.randint(0, 2)
			print("debug")
def show_board(board_values):
	print(("{}|{}|{}\n-----\n{}|{}|{}\n-----\n{}|{}|{}").format(board_values[0][0], board_values[0][1], board_values[0][2], board_values[1][0], board_values[1][1], board_values[1][2], board_values[2][0], board_values[2][1], board_values[2][2]))
board_values = [
[" ", " ", " "],
[" ", " ", " "],
[" ", " ", " "]
]
lose = False
while lose == False:
	player_turn(board_values)
	computer_turn(board_values)
	x_or_y = 'X'
	win = "Player wins!"
	show_board(board_values)
	for x in range(2):
		if board_values[0][0] == x_or_y and board_values[0][1] == x_or_y and board_values[0][2] == x_or_y:
			print(win)
			lose = True
			break
		if board_values[0][0] == x_or_y and board_values[1][0] == x_or_y and board_values[2][0] == x_or_y:
			print(win)
			lose = True
			break
		if board_values[0][0] == x_or_y and board_values[1][1] == x_or_y and board_values[2][2] == x_or_y:
			print(win)
			lose = True	
			break
		if board_values[0][2] == x_or_y and board_values[1][2] == x_or_y and board_values[2][2] == x_or_y:
			print(win)
			lose = True
			break
		if board_values[2][0] == x_or_y and board_values[2][1] == x_or_y and board_values[2][2] == x_or_y:
			print(win)
			lose = True
			break
		if board_values[2][0] == x_or_y and board_values[1][1] == x_or_y and board_values[0][2] == x_or_y:
			print(win)
			lose = True
			break
		if board_values[0][1] == x_or_y and board_values[1][1] == x_or_y and board_values[2][1] == x_or_y:	
			print(win)
			lose = True
			break
		if board_values[1][0] == x_or_y and board_values[1][1] == x_or_y and board_values[1][2] == x_or_y:
			print(win)
			lose = True	
			break
		x_or_y = 'O'
		win = "Computer wins!"

