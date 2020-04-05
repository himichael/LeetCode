class Node(object):
    def __init__(self,key,val):
        self.pre = None
        self.next = None
        self.key = key
        self.val = val
    
        
class LinkList(object):
    def __init__(self):
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.pre = self.tail
        self.head.next = self.tail
        self.tail.pre = self.head
        self.tail.next = self.head
        
    def add_to_first(self,node):
        node.next = self.head.next
        self.head.next.pre = node
        node.pre = self.head
        self.head.next = node
    
    def delete(self,node):
        pre_node = node.pre
        next_node = node.next
        pre_node.next = next_node
        next_node.pre = pre_node
        node.pre = None
        node.next = None
    
    def remove_last(self):
        if(self.tail.pre==self.head):
            return
        node = self.tail.pre
        node.pre.next = self.tail
        self.tail.pre = node.pre
        node.pre = None
        node.next = None
        
    def get_last(self):
        return self.tail.pre

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.remain = capacity
        self.d = dict()
        self.link_list = LinkList()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if(key not in self.d):
            return -1
        node = self.d[key]
        self.link_list.delete(node)
        self.link_list.add_to_first(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if(key in self.d):
            node = self.d[key]
            if(node.val != value):
                self.link_list.delete(node)
                node = Node(key,value)
                self.d[key] = node    
            else:
                self.link_list.delete(node)
            self.link_list.add_to_first(node)
            return
            
        node = Node(key,value)
        if(self.remain > 0):
            self.remain -= 1
            self.d[key] = node
            self.link_list.add_to_first(node)
        else:
            tmp = self.link_list.get_last()
            del self.d[tmp.key]
            self.link_list.remove_last()
            self.link_list.add_to_first(node)
            self.d[key] = node
        
        
	#精简了put部分的代码	
    def put_2(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """        
        if(key in self.cache):
            tmp = self.cache[key]
            self.link_list.delete(tmp)
            del self.cache[tmp.key]
        else:
            if self.size==0:
                return
            if(self.remain > 0):
                if(key not in self.cache):
                    self.remain -=1
            else:
                tmp = self.link_list.get_last_node()
                del self.cache[tmp.key]
                self.link_list.delete(tmp)
        node = Node(key,value)
        self.cache[key] = node
        self.link_list.add_to_first(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



# 用库函数实现
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        import collections 
        self.d = collections.OrderedDict()
        self.size = capacity
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if(key in self.d):
            value = self.d[key]
            del self.d[key]
            self.d[key] = value
            return value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if(key in self.d):
            del self.d[key]
            self.d[key] = value
        else:
            if(len(self.d)==self.size):
                self.d.popitem(False)
        self.d[key] = value








