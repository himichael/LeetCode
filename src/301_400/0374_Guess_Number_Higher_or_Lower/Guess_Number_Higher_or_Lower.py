# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
	def guessNumber(self, n):
		begin = 0
		end = n
		while(begin <= n):
			middle = (begin+end)/2
			g = guess(middle)
			if(g == 1):
				begin = middle+1
			elif(g == -1):
				end = middle-1
			else:
				return middle
		return -1
        