class Solution(object):
	# 暴力(超时)
	def getMaxRepetitions(self, s1, n1, s2, n2):
		"""
		:type s1: str
		:type n1: int
		:type s2: str
		:type n2: int
		:rtype: int
		"""		
		num1 = 0
		num2 = 0
		s1_len = len(s1)
		s2_len = len(s2)
		index = 0
		while num1<n1:
			for i in xrange(s1_len):
				if s1[i]==s2[index]:
					if index==s2_len-1:
						index = 0
						num2 += 1
					else:
						index += 1
			num1 += 1
		return num2/n2



	# 优化后的循环判断
	def getMaxRepetitions(self, s1, n1, s2, n2):
		len1 = len(s1)
		len2 = len(s2)
		index1 = 0
		index2 = 0
		if len1==0 or len2==0 or len1*n1<len2*n2:
			return 0
		map1 = dict()
		map2 = dict()
		ans = 0
		while (index1/len1)<n1:
			if index1%len1 == len1-1:
				if index2%len2 in map1:
					val = map1[index2%len2]
					cycleLen = index1/len1 - val/len1
					cycleNum = (n1-1-index1/len1)/cycleLen
					cycleS2Num = index2/len2 - map2[index2%len2]/len2
					index1 += cycleNum *cycleLen * len1
					ans += cycleNum * cycleS2Num
				else:
					map1[index2%len2] = index1
					map2[index2%len2] = index2
			if s1[index1%len1]==s2[index2%len2]:
				if index2%len2==len2-1:
					ans += 1
				index2 += 1
			index1 += 1
		return ans/n2
		
		
		
	# 来自官方的题解
	def getMaxRepetitions(self, s1, n1, s2, n2):
		s1_len = len(s1)
		s2_len = len(s2)
		s1_count = 0
		s2_count = 0
		map = dict()
		index = 0
		while True:
			s1_count += 1
			for c in s1:
				if c==s2[index]:
					index += 1
					if index==s2_len:
						index = 0
						s2_count += 1
			if index in map:
				s1_pre,s2_pre = map[index]
				pre_loop = (s1_pre,s2_pre)
				in_loop = (s1_count-s1_pre, s2_count-s2_pre)
				break
			else:
				map[index] = (s1_count,s2_count)
		# ans 存储的是 S1 包含的 s2 的数量，考虑的之前的 pre_loop 和 in_loop
		ans = pre_loop[1] + (n1-pre_loop[0])//in_loop[0] * in_loop[1]
		# S1 的末尾还剩下一些 s1，我们暴力进行匹配
		rest = (n1 - pre_loop[0])% in_loop[0]
		for _ in xrange(rest):
			for c in s1:
				if c==s2[index]:
					index += 1
					if index==s2_len:
						index = 0
						ans += 1
		# S1 包含 ans 个 s2，那么就包含 ans / n2 个 S2
		return ans//n2
		
		