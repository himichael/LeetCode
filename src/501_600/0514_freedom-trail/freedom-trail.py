class Solution(object):
    def findRotateSteps(self, ring, key):
        n = len(ring)
        m = len(key)
        d = {}
        def find(i,j):
            left,left_count,right,right_count = i,0,i,0
            while ring[left] != key[j]:
                left,left_count = left - 1, left_count + 1
                if left == -1:
                    left = n - 1
            while ring[right] != key[j]:
                right,right_count = right + 1, right_count + 1
                if right == n:
                    right = 0
            return left,left_count,right,right_count
        def search(i,j):
            if (i,j) in d:
                return d[i,j]
            if j == m:
                return 0
            left,left_count,right,right_count = find(i,j)
            a = search(left, j + 1) + left_count + 1
            b = search(right, j + 1) + right_count + 1
            d[i,j] = min(a,b)
            return d[i,j]
        return search(0,0)