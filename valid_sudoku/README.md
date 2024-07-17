# 36. Valid Sudoku

https://leetcode.com/problems/valid-sudoku/

## Description

```
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

 

Example 1:

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

 

Constraints:

    board.length == 9
    board[i].length == 9
    board[i][j] is a digit 1-9 or '.'.

```

## Solution

```python
def isValidSudoku(self, board: List[List[str]]) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)

    for row in range(9):
        for col in range(9):
            curr = board[row][col]
            if curr == '.':
                continue
            if curr in rows[row] or curr in cols[col] or curr in squares[(row//3, col//3)]:
                return False
            rows[row].add(curr)
            cols[col].add(curr)
            squares[(row//3, col//3)].add(curr)
    
    return True
```

## Explanation

Build a set for the 3 conditions to satisify a valid sudoku, a set for rows a set for columns and a set for 3x3 squares in the grid.  As we iterate through the sudoku board if we have a valid value we first check if the value has been added to it's corresponding data structure if it has we can immediately return False as we have a duplicate and thus invalid board.  if not then we can add it to our defaultdict sets.

To calculate the positions for each 3x3 grid, we can perform simple integer division
Checking each edge case to ensure where the first grid is in range 0-2 in both directions.

0//3 = 0
2//3 = 0

3//3 = 1
5//3 = 1

6//3 = 2
8//3 = 2

This will form the basis of our 3x3 blocks in the grid so our squares key becomes squares[(row // 3, col // 3)] = value


## Analyze Complexity

Time complexity: O(1) as the board will always be constant 9x9

Space Complexity: O(1) Each container will consistently only hold at most 9 elements.