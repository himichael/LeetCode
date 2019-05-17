class Solution(object):
    nums = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    roma = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

	#创建两个数组，然后将数字num 和数组nums中的值比较，如果大于nums[i] 就减去这个值，并将对应的roma[i]加到 结果res中
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ""
        for i in range(len(self.nums)):
            while(num >= self.nums[i]):
                res += self.roma[i]
                num -= self.nums[i]
        return res