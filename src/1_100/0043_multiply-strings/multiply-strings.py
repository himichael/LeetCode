class Solution(object):

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if(num1=="0" or num2=="0"):
            return "0"
        d = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
        num_arr = ["0","1","2","3","4","5","6","7","8","9"]
        
        def multiply(a,b):
            n = d[a]
            carry = 0
            res = ""
            for i in b[::-1]:
                tmp = n * d[i]
                tmp += carry
                carry = tmp/10
                tmp %= 10
                res = num_arr[tmp] + res
            if(carry > 0):
                return num_arr[carry]+res
            return res
        
        def fill_zero(num,count):
            if(count == 0):
                return num
            for _ in range(count):
                num += "0"
            return num
        
        def add(a,b):
            i = len(a)-1
            j = len(b)-1
            res = ""
            carry = 0
            while(i>=0 or j>=0):
                tmp = carry
                if(i >= 0):
                    tmp += d[a[i]]
                if(j >= 0):
                    tmp += d[b[j]]
                carry = tmp/10
                tmp %= 10
                res = num_arr[tmp] + res
                i -= 1
                j -= 1
            if(carry > 0):
                return num_arr[carry]+res
            return res
        
        index = 0
        nums = []
        for i in num1[::-1]:
            nums.append( fill_zero(multiply(i,num2),index) )
            index += 1
        #print nums
        if(len(nums)==1):
            return nums[0]
        res = nums.pop(0)
        for i in nums:
            res = add(res,i)
        return res


    def multiply_2(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str( int(num1)*int(num2) )