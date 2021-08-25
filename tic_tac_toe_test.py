# -*- coding: utf-8 -*-
"""
Created on Thu May 20 17:43:37 2021

@author: Wajeeh Rehman
"""



import random
import sys

Board={1:' ',2:' ',3:' ',
       4:' ',5:' ',6:' ',
       7:' ',8:' ',9:' '}



def PrintBoard(board):
    
    print(board[1] +'|' + board[2] +'|' + board[3])
    print('-+-+-')
    print(board[4] +'|' + board[5] +'|' + board[6])
    print('-+-+-')
    print(board[7] +'|' + board[8] +'|' + board[9])
    print('-+-+-')

print(PrintBoard(Board))
    

def win_condition(Player1,Player2,board):
    
    if((board[1]==board[2]==board[3]==Player1) or 
       (board[4]==board[5]==board[6]==Player1) or
       (board[7]==board[8]==board[9]==Player1) or
       (board[1]==board[5]==board[9]==Player1) or
       (board[3]==board[5]==board[7]==Player1) or
       (board[1]==board[4]==board[7]==Player1) or
       (board[2]==board[5]==board[8]==Player1) or
       (board[3]==board[6]==board[9]==Player1)):
        print("Player 1 Wins")
        sys.exit()
    
    
    if((board[1]==board[2]==board[3]==Player2) or 
       (board[4]==board[5]==board[6]==Player2) or
       (board[7]==board[8]==board[9]==Player2) or
       (board[1]==board[5]==board[9]==Player2) or
       (board[3]==board[5]==board[7]==Player2) or
       (board[1]==board[4]==board[7]==Player2) or
       (board[2]==board[5]==board[8]==Player2) or
       (board[3]==board[6]==board[9]==Player2)):
        print("Player 2 Wins")
        sys.exit()
   
    
    
def game(board):
    
    choice=random.randint(1, 2)
    
    if (choice==1):
        print("Player 1 is O and Player 2 is X")

        Player1='O'
        Player2='X'
        turn=0
      
    if (choice==2):
        
        print("Player 1 is X and Player 2 is O")
        print()
        Player1='X'
        Player2='O'
        turn=1
    
    count=0
    
    for i in range(1,9):
        
        if(count==9):
            print("The Game is declared a draw")
            sys.exit()
      
        if(turn==0):
            
            print("It is player 1's turn")
            print("Select any values between 1 to 9")
            player_input=int(input())
            
            if (board[player_input]==' '):
                board[player_input]=Player1
           
            else:
                print("Sorry that position is already filled select another position")
                player_input=int(input())
                board[player_input]=Player1
                 
            PrintBoard(board)
          
            turn=1
            count+=1
       
        win_condition(Player1,Player2,board)
         
        if(turn==1):
            
            print("It is player 2's turn")
            print("Select any values between 1 to 9")
            player_input=int(input())
            
            if (board[player_input]==' '):
                board[player_input]=Player2
           
            else:
                print("Sorry that position is already filled select another position")
                player_input=int(input())
                board[player_input]=Player2
            
            turn=0
            count+=1
        
            PrintBoard(board)
       
        win_condition(Player1,Player2,board)
    
def main():
    
    PrintBoard(Board)
    game(Board)
    
if __name__ == '__main__':
    main()

        
        
    