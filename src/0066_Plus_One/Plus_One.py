class Solution(object):
    def plusOne(self, c):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry_index=False
        for i in range(len(c)-1,-1,-1):
            if (not carry_index):
                if c[i]==9:
                    c[i]=0
                    carry_index=True
                else:
                    c[i]+=1
                    carry_index=False
                    break
            else:
                if c[i]==9:
                    carry_index=True
                    c[i]=0
                else:
                    c[i]+=1
                    carry_index=False
                    break
        if carry_index:
            c.insert(0,1)
        return c