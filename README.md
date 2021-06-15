# SudokuAI

### Explanation of the problem

In this problem we need to solve 10 sudokus which they 9x9. According to definition we have 9x9 grid and for every cell we can have following domain X = {1,2,3,4,5,6,7,8,9}. In initial state some of the cells are prefilled so we need to fill remaining cellsthat satisfiesevery line, row mustconsist all elements of domain. In addition,our 9x9 gridiscreated by 9 different small 3x3 gridsshown in the initial state. So in every small 3x3 grid we also need to have every element of domaina least once, which means at most once at the same time.

photo

### Restrictions

n this problem the restrictions are following;

Let Xmand Xnare elements from the list {X1, X2,X3, ... , X81}. Also domain for any X from the list is {1,2,3,4,5,6,7,8,9}. So if Xm= Xnthen Xmand Xncan not be in the same row, same column or in the same small 3x3 grid. If Xm= Xnand they are in same column or same row or same small 3x3 grid then m = n.

Meaning of this restriction is we can use domain values only once in a row and only once in a column and once in small 3x3 grid. Since every column, row and small 3x3 grid has 9 space and domain has 9 elements, that means we can use one value at most once in a column, in a row and in a small 3x3 grid.





### State

A state is the situation of the table with some values inside or no values inside. We can check if a state is complete or not or satisfies sudoku requirements. We consider state as the situation of board because we can keep continue to find solution from a given state(situation of board). If given state is not suitable,we can backtrack to previous states to check all possible options.


### Initial State

Initial state is a sudoku grid with some numbers inside it. The grids also consist of0 values where there are no initial domain elements inside. We call this as an initial state because we need a given state to solve sudoku. Thus,the first given sudoku is our initial state. The filled numbers createrestrictions from the beginning but there is no need to be any given filled number for a sudoku but we can still come up with a solution. There is an example of initial state.

			Photo


### Possible Actions

We can calculate the possible actions from a given states. Possible action is the next statethat a grid consists of zero changed with an appropriate domain value if the given state is not complete. This is an example of possible action, but the other actions may be the other changes with zero consisted grid from appropriate domain values. This is a possible action because appropriate domain value means a value does not appears twice in the same column, row or small 3x3 grid which changed 0 valued grid cell located


### Maximum Branching Factor

The maximum branching factor of the tree is 9 because we have 9 unique values in our domain. We can see this situation when the row, column and small 3x3 grid of a given cell is all empty. In this case we can try all {1,2,3,4,5,6,7,8,9} values for the next state and all of the states will be valid as a next state. 
