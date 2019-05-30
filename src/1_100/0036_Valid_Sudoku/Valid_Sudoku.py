class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        s = [[set() for i in range(3)] for j in range(3)]
        for i in range(len(board)):
            horizontal = set()
            vertical = set()
            for j in range(len(board[i])):
                #横线方向的set，每次横向遍历时候检查是否在set中
                if(board[i][j] in horizontal):
                    return False
                elif(board[i][j] != "."):
                    horizontal.add(board[i][j])
                
                #竖线方向的set，每次迭代 board[j][i]时候检查是否在set中
                if(board[j][i] in vertical):
                    return False
                elif(board[j][i] != "."):
                    vertical.add(board[j][i])
                
                #定义9个set，i的范围是0-9, j的范围也是0-9
                #将i/3，j/3就确定了对应的是哪个set
                #比如board[0][0],board[0][1].... board[2][2]都是在s[i/3][j/3]中，也就是s[0][0]中
                if(board[i][j] in s[i/3][j/3]):
                    return False
                elif(board[i][j] != "."):
                    s[i/3][j/3].add(board[i][j])
                
            horizontal.clear()
            vertical.clear()
        return True