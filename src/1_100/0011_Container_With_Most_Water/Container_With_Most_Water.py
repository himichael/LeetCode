class Solution(object):
	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		begin = 0
		end = len(height)-1
		res = 0
		#这题是要计算数组中第i位和第j位之间的距离 * min(abs(j-i))
		#利用两个指针begin和end不断向中间移动，每次记录面积并和上一次的最大面积比较
		while(begin < end):
			smaller_line = min(height[begin],height[end])
			difference = end - begin
			area = smaller_line * difference
			res = max(res,area)
			#水位的面积取决于较小的那个值，所以每次移动较小的值即可，begin向右移动，end向左移动
			if(height[begin] <= height[end]):
				begin += 1
			else:
				end -= 1
		return res