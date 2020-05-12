class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__stack = []
        self.__min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.__stack.append(x)
        if(self.__min_stack):
            if(self.__min_stack[-1] >= x):
                self.__min_stack.append(x)
        else:
            self.__min_stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if(self.__stack and self.__min_stack):
            if(self.__stack[-1] == self.__min_stack[-1]):
                self.__stack.pop()
                self.__min_stack.pop()
            else:
                self.__stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if(self.__stack):
            return self.__stack[-1]
        return None
        

    def getMin(self):
        """
        :rtype: int
        """
        if(self.__min_stack):
            return self.__min_stack[-1]
        return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


## 用一个栈来实现
class MinStack(object):
    def __init__(self):
        self.stack = []

    def push(self, x):
        if not self.stack:
            self.stack.append(x)
            self.stack.append(x)
        else:
            val = self.stack[-1]
            self.stack.append(x)
            if val<=x:
                self.stack.append(val)
            else:
                self.stack.append(x)

    def pop(self):
        self.stack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-2]

    def getMin(self):
        return self.stack[-1]
		
		
		
## 用一个栈实现，python的元组写法，更简洁
class MinStack(object):
    def __init__(self):
        self.stack = []

    def push(self, x):
        if not self.stack:
            self.stack.append((x,x))
        else:
            self.stack.append((x,min(self.stack[-1][1],x)))

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]		
		
		
