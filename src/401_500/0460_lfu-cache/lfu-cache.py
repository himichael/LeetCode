class Node(object):
    def __init__(self,key=None,value=None,freq=0):
        self.key = key
        self.val = value
        self.freq = freq
        self.pre = None
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head

    def insertFirst(self,node):
        node.next = self.head.next
        self.head.next.pre = node
        node.pre = self.head
        self.head.next = node

    def delete(self,node):
        if self.head.next==self.tail:
            return
        node.pre.next = node.next
        node.next.pre = node.pre
        node.next = None
        node.pre = None

    def getLast(self):
        if self.head.next==self.tail:
            return None
        return self.tail.pre

    def isEmpty(self):
        return self.head.next==self.tail

class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.keyMap = dict()
        self.freqMap = dict()
        self.minFreq = 0
        self.size = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.keyMap:
            return -1
        node = self.keyMap[key]
        self.__increment(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.keyMap:
            node = self.keyMap[key]
            node.val = value
            self.__increment(node)
        else:
            if self.size==0:
                return
            if len(self.keyMap)==self.size:
                self.__removeMinFreqElement()
            node = Node(key,value,1)
            self.__increment(node,True)
            self.keyMap[key] = node 

    def __increment(self,node,is_new_node=False):
        if is_new_node:
            self.minFreq = 1
            self.__setDefaultLinkedlist(node)
            return
        self.__deleteNode(node)
        node.freq += 1
        self.__setDefaultLinkedlist(node)
        if self.minFreq not in self.freqMap:
            self.minFreq +=1

    def __deleteNode(self,node):
        if node.freq not in self.freqMap:
            return
        linkedList = self.freqMap[node.freq]
        linkedList.delete(node)
        if linkedList.isEmpty():
            del self.freqMap[node.freq]

    def __setDefaultLinkedlist(self,node):
        if node.freq not in self.freqMap:
            self.freqMap[node.freq] = LinkedList()
        linkedList = self.freqMap[node.freq]
        linkedList.insertFirst(node)

    def __removeMinFreqElement(self):
        linkedList = self.freqMap[self.minFreq]
        node = linkedList.getLast()
        del self.keyMap[node.key]
        linkedList.delete(node)
        if linkedList.isEmpty():
            del self.freqMap[self.minFreq]



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)