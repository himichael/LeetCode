﻿class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if(s==None or len(s)==0 or words==None or len(words)==0):
            return []
        word_dict = dict()
        for w in words:
            if(word_dict.has_key(w)):
                word_dict[w] += 1
            else:
                word_dict[w] = 1
        word_arr_size = len(words) * len(words[0])
        single_word_size = len(words[0])
        res = []
        for i in range(len(s)-word_arr_size+1):
            tmp_str= s[i:i+word_arr_size]
            d = dict(word_dict)
            for j in range(0,len(tmp_str),single_word_size):
                key = tmp_str[j:j+single_word_size]
                if(d.has_key(key)):
                    if(d[key] <= 0):
                        break
                    else:
                        d[key] -= 1
                        if(d[key] == 0):
                            del d[key]
                else:
                    break
            if(len(d)==0):
                res.append(i)    
        return res
		
		
		
	# 精简代码	
	def findSubstring_2(self, s, words):
		"""
		:type s: str
		:type words: List[str]
		:rtype: List[int]
		"""
		if not s or len(s)==0 or not words or len(words)==0:
			return []
		words_map,res = dict(),[]
		for i in words:
			if i not in words_map:
				words_map[i] = 1
			else:
				words_map[i] += 1
		one_word_size = len(words[0])
		all_words_size = len(words)*one_word_size
		for i in xrange(len(s)-all_words_size+1):
			tmp_str,d = s[i:i+all_words_size],dict(words_map)
			for j in xrange(0,len(tmp_str),one_word_size):
				key = tmp_str[j:j+one_word_size]
				if key in d:
					d[key] -= 1
					if d[key]==0:
						del d[key]
				else:
					break
			if not d:
				res.append(i)
		return res