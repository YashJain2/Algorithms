# Python Program to Solve N - Queens Problem

'''
What is N - Queens Problem ?

You are given a N * N chess board and there are N queens. You have to place the queens in the board
such that no queens attack each other.

How do they attack ?

If one queen is placed in a cell, No other queen should be placed

-> In the same row
-> In the same column
-> In the same diogonals (Both and left diogonals)

Eg: N=3

Q - -
- - -
- - -

Q1 is placed in (0,0)
you cannot place other queens in 
board[0][0],board[0][1],board[0][2]     (same row)
board[1][0], board[2][0]                (same column)
board[1][1] ,board[2][2]                 (Diogonal)

]


Approach :

Try All possible cases.

How ? 

First place a queen in one cell and then go find a place for the next queen such that it does not 
attack the first one or vice versa,if you found such a position ,take the next queen and do the same,
else come back and place the first queen in some other position and continue.

By doing so if you don't find such a position return -1;

'''

#Code

#Number of queens
print ("Enter the number of queens")
N = int(input())

#chessboard
#NxN matrix with all elements 0
board = [[0]*N for _ in range(N)]

'''
Diagonal Property :

Right Diogonal :
 The sum of i and j is constant and unique for each right diagonal where i is the row of element and j is the
column of element.

Left Diogonal :
The difference of i and j is constant and unique for each left diagonal where i and j are row and column of element respectively.

'''

""" left_diogonal is an array where its indices indicate row-col+N-1  
(N-1) is for shifting the difference to store negative  
indices """
left_diogonal = [0] * 30
  
""" right_diogonal is an array where its indices indicate row+col  
and used to check whether a queen can be placed on  
right diagonal or not"""
right_diogonal = [0] * 30
  
"""column array where its indices indicates column and  
used to check whether a queen can be placed in that  
    row or not"""
column = [0] * 30

#A utility function to print solution """
def printSolution(board):  
    for i in board: 
        print(i)
  
# A recursive utility function to solve N Queen problem 
def solveNQUtil(board, col):  
      
    # If all queens are placed then return True 
    if (col >= N): 
        return True
          
    #Consider this column and try placing this queen in all rows one by one
    for i in range(N): 
          
          #Condition to check if the queen can be placed here such that it does not attack the other placed queens
        if ((left_diogonal[i - col + N - 1] != 1 and 
             right_diogonal[i + col] != 1) and column[i] != 1): 
                   
            #Place this queen in board[i][col] 
            board[i][col] = 1
            left_diogonal[i - col + N - 1] = right_diogonal[i + col] = column[i] = 1
              
            # recur to place rest of the queens 
            if (solveNQUtil(board, col + 1)): 
                return True
                  
            # If placing queen in board[i][col]  doesn't lead to a solution,  then remove queen from board[i][col] """
            board[i][col] = 0 # BACKTRACK  
            left_diogonal[i - col + N - 1] = right_diogonal[i + col] = column[i] = 0
              
    # If the queen cannot be placed in any row in this colum col then return False
    return False
      

#Function prints the solution if it is possible to place N queens int the board,else prints SOlution does not exist
def solveNQ(): 
    if (solveNQUtil(board, 0) == False): 
        print("Solution does not exist") 
        return False
    printSolution(board) 
    return True
      
# Driver Code 
solveNQ()  


'''
Input:

Enter the number of queens
4

Output:

[0, 1, 0, 0]
[0, 0, 0, 1]
[1, 0, 0, 0]
[0, 0, 1, 0]


Enter the number of queens
3

Output:

Solution does not exist


'''

#Time Complexity : O (2^N)