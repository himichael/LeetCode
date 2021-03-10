class Solution(object):
    def maxEnvelopes(self, envelopes):
        s = sorted(envelopes, key = lambda x : (x[0], -x[1]))
        n = len(s)
        dp = []
        for i in range(n):
            target = s[i][1]
            if not dp or dp[-1] < target:
                dp.append(target)
                continue
            begin, end = 0, len(dp) - 1
            while begin <= end:
                mid = begin + (end - begin) // 2
                if dp[mid] > target:
                    end = mid - 1
                elif dp[mid] < target:
                    begin = mid + 1
                else:
                    begin = mid
                    break
            dp[begin] = target
        return len(dp)