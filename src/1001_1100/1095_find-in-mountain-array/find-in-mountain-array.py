# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        n = mountain_arr.length();
        def find_peek_idx():
            begin = 0
            end = n-1
            while begin<=end:
                mid = begin+(end-begin)//2
                mid_left_val = mountain_arr.get(mid-1)
                mid_val = mountain_arr.get(mid)
                mid_right_val = mountain_arr.get(mid+1)
                if mid_left_val<mid_val and mid_val>mid_right_val:
                    return mid
                if mid_left_val<mid_right_val:
                    begin = mid
                else:
                    end = mid
            return -1
        def binary_search(begin,end):
            while begin<=end:
                mid = begin+(end-begin)//2
                mid_val = mountain_arr.get(mid)
                if mid_val>target:
                    end = mid-1
                elif mid_val<target:
                    begin = mid+1
                else:
                    return mid
            return -1
        def binary_search_2(begin,end):
            while begin<=end:
                mid = begin+(end-begin)//2
                mid_val = mountain_arr.get(mid)
                if mid_val>target:
                    begin = mid+1
                elif mid_val<target:
                    end = mid-1
                else:
                    return mid
            return -1
        peek_idx = find_peek_idx()
        if mountain_arr.get(peek_idx)==target:
            return peek_idx
        left_idx = binary_search(0, peek_idx-1)
        if left_idx>-1:
            return left_idx
        return binary_search_2(peek_idx+1, n-1)
            