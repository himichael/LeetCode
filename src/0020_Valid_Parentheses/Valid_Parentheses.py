class Solution(object):
    def isValid(self, s):   
		stack = []
		m = {'(': ')', '[': ']', '{': '}'}
		for i in s:
			if(i in m.keys()):
				stack.append(i)
			elif(len(stack)==0):
				return False
			else:
				tmp = stack.pop()
				if(i != m[tmp]):
					return False;		
		return not len(stack)