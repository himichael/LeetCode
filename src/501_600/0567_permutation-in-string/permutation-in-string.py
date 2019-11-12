class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if not (s1 and s2):
            return False
        s1_len,s2_len = len(s1),len(s2)
        if s1_len > s2_len:
            return False
        s1_map,s2_map = [0]*26,[0]*26
        for i in xrange(s1_len):
            s1_map[ord(s1[i])-ord("a")] += 1 
            s2_map[ord(s2[i])-ord("a")] += 1
            
        def match(map_1,map_2):
            for i in xrange(26):
                if map_1[i]!=map_2[i]:
                    return False
            return True
        for i in xrange(s2_len-s1_len):
            if match(s1_map,s2_map):
                return True
            s2_map[ord(s2[i+s1_len])-ord("a")] += 1
            s2_map[ord(s2[i])-ord("a")] -= 1
        return match(s1_map,s2_map)
