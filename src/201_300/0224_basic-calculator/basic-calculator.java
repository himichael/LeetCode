class Solution {
    public int calculate(String s) {
        Deque<Integer> stack = new LinkedList<Integer>();
        stack.push(1);
        int res = 0;
        int i = 0;
		int sign = 1;
        int n = s.length();
        while(i < n) {
			char c = s.charAt(i);
            if(c == ' ') {
				++i;
			}
			else if(c == '+') {
				sign = stack.peek();
				++i;
			}
			else if(c == '-') {
				sign = -stack.peek();
				++i;
			}
			else if(c == '(') {
				stack.push(sign);
				++i;
			}
			else if(c == ')') {
				stack.pop();
				++i;
			}
			else {
				int tmp = 0;
				while(i < n && Character.isDigit(s.charAt(i))) {
					tmp = tmp * 10 + s.charAt(i) - '0';
					++i;
				}
				res += sign * tmp;
 			}
         }
		 return res;
    }
}