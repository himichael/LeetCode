class Solution {
    public String longestPalindrome(String s) {
    	// abccba
    	if(s==null || s.length()==0 || s.length()==1) {
    		return s;
    	}
    	//s长度是奇数还是偶数
    	int start = 0;
    	int end = 0;
    	for(int i=0;i<s.length();i++) {
    		int count_1 = expandAroundCenter(s,i,i);
    		int count_2 = expandAroundCenter(s,i,i+1);
    		int max = Math.max(count_1, count_2);
    		if(max > end-start+1) {
    			start = i-(max-1)/2;
    			end = i+max/2;
    		}
    	}
        return s.substring(start,end+1);
    }	
	
	//不断的向两边扩展 ，i向左，j向右直到两个不相等为止
    int expandAroundCenter(String s, int i, int j) {
    	while(i>=0 && j<s.length() && s.charAt(i)==s.charAt(j)) {
    		i--;
    		j++;
    	}
    	return (j-i-1);
    }
}