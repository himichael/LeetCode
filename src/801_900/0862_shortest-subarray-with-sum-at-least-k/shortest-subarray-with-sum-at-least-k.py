class Solution(object):
    def shortestSubarray(self, A, K):
        p = [0]
        for x in A:
            p.append(p[-1] + x)
        queue = collections.deque()
        res = float("inf")
        for i in xrange(len(p)):
            while queue and p[queue[-1]] >= p[i]:
                queue.pop()
            while queue and p[i] - p[queue[0]] >= K:
                res = min(res, i - queue.popleft())
            queue.append(i)
        return res if res <= len(A) else -1