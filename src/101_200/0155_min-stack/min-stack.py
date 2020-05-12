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
        self.inner = []

    def push(self, x):
        if len(self.inner)==0 or self.inner[-1]>=x:
            self.inner.append(x)
        self.stack.append(x)

    def pop(self):
        val = self.stack.pop()
        if val==self.inner[-1]:
            self.inner.pop()
        return val

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.inner[-1]
		
