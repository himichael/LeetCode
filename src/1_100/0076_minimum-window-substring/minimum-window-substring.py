class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not (s and t):
            return ""
        left,right = 0,0
        max_res_len,res_left_pos,res_right_pos = 2**31-1,0,0
        dict_t = dict()
        for i in t:
            if i not in dict_t:
                dict_t[i] = 1
            else:
                dict_t[i] += 1
        non_duplicate_t_num = len(dict_t)
        windows_count = dict()
        match_num = 0
        
        while right<len(s):
            c = s[right]
            windows_count[c] = windows_count.get(c,0)+1
            if c in dict_t and windows_count[c]==dict_t[c]:
                match_num += 1
            
            while left<=right and match_num==non_duplicate_t_num:
                if (right-left+1)<max_res_len:
                    max_res_len = min(max_res_len,(right-left+1))
                    res_left_pos = left
                    res_right_pos = right
                left_c = s[left]
                windows_count[left_c] -= 1
                if left_c in dict_t and windows_count[left_c]<dict_t[left_c]:
                    match_num -= 1
                left += 1
            # end inner while
            right += 1
        if max_res_len<2**31-1:
            return s[res_left_pos:res_right_pos+1]
        return ""