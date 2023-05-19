# Notakto_AI_Assist
481 Project. AI Assistance for the game Notakto

Running the file Noktato.py will simulate a game of Noktato in the console. 
The opponent will take the first move then prompt the user to make a move among 
the list of suggested moves provided by the assistant. 
**games.py contains minmax algorithms used in Notakto

# How To Play
1. Both Players Utilize 'X' as their mark
2. The Player that completes the **last** board with 3 X's in a row loses.
3. The User will enter in a valid Cell# to make their mark.
4. When a board is completed, it is removed from the space

** An AI Assistant is provided, guiding the user on how to win

The user may exit the game at any time with the command 'Ctrl + C' 
Once the game is over, user has the choice to play again with response 'y' or 'n'.

## tkinterGUI.py
Running the file tkinterGUI.py will open a window for the user to start the game. 
Press 'Play' to start the game. **This only lets you play once.

The GUI follows a similar simulation to Notakto.py running on the console. 
GUI is missing features such as displaying the opponent's move as a pop up window, resetting the game if user 
continues to play, and closing the window once the game has ended. 


