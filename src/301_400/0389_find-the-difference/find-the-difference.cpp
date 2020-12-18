class Solution {
public:
    char findTheDifference(string s, string t) {
        vector<int> cnt(26, 0);
        for(char cs : s) {
            cnt[cs - 'a']++;
        }
        for(char cs : t) {
            cnt[cs - 'a']--;
            if(cnt[cs - 'a'] < 0) {
                return cs;
            }
        } 
        return ' ';
    }
};
 