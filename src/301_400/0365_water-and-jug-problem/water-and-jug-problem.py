class Solution(object):
	def canMeasureWater(self, x, y, z):
		"""
		:type x: int
		:type y: int
		:type z: int
		:rtype: bool
		"""		
		stack = [(0,0)]
		mem = set()
		while stack:
			remain_x,remain_y = stack.pop()
			if remain_x==z or remain_y==z or remain_x+remain_y==z:
				return True
			if (remain_x,remain_y) in mem:
				continue
			mem.add((remain_x,remain_y))
			# 把 x 装满	
			stack.append( (x,remain_y) )
			# 把 y 装满
			stack.append( (remain_x,y) )
			# 把 x 倒空
			stack.append( (0,remain_y) )
			# 把 y 倒空
			stack.append( (remain_x,0) )
			
			# 把 x 倒入 y 中
			move_size = min(remain_x, y-remain_y)
			stack.append( (remain_x-move_size, remain_y+move_size) )
			
			# 把 y 倒入 x 中
			move_size = min(remain_y, x-remain_x)
			stack.append( (remain_x+move_size, remain_y-move_size) )
		return False
		
		
	# 根据 贝祖定理 计算求得
	def canMeasureWater(self, x, y, z):	
		if x+y<z:
			return False
		if x==0 or y==0:
			return z==0 or x+y==z
		def gdc(a,b):
			if not b: return a
			return gdc(b,a%b)
		return z%gdc(x,y)==0
		
		