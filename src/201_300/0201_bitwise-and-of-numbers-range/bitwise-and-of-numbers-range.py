class Solution:
    def rangeBitwiseAnd(self, m, n):
        while m < n:
            # 抹去最右边的 1
            n = n & (n - 1)
        return n



	# 求前缀
    def rangeBitwiseAnd(self, m,n):
        cnt = 0
        while m!=n:
            m >>= 1
            n >>= 1
            cnt += 1
        return n << cnt