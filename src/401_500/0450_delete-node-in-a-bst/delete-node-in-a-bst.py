# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if(root==None):
            return root
        p = root
        if(p.val == key):
            left = p.left
            right = p.right
            cur = right
            if(cur==None):
                p.right = left
            else:
                while(cur!=None):
                    if(cur.left != None):
                        cur = cur.left
                    else:
                        break
                if(cur!=None):
                    cur.left = left
            return p.right
            
        is_left = True
        while(p):
            if(key < p.val):
                if(p.left!=None and p.left.val==key):
                    break
                else:
                    p = p.left
            elif(key > p.val):
                if(p.right!=None and p.right.val==key):
                    is_left = False
                    break
                else:
                    p = p.right
        if(p==None):
            return root
        to_be_deleted_node = p.left
        if(not is_left):
            to_be_deleted_node = p.right
        
        deleted_left = to_be_deleted_node.left
        deleted_right = to_be_deleted_node.right
        if(is_left):
            if(deleted_right):
                p.left = deleted_right
            else:
                p.left = deleted_left
                return root
        else:
            if(deleted_right):
                p.right = deleted_right
            else:
                p.right = deleted_left
                return root
        
        cur = deleted_right
        while(cur!=None):
            if(cur.left != None):
                cur = cur.left
            else:
                break
        cur.left = deleted_left
        return root    


	# 新实现方式
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root
        if root.val==key:
            if not root.left and not root.right:
                return None
            elif not root.left and root.right:
                return root.right
            elif root.left and not root.right:
                return root.left
            head = root.right
            p = head
            while p.left:
                p = p.left
            p.left = root.left
            return head
        d = dict()
        p = root
        node = None
        while p:
            if p.val>key and p.left:
                d[p.left] = p
                p = p.left
            elif p.val<key and p.right:
                d[p.right] = p
                p = p.right
            else:
                node = p
                break
        if not node:
            return root
        if node.val!=key:
            return root
        parent = d[node]
        #print "pareint->"+str(parent.val)
        #print "node->"+str(node.val)
        if node.left and node.right:
            print ""
            p = node.right
            while p.left:
                p = p.left
            p.left = node.left
            if parent.left==node:
                parent.left=node.right
            else:
                parent.right=node.right
        elif node.left and not node.right:
            print node.left.val
            if parent.left==node:
                parent.left=node.left
            else:
                parent.right=node.left
        elif not node.left and node.right:
            if parent.left==node:
                parent.left=node.right
            else:
                parent.right=node.right
        else:
            if parent.left==node:
                parent.left=None
            else:
                parent.right=None
        return root











		
