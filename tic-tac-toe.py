import random
print("=============================================================================")
print("\n			WELCOME TO TIC-TAC-TOE			\n")
print("=============================================================================\n")
player1=input("You are PLAYER 1. Enter a symbol: ")
player2=input("\nYou are PLAYER 2. Enter a different symbol: ")
while(player1==player2):
	player2=input("\nSame symbol is NOT ACCEPTED. Please enter a different symbol: ")
box=0
def display_board(board):

	print("\t "+board[6]+" | "+board[7]+" | "+board[8] )
	print("\t-----------")
	print("\t "+board[3]+" | "+board[4]+" | "+board[5] )
	print("\t-----------")
	print("\t "+board[0]+" | "+board[1]+" | "+board[2] )

test_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
display_board(test_board)


def place_marker(board,marker,position):
	board[position]=marker

def win_check(board,mark):
	if(board[7]==mark):
		if(board[6]==mark and board[8]==mark):
			return True
	if(board[1]==mark):
		if(board[0]==mark and board[2]==mark):
			return True
	if(board[3]==mark):
		if(board[6]==mark and board[0]==mark):
			return True
	if(board[5]==mark):
		if(board[2]==mark and board[8]==mark):
			return True
	if(board[4]==mark):
		if(board[6]==mark and board[2]==mark):
			return True
		if(board[0]==mark and board[8]==mark):
			return True
		if(board[3]==mark and board[5]==mark):
			return True
		if(board[1]==mark and board[7]==mark):
			return True
	else:
		return False

def choose_first():
	choose=random.randint(0,1)
	if (choose):
		print("PLAYER 1 goes first\n")
		return True
	else:
		print("PLAYER 2 goes first\n")
		return False

def space_check(board,position):
	if(board[position]==' '):
		return True
	else:
		return False
			
def full_board_check(board):
	a=8
	while a>=0:
		if(board[a]==' '):
			return True
			break
		else:
			a-=1
	return False


def player_input(board):
	global box
	box=int(input("Choose the box you want: From 1(BOTTOM LEFT CORNER) TO 9(TOP RIGHT CORNER)\n"))
	while(box>9 or box<1):
		print("\nWrong input. Try Again!\n")
		box=int(input("Choose the box you want: From 1(BOTTOM LEFT CORNER) TO 9(TOP RIGHT CORNER)\n"))
	box-=1
	if(space_check(board,box)):
		return box
	else:
		print("The box you chose is already filled\n")

def replay():
	ans=input("Do you want to play again? yes OR no:  ")
	if(ans.lower()=='yes'):
		return True
	elif(ans.lower()=='no'):
		return False
	else:
		while(ans.lower()!='yes' or ans.lower()!='no'):
			print("Wrong answer")
			ans=input("Do you want to play again? yes OR no:  ")
			if(ans.lower()=='yes'):
				return True
			elif(ans.lower()=='no'):
				return False

#EXECUTION:
def execution():
	x=0
	y=0
	if(choose_first()):
		print("\nPlayer1's Turn:")
		player_input(test_board)
		place_marker(test_board,player1,box)
		display_board(test_board)
		x+=1
	else:
		print("\nPlayer2's Turn:")	
		player_input(test_board)
		place_marker(test_board,player2,box)
		display_board(test_board)

	while (full_board_check(test_board)):
		if(x%2==0):
			print("\nPlayer1's Turn:")
			player_input(test_board)
			if(space_check(test_board,box)):
				place_marker(test_board,player1,box)
			else:
				while(space_check(test_board,box)==False):
					print("Chosen position is Full!\n")
					print("Your turn again!\n")
					player_input(test_board)
				place_marker(test_board,player1,box)
			display_board(test_board)
		else:
			print("\nPlayer2's Turn:")	
			player_input(test_board)
			if(space_check(test_board,box)):
				place_marker(test_board,player2,box)
			else:
				while(space_check(test_board,box)==False):
					print("Chosen position is Full!\n")
					print("Your turn again!\n")
					player_input(test_board)
				place_marker(test_board,player2,box)
			display_board(test_board)
		if(win_check(test_board,player1)):
			print("\n**************Congratulations! PLAYER 1 IS THE WINNER! ***************\n")
			y+=1
			break
		elif(win_check(test_board,player2)):
			y+=1
			print("\n**************Congratulations! PLAYER 2 IS THE WINNER! ***************\n")
			break
		x+=1
	if(y==0):
		print("------------- IT ENDS AS A DRAW! ---------------")

execution()

while(replay()):
	test_board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
	box=0
	execution()
