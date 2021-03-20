class Solution {
    public int calculate(String s) {
        Deque<Integer> stack = new LinkedList<Integer>();
        int num = 0;
        char pre_sign = '+';
        int res = 0;
        int n = s.length();
        for(int i = 0; i < n; ++i) {
            char c = s.charAt(i);
            if(Character.isDigit(c)) {
                num = num * 10 + c - '0';
            }
            if(!Character.isDigit(c) && c != ' ' || i == n - 1) {
                switch(pre_sign) {
                    case '+':
                        stack.push(num);
                        break;
                    case '-':
                        stack.push(-num);
                        break;
                    case '*':
                        stack.push(stack.pop() * num);
                        break;
                    default:
                        stack.push(stack.pop() / num);
                }
                pre_sign = c;
                num = 0;
            }
        }
        while(!stack.isEmpty()) {
            res += stack.pop();
        }
        return res;
    }
}