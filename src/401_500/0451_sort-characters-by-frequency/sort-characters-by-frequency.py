class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if(not s):
            return s
        word_2_num = dict()    # word(key) -> count(value)
        num_2_word = dict() # count(key) -> word(value)
        res = ""
        for i in s:
            if(i not in word_2_num):
                word_2_num[i] = 1
            else:
                word_2_num[i] += 1
        for key in word_2_num.keys():
            num = word_2_num[key]
            if( num not in num_2_word):
                num_2_word[num] = [key]
            else:
                num_2_word[num].append(key)
        
        #iter num_2_word dict
        #print word_2_num
        #print num_2_word
        nums = sorted( num_2_word.keys() )
        for i in xrange(len(nums)-1,-1,-1):
            arr = num_2_word[nums[i]]  # get num_2_word -> value, value is list,like [a,b,c...]
            for c in arr:
                res += c*nums[i]
        return res