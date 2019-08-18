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