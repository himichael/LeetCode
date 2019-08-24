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
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if(not board or not board[0]):
            return []
        if(not words):
            return []
        
        self.__trie = Trie()
        self.__n = len(board)
        self.__m = len(board[0])
        self.__res = set()
        for word in words:
            self.__trie.insert(word)
            
        for i in xrange(self.__n):
            for j in xrange(self.__m):
                self.__dsf(i,j,board,"")
        return list(self.__res)
        
        
        
    def __dsf(self,i,j,board,cur_word):    
        cur_word += board[i][j]
        if(not self.__trie.is_star_with(cur_word)):
            return
        if(self.__trie.search(cur_word)):
            self.__res.add(cur_word)
        
        tmp,board[i][j] = board[i][j],"$"
        for k in xrange(4):
            x = i + dx[k]
            y = j + dy[k]
            if(0<=x<self.__n and 0<=y<self.__m and board[x][y]!="$"):
                self.__dsf(x,y,board,cur_word)
        board[i][j] = tmp
        