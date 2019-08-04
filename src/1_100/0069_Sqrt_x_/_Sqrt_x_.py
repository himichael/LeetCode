class Solution(object):
	def mySqrt(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		if(x == 0):
			return 0
		begin = 1
		end = x/2
		while(begin < end):
			mid = (begin+end+1)/2
			if(mid*mid > x):
				end = mid-1
			else:
				begin = mid
		return begin
		
	#返回浮点结果	
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x==0 or x==1):
            return x
        begin = 1
        end = x
        while(begin < end):
            mid = (begin+end+1)/2
            if(mid*mid > x):
                end = mid-1
            else:
                begin = mid
        return begin