class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        digit = []
        letter = []
        for i in s:
            if i.isdigit():
                digit.append(i)
            else:
                letter.append(i)
        n = len(digit)
        m = len(letter)
        if abs(n-m)>1:
            return ""
        i,j = 0,0
        res = []
        while i<n and j<m:
            if n<=m:
                res.append(letter[j])
                res.append(digit[i])
            else:
                res.append(digit[i])
                res.append(letter[j])
            i += 1
            j += 1
        if i<n:
            res.append(digit[i])
        if j<m:
            res.append(letter[j])
        return "".join(res)