class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.dummy = Node(-1)

        
    def print_info(self,info):
        s = ""
        p = self.dummy
        while p:
            if p==self.dummy:
                s = s+"dummy->"
            else:
                s = s +str(p.val)+"-->"
            p = p.next
        print info+" ### "+s
        
        
    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        #self.print_info("get")
        if index<0 or index>self.size:
            return -1
        p = self.dummy
        k = 0
        while p and p.next and k<index:
            p = p.next
            k += 1
        if not p or not p.next:
            return -1
        return p.next.val
            

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """        
        cur = Node(val)
        cur.next = self.dummy.next
        self.dummy.next = cur
        self.size += 1
        #self.print_info("addAtHead")
        
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        cur = Node(val)
        p = self.dummy
        while p and p.next:
            p = p.next
        p.next = cur
        self.size += 1
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if(index>self.size):
            return
        if(index==self.size):
            self.addAtTail(val)
            return
        if(index<0):
            self.addAtHead(val)
            return
        k = 0
        cur = self.dummy
        n = Node(val)
        while cur and cur.next and k<index:
            cur = cur.next
            k += 1
        n.next = cur.next
        cur.next = n
        self.size += 1
        #self.print_info("addAtIndex")


    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if(index<0 or index>=self.size):
            return
        cur = self.dummy
        k = 0
        while cur and cur.next and k<index:
            cur = cur.next
            k += 1
        if cur.next:
            cur.next = cur.next.next
        self.size -=1
        #self.print_info("deleteAtIndex")


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)