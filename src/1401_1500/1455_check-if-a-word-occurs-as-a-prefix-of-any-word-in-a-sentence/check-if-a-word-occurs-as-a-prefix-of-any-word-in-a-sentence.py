class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        if not (sentence and searchWord):
            return -1
        arr = sentence.split(" ")
        index = 0
        n = len(arr)
        while index<n:
            if arr[index].startswith(searchWord):
                return index+1
            index += 1
        return -1    