#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tkinter-based GUI for Notakto
"""
import tkinter as tk
from Notakto import Game
from tkinter import messagebox

#Instance of Game from Notakto.py
notaktoGui = Game()

class GameGUI:
    def __init__(self, master):
        self.master = master 
        self.current_frame = my_label
        self.board_labels = {}
        self.boards = {
            "A": list(range(9)),
            "B": list(range(9)),
            "C": list(range(9))
        }
        self.notakto = Game()
        self.player = ''
    def create_board_labels(self):
        column = 0
        for board_key in self.boards.keys():
            board_frame = tk.Frame(self.master,padx=10,pady=10, 
                                   borderwidth=2,relief="solid")
            
            board_frame.grid(row = 0, column = column)
            column += 1
            
            label = tk.Label(board_frame, text=f"Board {board_key}")
            label.grid(row = 0, column = 0, columnspan=3)
            
            self.board_labels[board_key] = {}
            
            for i, mark in enumerate(self.boards[board_key]):
                boardLabel = tk.Button(board_frame, text=mark, 
                                       width=4, height=4, border=2, 
                                       command = lambda mark=mark, board_key=board_key, 
                                       i=i: self.userInput(i, board_key,mark))
                
                boardLabel.grid(row=(i // 3) + 1, column=i % 3)
                self.board_labels[(board_key, i)] = boardLabel
                
    def printBoards(self, boards):
        self.update_board_labels(boards)
        
    def update_board_labels(self, boards):
        #self.checkDeadBoard()
        for key, board in boards.items():
            for i in range(9):
                value = board[i] if board[i] != 'X' else 'X'
                self.board_labels[key][i] = value
        
    def checkGameOver(self):        
        deadBoard = self.notakto.isAllBoardDead(self.boards)
        
        if deadBoard:
            lastPlayer = self.player
            messagebox.showwarning('Player Lost', lastPlayer + ' Lost')
            
    def checkDeadBoard(self):
        #Check for dead state
        for key,board in self.boards.items():
            if self.notakto.isDead(board):
                
                #Board is dead, mark entire board with 'X'
                for label in self.board_labels[key]:
                    self.board_labels[(key, label)]["text"] = 'X'
                    self.board_labels[(key, label)].config(state="disabled")                
            
                #Update boards[key] to all X when a board is dead
                self.boards[key] = ['X'] * 9
                
    #Handle play button
    def start_game_button(self):
        if self.current_frame:
            self.current_frame.destroy()
            
        play_Frame = tk.Frame(self.master)
        
        labelPrint = tk.Label(play_Frame, text = "The button is pressed")
        labelPrint.grid()
        play_Frame.grid()
        
        self.create_board_labels()
        self.current_frame = play_area
        self.opponent_move()
        
    def userInput(self, i, board_key, mark):
        self.player = 'User'
        move = board_key + str(mark)
        print(move)
        
        self.notakto.makeMove(self.boards, move)
        self.board_labels[(board_key,i)]["text"]='X'
        self.board_labels[(board_key, i)].config(state="disabled")
        
        self.printBoards(self.boards)
        self.checkDeadBoard()
        self.checkGameOver()
        self.opponent_move()
        
    def opponent_move(self):
        self.player = 'Opponent'
        move = self.notakto.getAIMove(self.boards)
        print(move)
        
        board_key = move[0]
        i = int(move[1])
        
        self.notakto.makeMove(self.boards, move)
        self.board_labels[(board_key,i)]["text"]="X"
        self.board_labels[(board_key, i)].config(state="disabled")

        self.printBoards(self.boards)
        self.checkDeadBoard()
        self.checkGameOver()
        self.AIassist(board_key,move)

        
    def AIassist(self,board_key,i):
        print(self.boards)
        messagebox.showinfo('Assistant', notaktoGui.getNextMove(self.boards))
        

#Create GUI Start Window 
window = tk.Tk()
width = 800
height = 600
#window.geometry(f"{width}x{height}")
window.title("Notakto")
my_label = tk.Label(text=notaktoGui.intro(),
                    background = 'black',
                    foreground = 'white',
                    font=('Ariel', 20))
#Displays label
my_label.grid() 
play_area = tk.Frame(window, bg = 'black')
game = GameGUI(window)
#Create instance of GameGUI class

#Creates Play Button
play_button = tk.Button(text="PLAY", command = game.start_game_button)
play_button.grid(row = 3, column = 1, pady = 10, columnspan = 3)

window.mainloop()