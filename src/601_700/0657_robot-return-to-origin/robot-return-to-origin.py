class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if(moves==None or len(moves)==0):
            return True
        x = 0
        y = 0
        x_dict = {"L":-1,"R":1}
        y_dict = {"U":1,"D":-1}
        for i in moves:
            if(x_dict.has_key(i)):
                x += x_dict[i]
            if(y_dict.has_key(i)):
                y += y_dict[i]
        return (x==0) and (y==0)