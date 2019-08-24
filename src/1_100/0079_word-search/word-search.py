class Trie(object):
    def __init__(self):
        self.__root = {}
        self.__end_word = "#"
    
    def insert(self,word):
        node = self.__root
        for c in word:
            node = node.setdefault(c,{})
        node[self.__end_word] = self.__end_word
    
    def is_star_with(self,prefix):
        node = self.__root
        for c in prefix:
            if(c not in node):
                return False
            node = node[c]
        return True
    
    def search(self,word):
        node = self.__root
        for c in word:
            if(c not in node):
                return False
            node = node[c]
        return (self.__end_word in node)


dx = [-1,1,0,0]
dy = [0,0,-1,1]
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if(not board or not board[0]):
            return False
        if(not word):
            return False
        
        self.__trie = Trie()
        self.__n = len(board)
        self.__m = len(board[0])
        self.__res = set()
        self.__is_ok = False
        for c in [word]:
            self.__trie.insert(c)
            
        for i in xrange(self.__n):
            if(word[0] in board[i]):
                j = 0
                while(j < self.__m):
                    if(word[0]==board[i][j]):
                        self.__dfs(i,j,board,"")
                    j += 1
        if(len(self.__res)>0):
            return True
        return False
    
    
    def __dfs(self,i,j,board,cur_word):    
        cur_word += board[i][j]
        if(not self.__trie.is_star_with(cur_word)):
            return
        if(self.__trie.search(cur_word)):
            self.__res.add(cur_word)
            self.__is_ok = True
            return
        tmp,board[i][j] = board[i][j],"$"
        for k in xrange(4):
            x = i + dx[k]
            y = j + dy[k]
            if(0<=x<self.__n and 0<=y<self.__m and board[x][y]!="$"):
                self.__dfs(x,y,board,cur_word)
                if( self.__is_ok ):
                    return
        board[i][j] = tmp    