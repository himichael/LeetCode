class Solution {
    public int romanToInt(String s) {
    	int num = 0;
    	int len = s.length();
		
		//遍历每个字符，然后看对应的是哪个罗马字母，如果是C,X,I，还要再取下一个字符比较 
    	for(int i=0;i<len;i++) {
    		char c = s.charAt(i);
    		switch(c) {
    			case 'M':
    				num += 1000;
    				break;
    			case 'C':
    				if(i<len-1 && s.charAt(i+1)=='M') {
    					num += 900;
    					i++;
    					break;
    				}
    				if(i<len-1 && s.charAt(i+1)=='D') {
    					num += 400;
    					i++;
    					break;
    				}
    				num += 100;
    				break;
    			case 'D':
    				num += 500;
    				break;
    			case 'X':
    				if(i<len-1 && s.charAt(i+1)=='C') {
    					num += 90;
    					i++;
    					break;
    				}
    				if(i<len-1 && s.charAt(i+1)=='L') {
    					num += 40;
    					i++;
    					break;
    				}
    				num += 10;
    				break;
    			case 'L':
    				num += 50;
    				break;
    			case 'I':
    				if(i<len-1 && s.charAt(i+1)=='X') {
    					num += 9;
    					i++;
    					break;
    				}
    				if(i<len-1 && s.charAt(i+1)=='V') {
    					num += 4;
    					i++;
    					break;
    				}
    				num += 1;
    				break;
    			case 'V':
    				num += 5;
    				break;
    			default:
    				break;
    				
    		}		
    	}
    	return num;
    }
}