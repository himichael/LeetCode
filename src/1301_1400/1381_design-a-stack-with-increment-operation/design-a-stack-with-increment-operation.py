class CustomStack(object):
    def __init__(self, maxSize):
        self.arr = []
        self.size = maxSize


    def push(self, x):
        if len(self.arr)>=self.size:
            return
        self.arr.append(x)


    def pop(self):
        if len(self.arr)==0:
            return -1
        return self.arr.pop()


    def increment(self, k, val):
        if len(self.arr)==0:
            return
        size = min(len(self.arr),k)
        for i in xrange(size):
            self.arr[i] += val



# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)