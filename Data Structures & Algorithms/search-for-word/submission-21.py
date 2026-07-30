class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def path(index: int, x: int, y: int, used: List) -> bool:
            if (index == len(word)):
                return True
            elif used and (x, y) in used:
                return False
            elif (x == -1 or x == len(board) or y == -1 or y == len(board[0])):
                return False
            elif board[x][y] != word[index]:
                return False
            else:
                used.append((x, y))
                found = (path(index+1, x+1, y, used) or 
                path(index+1, x-1, y, used) or
                path(index+1, x, y+1, used) or path(index+1, x, y-1, used))
                used.pop()
                return found            
    
        ans = False
        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if (char == word[0]):
                   ans = path(0, i, j, [])
                   if (ans == True):
                        return ans

        return ans
