# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 14:19:06 2020

This Tic-tac-toe Games is COMP-2100 Group 1 Final Project
Submitted to Prof. Othman, Salem

@author: Boonpeng, Pikulkaew (Pk)
@author: DiMarzio, Ariane
@author: Sajjad, Tania

This project uses PyGame for creating GUI

There are 2 types of games
1. Traditional Tic-tac-toe (X and O players)
        - A row, a column, or a diagonal line must have the same sign.
        
2. Sum-of-15 Tic-tac-toe (Even number and Odd number players)
        - The last player who makes a row, a column, or a diagonal line has the
    sum of 15 will be the winner.
        - Odd number player always goes first: 1, 3, 5, 7, 9
        - Even number player: 2, 4, 6, 8
        
"""

import pygame

pygame.init()

#window width
windowWidth = 1200
#window height
windowHeight = 600
#sets window dimension
screen = pygame.display.set_mode((windowWidth, windowHeight))
#set window's title
pygame.display.set_caption('COMP-2100-09 Final Project Group 1: Tic-tac-toe Client')
#-----------------------------------------------------------------------------
#colors
BLACK  = (0, 0, 0)
WHITE  = (255, 255, 255)
RED    = (255, 138, 138)

#-----------------------------------------------------------------------------
#font setting for "select" text
selectText = pygame.font.Font(pygame.font.get_default_font(), 24)
#font for buttons
btnText = pygame.font.Font(pygame.font.get_default_font(), 40)

#stores game option; 1 for XO , 2 for number
gameOption = 0;
#stores player option; 1 for 1 player(not available), 2 for 2 players
playerOption = 0

#stores player 1's score
score1 = 0
#stores player 2's score
score2 = 0
#player 1 is X or Odd
player1 = ""
#player 2 is O or Even
player2 = ""

#global variables used when sending and receiving data from other user
playing= True
turn=True
numOfImg = 1
tradiCurrPlayer= 'x'

#grid setting for X and O
gridTradi = [[None]*3, [None]*3, [None]*3]
gridImg = pygame.image.load(r"assets\grid.png")
row = 0
col = 0

#gris setting for Odd and Even
gridNum = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# 1 | 2 | 3
#---+---+---
# 4 | 5 | 6
#---+---+---
# 7 | 8 | 9
cell = 0
#------------------------------------------------------------------
gridImg = pygame.transform.scale(gridImg, (480,430))

#X and O game option button image
imgGame1 = pygame.image.load(r"assets\game1.png")
imgGame1 = pygame.transform.scale(imgGame1, (160,160))
#Odd and Even game option button image
imgGame2 = pygame.image.load(r"assets\game2.png")
imgGame2 = pygame.transform.scale(imgGame2, (160,160))

#1 player option button image
imgPlayer1 = pygame.image.load(r"assets\player1.png")
imgPlayer1 = pygame.transform.scale(imgPlayer1, (160,160))
#2 player option button image
imgPlayer2 = pygame.image.load(r"assets\player2.png")
imgPlayer2 = pygame.transform.scale(imgPlayer2, (160,160))

#loads x image
xImg = pygame.image.load(r"assets\x.png") 
xImg = pygame.transform.scale(xImg, (80,80))
#loads o image
imgO = pygame.image.load(r"assets\o.png")
imgO = pygame.transform.scale(imgO, (80,80))

#loads winning lines
imgWinHon = pygame.image.load(r"assets\honWinLine.png")
imgWinHon = pygame.transform.scale(imgWinHon, (400,14))
imgWinVer = pygame.image.load(r"assets\verWinLine.png")
imgWinVer = pygame.transform.scale(imgWinVer, (14,400))
imgWinTopLeft = pygame.image.load(r"assets\topLeftWinLine.png")
imgWinTopLeft = pygame.transform.scale(imgWinTopLeft, (390,390))
imgWinTopRight = pygame.image.load(r"assets\topRightWinLine.png")
imgWinTopRight = pygame.transform.scale(imgWinTopRight, (390,390))

import threading 

#creates a thread to communicate between users
def createThread(target):
    thread=threading.Thread(target=target)
    thread.daemon=True
    thread.start()

import socket

HOST= '127.0.0.1'
PORT= 1542

#creates socket and socket connection
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

#method to receive data from the other user
def receiveData():
    global turn, playing, xImg, score1, gameOption, numOfImg, btnText
    #infinite loop for receive any data sent 
    while True:
        data= sock.recv(1024).decode()
        print(data)
        data=data.split("-")
        x,y=int(float(data[0])),int(float(data[1])) 
        turn=True
        if x>585 and x<975 and y>34 and y<415:
            #X and O game output for other player's move
            if gameOption==1:
                screen.blit(xImg, (x, y))
                #turn status output
                background = pygame.Rect(55, 525, 375, 75)
                pygame.draw.rect(screen, BLACK, background)
                screen.blit(btnText.render("Your turn!", True, RED), (60, 525))
            #num output for other player's move
            elif gameOption==2:
                imgNum = pygame.image.load('assets\\' + str(numOfImg) + ".png")
                imgNum = pygame.transform.scale(imgNum, (80,80))
                if x > 585 and x < 715 and y > 35 and y < 155:
                     cell = 0
                elif x > 715 and x <= 850 and y > 35 and y <= 155:
                    cell = 1
                elif x > 850 and x <= 975 and y > 35 and y <= 155:
                    cell = 2
                elif x > 585 and x <= 715 and y > 155 and y <= 300:
                    cell = 3
                elif x > 715 and x <= 850 and y > 155 and y <= 300:
                    cell = 4
                elif x > 850 and x <= 975 and y > 155 and y <= 300:
                    cell = 5
                elif x > 585 and x <= 715 and y > 300 and y <= 415:
                    cell = 6
                elif x > 715 and x <= 850 and y > 300 and y <= 415:
                    cell = 7
                elif x > 850 and x <= 975 and y > 300 and y <= 415:
                    cell = 8
                gridNum[cell]= numOfImg
                screen.blit(imgNum, (x, y))
                numOfImg+=1
                #turn status output
                background = pygame.Rect(55, 525, 375, 75)
                pygame.draw.rect(screen, BLACK, background)
                screen.blit(btnText.render("Your turn!", True, RED), (60, 525))
        #checks to see if the other player won
        if len(data)==4  : 
            thirdPlace = int(float(data[2]))
            #determines which winning line is being used and prints
            if thirdPlace==1.0:
                screen.blit(imgWinHon, (x, y)) 
            elif thirdPlace==2.0:
                screen.blit(imgWinVer, (x, y)) 
            elif thirdPlace==3.0:
                screen.blit(imgWinTopLeft, (x, y)) 
            elif thirdPlace==4.0:
                screen.blit(imgWinTopRight, (x, y)) 
            #updates the other player's score since they won 
            score1+=1
            playing=False
            #turn update output
            background = pygame.Rect(55, 525, 375, 75)
            pygame.draw.rect(screen, BLACK, background)
            screen.blit(btnText.render("Game Over!", True, RED), (60, 525))

        pygame.display.update()

#calls the createThread method and passes in receiveData
createThread(receiveData)

#GUI for the game
def gamePage():
    global score1, score2, gameOption, screen, btnText, player1, player2, selectText
    
    #Game option header
    screen.blit(btnText.render("Games", True, RED), (55,50))
    screen.blit(imgGame1, (55, 90))
    screen.blit(imgGame2, (215, 90))
    screen.blit(btnText.render("Players", True, RED), (55,300))
    screen.blit(imgPlayer1, (55, 345))
    screen.blit(imgPlayer2, (215, 345))
    
    #score board for player 1
    player1Score = pygame.Rect(435, 460, 180, 45)
    pygame.draw.rect(screen, RED, player1Score)
    
    #score board for player 2
    player2Score = pygame.Rect(435, 515, 180, 45)
    pygame.draw.rect(screen, RED, player2Score)
    
    #shows grid image
    screen.blit(gridImg, (550, 20))
    
    #if a game option is selected (not zero), player 1's score board will show player 1's score.
    #otherwise, it will tell the user to select a game.
    if gameOption != 0:
        screen.blit(selectText.render("Select Games", True, RED), (443, 470))
        screen.blit(btnText.render(player1 + ": " + str(score1), True, BLACK), (455, 465))
    else:
        screen.blit(btnText.render(player1 + ": " + str(score1), True, RED), (455, 465))
        screen.blit(selectText.render("Select Games", True, BLACK), (443, 470))
    
    #if a player option is selected (not zero), player 2's score board will show player 2's score.
    #otherwise, it will tell the user to select a number of players.
    if playerOption != 0:
        screen.blit(selectText.render("Select Players", True, RED), (441, 525))
        screen.blit(btnText.render(player2 + ": " + str(score2), True, BLACK), (455, 520))
    else:
        screen.blit(btnText.render(player2 + ": " + str(score2), True, RED), (455, 520))
        screen.blit(selectText.render("Select Players", True, BLACK), (441, 525))
    
    #if gameOption is 1 means X and O
    #otherwise, it means odd and even
    if gameOption == 1:
        player1 = "X"
        player2 = "O"
    elif gameOption == 2:
        player1 = "Even"
        player2 = "Odd"
       
    #Again button setting
    againBtn = pygame.Rect(655, 460, 130, 100)
    pygame.draw.rect(screen, RED, againBtn)
    screen.blit(btnText.render("Again", True, BLACK), (663, 490))
    
    #New button setting
    newBtn = pygame.Rect(831, 460, 130, 100)
    pygame.draw.rect(screen, RED, newBtn)
    screen.blit(btnText.render("New", True, BLACK), (855, 490))
    
    #Reset button setting
    resetBtn = pygame.Rect(1005, 460, 130, 100)
    pygame.draw.rect(screen, RED, resetBtn)
    screen.blit(btnText.render("Reset", True, BLACK), (1015, 490))
    
#keeps track of loop
count=0  
#set gameOption and playerOption by checking the ranges of co-ordiantes of each button
def setGameAndPlayerOptions():
    global gameOption, playerOption, imgGame1, imgGame2, count
    
    count+=1
    x, y = pygame.mouse.get_pos()
    
    if x > 55 and x < 215 and y > 90 and y < 250:
        if gameOption == 0:
            gameOption = 1         
    
    if x > 215 and x < 375 and y > 90 and y < 250:
        if gameOption == 0:
            gameOption = 2
        
    if x > 55 and x < 215 and y > 345 and y < 505:
        if playerOption == 0:
            playerOption = 0
    
    if x > 215 and x < 375 and y > 345 and y < 505:
        if playerOption == 0:
            playerOption = 2
            if count==2:
                #turn status output
                background = pygame.Rect(55, 525, 375, 75)
                pygame.draw.rect(screen, BLACK, background)
                screen.blit(btnText.render("Your turn!", True, RED), (60, 525))
    
#sets everything back to the beginning and clear the grid,
#but does not reset the scores nor let the users change game and player options
def clear():
    global tradiCurrPlayer, gridTradi, gridNum, gameOption, cell, numOfImg
    
    screen.blit(gridImg, (550, 20))
    screen.fill(BLACK)
    
    if gameOption==1:
        tradiCurrPlayer = 'x'
        for row in range(0,3):
            for col in range(0,3):
                gridTradi[row][col] = None
    else:
        cell = 0
        numOfImg = 1
        gridNum = [0, 0, 0, 0, 0, 0, 0, 0, 0]

#function for Again button
def againBtn():
    global turn, playing
    x, y = pygame.mouse.get_pos()
    if x > 655 and x < 785 and y > 460 and y < 560:
        clear()
        turn=True
        playing= True
        sendData= '{}-{}-{}'.format(x,y,playing).encode() 
        sock.send(sendData)
        #turn status output
        background = pygame.Rect(55, 525, 375, 75)
        pygame.draw.rect(screen, BLACK, background)
        screen.blit(btnText.render("Your turn!", True, RED), (60, 525))
 
#function for New button. resets the scores
def newBtn():
    global score1, score2, turn, playing
    
    x, y = pygame.mouse.get_pos()
    if x > 830 and x < 961 and y > 460 and y < 560:
        score1 = 0
        score2 = 0
        screen.blit(gridImg, (550, 20))
        screen.fill(BLACK)
        clear()
        playing=True
        turn= True
        sendData= '{}-{}-{}'.format(x,y,playing).encode() 
        sock.send(sendData)
        #turn status output
        background = pygame.Rect(55, 525, 375, 75)
        pygame.draw.rect(screen, BLACK, background)
        screen.blit(btnText.render("Your turn!", True, RED), (60, 525))
 
#function for Reset button. resets the score and
#the users can change game and player options
def resetBtn():
    global gameOption, playerOption, score1, score2, turn, playing, count, numOfImg
    
    x, y = pygame.mouse.get_pos()
    if x > 1005 and x < 1135 and y > 460 and y < 560:
        score1 = 0
        score2 = 0
        gameOption = 0
        playerOption = 0
        numOfImg=1
        screen.blit(gridImg, (550, 20))
        screen.fill(BLACK)
        clear()
        turn=True
        playing=True
        count=0
 
#----------------------------------------
#|           FOR X and O GAME           |
#----------------------------------------

#setting where to put X and O on the grid
def tradiDrawOX(row, col):
    global tradiCurrPlayer, turn
    codY = 0
    codX = 0
    
    if row == 1:
        codY = 50
        
    if row == 2:
        codY = 185
        
    if row == 3:
        codY = 320
        
    if col == 1:
        codX = 614
        
    if col == 2:
        codX = 744
        
    if col == 3:
        codX = 879
        
    #the current player is A so draw something and set the next player to be B
    tradiCurrPlayer='x'
    screen.blit(imgO, (codX, codY))
    turn= False
    
#if a row, column, or diagonal has the same sign, the winning line will be drawn and sent to the other user
def tradiCheckWin():
    global turn, playing
    win = False
    
    row = 0
    if gridTradi[row][0] == gridTradi[row][1] == gridTradi[row][2] and gridTradi[row][0] is not None and gridTradi[row][1] is not None and gridTradi[row][2] is not None:
        screen.blit(imgWinHon, (583, 90))
        playing=False
        sendData= '{}-{}-{}-{}'.format(583,90,1.0,playing).encode() 
        sock.send(sendData)
        #turn status output
        background = pygame.Rect(55, 525, 375, 75)
        pygame.draw.rect(screen, BLACK, background)
        screen.blit(btnText.render("You win!", True, RED), (60, 525))
        turn=False
        win = True
        
    row = 1
    if gridTradi[row][0] == gridTradi[row][1] == gridTradi[row][2] and gridTradi[row][0] is not None and gridTradi[row][1] is not None and gridTradi[row][2] is not None:
        screen.blit(imgWinHon, (583, 222))
        playing=False
        sendData= '{}-{}-{}-{}'.format(583,222,1.0,playing).encode() 
        sock.send(sendData)
        #turn status output
        background = pygame.Rect(55, 525, 375, 75)
        pygame.draw.rect(screen, BLACK, background)
        screen.blit(btnText.render("You win!", True, RED), (60, 525))
        turn=False
        win = True
    
    row = 2
    if gridTradi[row][0] == gridTradi[row][1] == gridTradi[row][2] and gridTradi[row][0] is not None and gridTradi[row][1] is not None and gridTradi[row][2] is not None:
        screen.blit(imgWinHon, (583, 354))
        playing=False
        sendData= '{}-{}-{}-{}'.format(583,354,1.0,playing).encode() 
        sock.send(sendData)
        #turn status output
        background = pygame.Rect(55, 525, 375, 75)
        pygame.draw.rect(screen, BLACK, background)
        screen.blit(btnText.render("You win!", True, RED), (60, 525))
        turn=False
        win = True
        
    col = 0
    if gridTradi[0][col] == gridTradi[1][col] == gridTradi[2][col] and gridTradi[0][col] is not None and gridTradi[1][col] is not None and gridTradi[2][col] is not None:
        screen.blit(imgWinVer, (645, 27))
        playing=False
        sendData= '{}-{}-{}-{}'.format(645,27,2.0,playing).encode() 
        sock.send(sendData)
        #turn status output
        background = pygame.Rect(55, 525, 375, 75)
        pygame.draw.rect(screen, BLACK, background)
        screen.blit(btnText.render("You win!", True, RED), (60, 525))
        turn=False
        win = True
    
    col = 1
    if gridTradi[0][col] == gridTradi[1][col] == gridTradi[2][col] and gridTradi[0][col] is not None and gridTradi[1][col] is not None and gridTradi[2][col] is not None:
        screen.blit(imgWinVer, (775, 27))
        playing=False
        sendData= '{}-{}-{}-{}'.format(775,27,2.0,playing).encode() 
        sock.send(sendData)
        #turn status output
        background = pygame.Rect(55, 525, 375, 75)
        pygame.draw.rect(screen, BLACK, background)
        screen.blit(btnText.render("You win!", True, RED), (60, 525))
        turn=False
        win = True
    
    col = 2
    if gridTradi[0][col] == gridTradi[1][col] == gridTradi[2][col] and gridTradi[0][col] is not None and gridTradi[1][col] is not None and gridTradi[2][col] is not None:
        screen.blit(imgWinVer, (910, 27))
        playing=False
        sendData= '{}-{}-{}-{}'.format(910,27,2.0,playing).encode() 
        sock.send(sendData)
        #turn status output
        background = pygame.Rect(55, 525, 375, 75)
        pygame.draw.rect(screen, BLACK, background)
        screen.blit(btnText.render("You win!", True, RED), (60, 525))
        turn=False
        win = True
        
    if gridTradi[0][0] == gridTradi[1][1] == gridTradi[2][2] and gridTradi[0][0] is not None and gridTradi[1][1] is not None and gridTradi[2][2] is not None:
        screen.blit(imgWinTopLeft, (587, 34))
        playing=False
        sendData= '{}-{}-{}-{}'.format(587, 34,3.0,playing).encode() 
        sock.send(sendData)
        #turn status output
        background = pygame.Rect(55, 525, 375, 75)
        pygame.draw.rect(screen, BLACK, background)
        screen.blit(btnText.render("You win!", True, RED), (60, 525))
        turn=False       
        win = True
    
    if gridTradi[0][2] == gridTradi[1][1] == gridTradi[2][0] and gridTradi[0][0] is not None and gridTradi[1][1] is not None and gridTradi[2][2] is not None:
        screen.blit(imgWinTopRight, (587, 34))
        playing=False
        sendData= '{}-{}-{}-{}'.format(587, 34, 4.0, playing).encode() 
        sock.send(sendData)
        #turn status output
        background = pygame.Rect(55, 525, 375, 75)
        pygame.draw.rect(screen, BLACK, background)
        screen.blit(btnText.render("You win!", True, RED), (60, 525))
        turn=False
        win = True
        
    return win
 
#game logic for X and O    
def tradiGame():
    global turn, tradiCurrPlayer, gridTradi, score1, score2, row, col, playing, turn, btnText
    if turn and playing:
        x, y = pygame.mouse.get_pos()
        if x > 585 and x <= 975 and y > 35 and y <= 415:
            #turn status output
            background = pygame.Rect(55, 525, 375, 75)
            pygame.draw.rect(screen, BLACK, background)
            screen.blit(btnText.render("Wait for your turn!", True, RED), (60, 525))
            
            if x > 585 and x <= 715:
                col = 1
                x=615
            elif x > 715 and x <= 850:
                col = 2
                x=745
            elif x > 850 and x <= 975:
                col = 3
                x=890
            if y > 35 and y <= 155:
                row = 1
                y=55
            elif y > 155 and y <= 300:
                row = 2
                y=185
            elif y > 300 and y <= 415:
                row = 3
                y=320
            
            #sends information about the move to the other user 
            sendData= '{}-{}-{}'.format(int(x),int(y),playing).encode() 
            sock.send(sendData)
            
            if tradiCheckWin() is False:
                if x > 585 and x <= 975 and y > 35 and y <= 415:
                    if gridTradi[row-1][col-1] == None:
                        gridTradi[row-1][col-1] = tradiCurrPlayer
                        tradiDrawOX(row, col)
                        if tradiCheckWin():
                            playing=False
                            if tradiCurrPlayer == 'x':
                                score2 += 1
                            else:
                                score1 += 1
                turn=False

#---------------------------------------------
#|           FOR Odd and Even GAME           |
#---------------------------------------------
#for drawing number images
def numDraw(celll):
    global numOfImg
    codX = 0
    codY = 0
    
    if cell == 1:
        codX= 614
        codY = 50
        
    if cell == 2:
        codX= 744
        codY = 50
        
    if cell == 3:
        codX= 879
        codY = 50
        
    if cell == 4:
        codX= 614
        codY = 185
        
    if cell == 5:
        codX= 744
        codY = 185
        
    if cell == 6:
        codX= 879
        codY = 185
        
    if cell == 7:
        codX= 614
        codY = 320
        
    if cell == 8:
        codX= 744
        codY = 320
        
    if cell == 9:
        codX= 879
        codY = 320        
    
    imgNum = pygame.image.load('assets\\' + str(numOfImg) + ".png")
    imgNum = pygame.transform.scale(imgNum, (80,80))
    screen.blit(imgNum, (codX, codY))

#if a row, column, or diagonal line has the sum of 15, a winning line will be drawn and sent to the other user 
def numCheckWin():
    global turn, playing
    win = False
    
    if (gridNum[0]+ gridNum[1]+ gridNum[2]==15 and gridNum[0] != 0 and gridNum[1] != 0 and gridNum[2] != 0):
        screen.blit(imgWinHon, (583, 90))
        playing=False
        sendData= '{}-{}-{}-{}'.format(583,90,1.0,playing).encode() 
        sock.send(sendData)
        #turn status output
        background = pygame.Rect(55, 525, 375, 75)
        pygame.draw.rect(screen, BLACK, background)
        screen.blit(btnText.render("You win!", True, RED), (60, 525))
        turn=False
        win = True
        
    if (gridNum[3]+ gridNum[4]+ gridNum[5]==15 and gridNum[3] != 0 and gridNum[4] != 0 and gridNum[5] != 0):
        screen.blit(imgWinHon, (583, 222))
        playing=False
        sendData= '{}-{}-{}-{}'.format(583,222,1.0,playing).encode() 
        sock.send(sendData)
        #turn status output
        background = pygame.Rect(55, 525, 375, 75)
        pygame.draw.rect(screen, BLACK, background)
        screen.blit(btnText.render("You win!", True, RED), (60, 525))
        turn=False
        win = True
    
    if (gridNum[6]+ gridNum[7]+ gridNum[8]==15 and gridNum[6] != 0 and gridNum[7] != 0 and gridNum[8] != 0):
        screen.blit(imgWinHon, (583, 354))
        playing=False
        sendData= '{}-{}-{}-{}'.format(583,354,1.0,playing).encode() 
        sock.send(sendData)
        #turn status output
        background = pygame.Rect(55, 525, 375, 75)
        pygame.draw.rect(screen, BLACK, background)
        screen.blit(btnText.render("You win!", True, RED), (60, 525))
        turn=False
        win = True
        
    if (gridNum[0]+ gridNum[3]+ gridNum[6]==15 and gridNum[0] != 0 and gridNum[3] != 0 and gridNum[6] != 0):
        screen.blit(imgWinVer, (645, 27))
        playing=False
        sendData= '{}-{}-{}-{}'.format(645,27,2.0,playing).encode() 
        sock.send(sendData)
        #turn status output
        background = pygame.Rect(55, 525, 375, 75)
        pygame.draw.rect(screen, BLACK, background)
        screen.blit(btnText.render("You win!", True, RED), (60, 525))
        turn=False
        win = True
    
    if (gridNum[1] +gridNum[4]+ gridNum[7]==15 and gridNum[1] != 0 and gridNum[4] != 0 and gridNum[7] != 0):
        screen.blit(imgWinVer, (775, 27))
        playing=False
        sendData= '{}-{}-{}-{}'.format(775,27,2.0,playing).encode() 
        sock.send(sendData)
        #turn status output
        background = pygame.Rect(55, 525, 375, 75)
        pygame.draw.rect(screen, BLACK, background)
        screen.blit(btnText.render("You win!", True, RED), (60, 525))
        turn=False
        win = True
    
    if (gridNum[2]+ gridNum[5]+ gridNum[8]==15 and gridNum[2] != 0 and gridNum[5] != 0 and gridNum[8] != 0):
        screen.blit(imgWinVer, (910, 27))
        playing=False
        sendData= '{}-{}-{}-{}'.format(910,27,2.0,playing).encode() 
        sock.send(sendData)
        #turn status output
        background = pygame.Rect(55, 525, 375, 75)
        pygame.draw.rect(screen, BLACK, background)
        screen.blit(btnText.render("You win!", True, RED), (60, 525))
        turn=False
        win = True
        
    if (gridNum[0]+ gridNum[4]+ gridNum[8]==15 and gridNum[0] != 0 and gridNum[4] != 0 and gridNum[8] != 0):
        screen.blit(imgWinTopLeft, (587, 34))
        playing=False
        sendData= '{}-{}-{}-{}'.format(587,34,3.0,playing).encode() 
        sock.send(sendData)
        #turn status output
        background = pygame.Rect(55, 525, 375, 75)
        pygame.draw.rect(screen, BLACK, background)
        screen.blit(btnText.render("You win!", True, RED), (60, 525))
        turn=False
        win = True
    
    if (gridNum[2]+ gridNum[4]+ gridNum[6]==15 and gridNum[2] != 0 and gridNum[4] != 0 and gridNum[6] != 0):
        screen.blit(imgWinTopRight, (587, 34))
        playing=False
        sendData= '{}-{}-{}-{}'.format(587,34,4.0,playing).encode() 
        sock.send(sendData)
        #turn status output
        background = pygame.Rect(55, 525, 375, 75)
        pygame.draw.rect(screen, BLACK, background)
        screen.blit(btnText.render("You win!", True, RED), (60, 525))
        turn=False
        win = True
        
    return win

#game logic for odd and even       
def numGame():
    global numOfImg, gridNum, score1, score2, cell, playing, turn

    if turn and playing:
        # get coordinates of mouse click 
        x, y = pygame.mouse.get_pos()
        if x > 585 and x <= 975 and y > 35 and y <= 415:
             #turn status output
            background = pygame.Rect(55, 525, 375, 75)
            pygame.draw.rect(screen, BLACK, background)
            screen.blit(btnText.render("Wait for your turn!", True, RED), (60, 525))
            if x > 585 and x < 715 and y > 35 and y < 155:
                cell = 1
                x=615
                y=55
            elif x > 715 and x <= 850 and y > 35 and y <= 155:
                cell = 2
                x=745
                y=55
            elif x > 850 and x <= 975 and y > 35 and y <= 155:
                cell = 3
                x=890
                y=55
            elif x > 585 and x <= 715 and y > 155 and y <= 300:
                cell = 4
                x=615
                y=185
            elif x > 715 and x <= 850 and y > 155 and y <= 300:
                cell = 5
                x=745
                y=185
            elif x > 850 and x <= 975 and y > 155 and y <= 300:
                cell = 6
                x=890
                y=185
            elif x > 585 and x <= 715 and y > 300 and y <= 415:
                cell = 7
                x=615
                y=320
            elif x > 715 and x <= 850 and y > 300 and y <= 415:
                cell = 8
                x=745
                y=320
            elif x > 850 and x <= 975 and y > 300 and y <= 415:
                cell = 9
                x=890
                y=320
            
            if numCheckWin() is False:
                if x > 585 and x <= 975 and y > 35 and y <= 415:
                    if gridNum[cell-1] < 1 and numOfImg <= 9:
                        gridNum[cell-1] = numOfImg
                        numDraw(cell)
                        #sends information about the move to the other user 
                        sendData= '{}-{}-{}'.format(x,y,playing).encode() 
                        sock.send(sendData)
                        numOfImg += 1
                        if numCheckWin():
                            playing=False
                            if numOfImg % 2:
                                score1 += 1
                            else:
                                score2 += 1

#for running the buttons and runs the right type of selected game option
def gameClicks():
    global gameOption
    
    againBtn()
    newBtn()
    resetBtn()
    
    if gameOption == 1:
        tradiGame()
    elif gameOption == 2:
        numGame()
 
#for running the game
running = True

#while loop for running Pygame
while running:
    pygame.init()
   
    gamePage()
    #if mouse click event happens in the active co-ordinate, the game runs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            playing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            setGameAndPlayerOptions()
            gameClicks()
            
    pygame.display.update()
            
pygame.quit()