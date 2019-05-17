class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        handreds_digit = False
        ten_digit = False
        digits = False
		
		#每次迭代一位，如果碰到是C,X,I要做特殊处理，此时记录一个标志位，下次迭代的时候检查这个标记为
		#然后再检查相应的字符是否满足匹配
        for i in s:
            if(handreds_digit):
                handreds_digit = False
                if(i == "M"):
                    num += 800
                    continue
                if(i == "D"):
                    num += 300
                    continue
            if(ten_digit):
                ten_digit = False
                if(i == "C"):
                    num += 80
                    continue
                if(i == "L"):
                    num += 30
                    continue
            if(digits):
                digits = False
                if(i == "X"):
                    num += 8
                    continue
                if(i == "V"):
                    num += 3
                    continue
                
            if(i == "M"):
                num += 1000
            if(i == "D"):
                num += 500
            if(i == "C"):
                num += 100
                handreds_digit = True
            if(i == "L"):
                num += 50
            if(i == "X"):
                num += 10
                ten_digit = True
            if(i == "I"):
                num += 1
                digits = True
            if(i == "V"):
                num += 5
        #end for
        return num
        