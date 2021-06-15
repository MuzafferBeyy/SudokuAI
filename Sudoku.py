"""
This code solves 10 sudoku under 1 seconds by creating search trees and back tracking method.
"""

#create matrix

import numpy as np

f = open("/content/Assignment 2 sudoku.txt", "r")

lines = f.readlines()

sudokus = []
c = 0
temp = []
for i in lines[4:]:

  temp.append(i)
  c += 1 
  if c == 11:
    sudokus.append(temp)
    temp = []
    c=0

mat = []
temp = []

final_sudokus = []

for s in range(10):
  arr = []
  mat = []
  for i in sudokus[s][1:]:
    for j in i:
      if "0" <= j <= "9":
        temp.append(int(j))
    if temp:
      mat.append(temp.copy())
      temp=[]
  arr = np.array(mat)

  final_sudokus.append(arr)


"""
for i in final_sudokus:
  print(i)
  print()"""


# Find solution

from copy import copy, deepcopy
import time

def selectUnass(state):
  c = 1
  for i in state:
    for j in i:
      if j==0:
        row = int((c-1)/9)
        col = (c-1)%9
        return (row,col)
      c +=1


      

def findDom(state,row,col):
  dom = []

  i = int(row/3)
  j = int(col/3)

  k = 0

  vec = [0,0,0,0,0,0,0,0,0,0]#use this vector to search

  


  for x in range(3):
    for y in range(3):
      #l = state[x+(i*3)][y+(j*3)]
      vec[state[x+(i*3)][y+(j*3)]] = 1
      vec[state[row][k]] = 1
      vec[state[k][col]] = 1
      k +=1 


  for i in range(1,10):
    if vec[i] == 0:
      dom.append(i)


  return dom



def mat_copy(original):#use deep copy function
  copy = []
  for i in original:
    copy.append(i.copy())
  return copy



def print_mat(mat):
  for i in mat:
    print(i)


# check function times



def back_track(state):

  prev_state = []
 
  prev_state = mat_copy(state)
  
  unass = selectUnass(state)#just print x,y coordinates

  if unass:
    

    domain = findDom(state,unass[0],unass[1])



    for i in domain:

      state[unass[0]][unass[1]] = i#state_update(state,i,unass)
      
      result = back_track(state)
  
      if result:
        return result

      else:
        state = mat_copy(prev_state)
       
  else:
    return state



back_track(state)

#Find solution in 10 matrix

count = 1
for mat in final_sudokus:
  print("Sudoku",count)
  print_mat(back_track(mat))
  count += 1
  print()

