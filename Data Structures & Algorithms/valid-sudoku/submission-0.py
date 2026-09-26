class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        for row in range(9): #check rows
            num_set = set()
            for j in range(9):
                if board[row][j] == '.':
                    continue
                if board[row][j] in num_set:
                    return False
                num_set.add(board[row][j])

        for col in range(9):
            num_set = set()
            for j in range(9):
                if board[j][col] == '.':
                    continue
                if board[j][col] in num_set:
                    return False
                num_set.add(board[j][col])
        
        for square in range(9):
            num_set = set()
            for i in range(3): # need a way to get 9 -> 1, 2, 3
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in num_set:
                        return False
                    num_set.add(board[row][col])
        return True