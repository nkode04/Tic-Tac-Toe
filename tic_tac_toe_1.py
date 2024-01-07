

import turtle
import time

t = turtle.Turtle()


t.hideturtle()
t.speed('fastest')

t.penup()
t.forward(100)
t.pendown()
t.right(90)
t.forward(300)
t.penup()
t.right(180)
t.forward(300)
t.pendown()
t.forward(300)
t.right(180)
t.penup()
t.forward(300)
t.right(90)
t.forward(200)
t.pendown()
t.right(90)
t.forward(300)
t.right(180)
t.penup()
t.forward(300)
t.pendown()
t.forward(300)
t.right(180)
t.penup()
t.forward(200)
t.left(90)
t.pendown()
t.forward(200)
t.right(180)
t.penup()
t.forward(200)
t.pendown()
t.forward(400)
t.right(180)
t.penup()
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.pendown()
t.forward(200)
t.right(180)
t.penup()
t.forward(200)
t.pendown()
t.forward(400)

player = 'x'
opponent = 'o'

board = [
    [ '_', '_', '_' ],
    [ '_', '_', '_' ],
    [ '_', '_', '_' ]
]

turn = 'x'
spotx = 0
spoty = 0
game = ''

def movesLeft(board) :
	for i in range(3) :
		for j in range(3) :
			if (board[i][j] == '_') :
				return True
	return False

def checkWin(b) :
	for row in range(3) :
		if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :
			if (b[row][0] == player) :
				return 10
			elif (b[row][0] == opponent) :
				return -10

	for col in range(3) :
		if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) :
			if (b[0][col] == player) :
				return 10
			elif (b[0][col] == opponent) :
				return -10

	if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) :
		if (b[0][0] == player) :
			return 10
		elif (b[0][0] == opponent) :
			return -10
	
	if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) :
		if (b[0][2] == player) :
			return 10
		elif (b[0][2] == opponent) :
			return -10

	return 0

def minimax(board, depth, isMax) :
    global turn
    score = checkWin(board)

    if (score == 10) :
        return score
 
    if (score == -10) :
        return score
 
    if (movesLeft(board) == False) :
        return 0
 
    if (isMax) :    
        best = -1000
 
        for i in range(3) :        
            for j in range(3) :
              
                if (board[i][j]=='_') :
                 
                    board[i][j] = player
                    turn = 'x'
 
                    best = max( best, minimax(board, depth + 1, not isMax) )
 
                    board[i][j] = '_'
        return best
 
    else :
        best = 1000
 
        for i in range(3) :        
            for j in range(3) :
              
                if (board[i][j] == '_') :
                 
                    board[i][j] = opponent
                    best = min(best, minimax(board, depth + 1, not isMax))
 
                    board[i][j] = '_'
        return best
 

def findBestMove(board) :
    global turn, spotx, spoty
    bestVal = -1000
    bestMove = (-1, -1)
 
    for i in range(3) :    
        for j in range(3) :
         
            if (board[i][j] == '_') :
             
                board[i][j] = player
 
                moveVal = minimax(board, 0, False)
 
                board[i][j] = '_'
 
                if (moveVal > bestVal) :               
                    bestMove = (i, j)
                    bestVal = moveVal
 
    if (bestMove[0] == 0 and bestMove[1] == 0) :
        spotx = -200
        spoty = 200
        board[0][0] = 'x'
    elif (bestMove[0] == 0 and bestMove[1] == 1) :
        spotx = 0
        spoty = 200
        board[0][1] = 'x'
    elif (bestMove[0] == 0 and bestMove[1] == 2) :
        spotx = 200
        spoty = 200
        board[0][2] = 'x'
    elif (bestMove[0] == 1 and bestMove[1] == 0) :
        spotx = -200
        spoty = 0
        board[1][0] = 'x'
    elif (bestMove[0] == 1 and bestMove[1] == 1) :
        spotx = 0
        spoty = 0
        board[1][1] = 'x'
    elif (bestMove[0] == 1 and bestMove[1] == 2) :
        spotx = 200
        spoty = 0
        board[1][2] = 'x'
    elif (bestMove[0] == 2 and bestMove[1] == 0) :
        spotx = -200
        spoty = -200
        board[2][0] = 'x'
    elif (bestMove[0] == 2 and bestMove[1] == 1) :
        spotx = 0
        spoty = -200
        board[2][1] = 'x'
    elif (bestMove[0] == 2 and bestMove[1] == 2) :
        spotx = 200
        spoty = -200
        board[2][2] = 'x'
    if (turn == 'x') :
        turtle.hideturtle()
        turtle.penup()
        turtle.speed('fastest')
        turtle.goto(spotx, spoty)
        turtle.setheading(0)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(50)
        turtle.backward(100)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.backward(100)
        turn = 'o'
    return bestMove

def draw(x, y) :
    global turn, board, spotx, spoty, place
    place = True
    if(x < -100 and y > 100) :
        if (board[0][0] == '_') :
            spotx = -200
            spoty = 200
            board[0][0] = 'o'
        else :
            place = False
    elif(x < 100 and x > -100 and y > 100) :
        if (board[0][1] == '_') :
            spotx = 0
            spoty = 200
            board[0][1] = 'o'
        else :
            place = False
    elif(x > 100 and y > 100) :
        if (board[0][2] == '_') :
            spotx = 200
            spoty = 200
            board[0][2] = 'o'
        else :
            place = False
    elif(x < -100 and y > -100 and y < 100) :
        if (board[1][0] == '_') :
            spotx = -200
            spoty = 0
            board[1][0] = 'o'
        else :
            place = False
    elif(x < 100 and x > -100 and y > -100 and y < 100) :
        if (board[1][1] == '_') :
            spotx = 0
            spoty = 0
            board[1][1] = 'o'
        else :
            place = False
    elif(x > 100 and y > -100 and y < 100) :
        if (board[1][2] == '_') :
            spotx = 200
            spoty = 0
            board[1][2] = 'o'  
        else :
            place = False
    elif(x < -100 and y < -100) :
        if (board[2][0] == '_') :
            spotx = -200
            spoty = -200
            board[2][0] = 'o'
        else :
            place = False
    elif(x < 100 and x > -100 and y < -100) :
        if (board[2][1] == '_') :
            spotx = 0
            spoty = -200
            board[2][1] = 'o'
        else :
            place = False
    elif(x > 100 and y < -100) :
        if (board[2][2] == '_') :
            spotx = 200
            spoty = -200
            board[2][2] = 'o'
        else :
            place = False
    if (place == True) :
        if(turn == 'o') :
            turtle.hideturtle()
            turtle.penup()
            turtle.speed('fastest')
            turtle.goto(spotx, spoty-50)
            turtle.setheading(0)
            turtle.pendown()
            turtle.circle(50)
            turn = 'x'




while (game != 'done') :

    spot1 = board[0][0]
    spot2 = board[0][1]
    spot3 = board[0][2]
    spot4 = board[1][0]
    spot5 = board[1][1]
    spot6 = board[1][2]
    spot7 = board[2][0]
    spot8 = board[2][1]
    spot9 = board[2][2]


    if (spot1 == spot2 and spot2 == spot3) :
        if (spot1 == 'x') :
            style = ('Courier', 30, 'italic')
            turtle.write('x wins', font=style, align='center')
            time.sleep(3)
            turtle.bye()
        if (spot1 == 'o') :
            style = ('Courier', 30, 'italic')
            turtle.write('o wins', font=style, align='center')
            time.sleep(3)
            turtle.bye()
    elif (spot4 == spot5 and spot5 == spot6) :
        if (spot4 == 'x') :
            style = ('Courier', 30, 'italic')
            turtle.write('x wins', font=style, align='center')
            time.sleep(3)
            turtle.bye()
        if (spot4 == 'o') :
            style = ('Courier', 30, 'italic')
            turtle.write('o wins', font=style, align='center')
            time.sleep(3)
            turtle.bye()
    elif (spot7 == spot8 and spot8 == spot9) :
        if (spot7 == 'x') :
            style = ('Courier', 30, 'italic')
            turtle.write('x wins', font=style, align='center')
            time.sleep(3)
            turtle.bye()
        if (spot7 == 'o') :
            style = ('Courier', 30, 'italic')
            turtle.write('o wins', font=style, align='center')
            time.sleep(3)
            turtle.bye()
    elif (spot1 == spot4 and spot4 == spot7) :
        if (spot1 == 'x') :
            style = ('Courier', 30, 'italic')
            turtle.write('x wins', font=style, align='center')
            time.sleep(3)
            turtle.bye()
        if (spot1 == 'o') :
            style = ('Courier', 30, 'italic')
            turtle.write('o wins', font=style, align='center')
            time.sleep(3)
            turtle.bye()
    elif (spot2 == spot5 and spot5 == spot8) :
        if (spot2 == 'x') :
            style = ('Courier', 30, 'italic')
            turtle.write('x wins', font=style, align='center')
            time.sleep(3)
            turtle.bye()
        if (spot2 == 'o') :
            style = ('Courier', 30, 'italic')
            turtle.write('o wins', font=style, align='center')
            time.sleep(3)
            turtle.bye()
    elif (spot3 == spot6 and spot6 == spot9) :
        if (spot3 == 'x') :
            style = ('Courier', 30, 'italic')
            turtle.write('x wins', font=style, align='center')
            time.sleep(3)
            turtle.bye()
        if (spot3 == 'o') :
            style = ('Courier', 30, 'italic')
            turtle.write('o wins', font=style, align='center')
            time.sleep(3)
            turtle.bye()
    elif (spot1 == spot5 and spot5 == spot9) :
        if (spot1 == 'x') :
            style = ('Courier', 30, 'italic')
            turtle.write('x wins', font=style, align='center')
            time.sleep(3)
            turtle.bye()
        if (spot1 == 'o') :
            style = ('Courier', 30, 'italic')
            turtle.write('o wins', font=style, align='center')
            time.sleep(3)
            turtle.bye()
    elif (spot3 == spot5 and spot5 == spot7) :
        if (spot3 == 'x') :
            style = ('Courier', 30, 'italic')
            turtle.write('x wins', font=style, align='center')
            time.sleep(3)
            turtle.bye()
        if (spot3 == 'o') :
            style = ('Courier', 30, 'italic')
            turtle.write('o wins', font=style, align='center')
            time.sleep(3)
            turtle.bye()
    elif (spot1 != '_' and spot2 != '_' and spot3 != '_' and spot4 != '_' and spot5 != '_' and spot6 != '_' and spot7 != '_' and spot8 != '_' and spot9 != '_') :
        style = ('Courier', 30, 'italic')
        turtle.write('draw', font=style, align='center')
        time.sleep(3)
        turtle.bye()
    if (turn == 'x') :
        bestMove = findBestMove(board)
    elif (turn == 'o') :
        turtle.onscreenclick(draw, 1)
        turtle.speed(10)




