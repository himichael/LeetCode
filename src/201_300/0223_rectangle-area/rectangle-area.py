class Solution(object):
	def computeArea(self, A, B, C, D, E, F, G, H):
		"""
		:type A: int
		:type B: int
		:type C: int
		:type D: int
		:type E: int
		:type F: int
		:type G: int
		:type H: int
		:rtype: int
		"""			
		if(A>E):
			return self.computeArea(E,F,G,H,A,B,C,D)
		
		ab_cd = abs(A-C) * abs(B-D)
		ef_gh = abs(E-G) * abs(F-H)
		if(D<=F or B>=H or E>=C):
			return ab_cd + ef_gh
		
		x_left = max(A,E)
		y_left = max(B,F)
		x_right = min(C,G)
		y_right = min(D,H)
		
		overlap = abs(x_left-x_right) * abs(y_left-y_right)
		return ab_cd + ef_gh - overlap
    
    
    
    