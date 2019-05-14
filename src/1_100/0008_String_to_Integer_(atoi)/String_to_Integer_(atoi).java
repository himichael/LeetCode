class Solution {
    public int myAtoi(String str) {
        if(str==null || str.length()==0) {
            return 0;
        }
        java.math.BigDecimal min = new java.math.BigDecimal(Integer.MIN_VALUE);
        java.math.BigDecimal max = new java.math.BigDecimal(Integer.MAX_VALUE);
        int max_len = (""+Integer.MAX_VALUE).length()+1;
        StringBuilder sb = new StringBuilder();
        str = str.trim();

        int index = 0;
        if(str.length() > 0) {
            if(str.startsWith("-")) {
                sb.append("-");
                index++;
            }
            else if(str.startsWith("+")) {
                index++;
            }
        } else {
            return 0;
        }

        for(;index<str.length();index++) {
            char c = str.charAt(index);
            if(c==' ') {
                break;
            }else if(c=='.') {
                break;
            }else if(c>='0' && c<='9') {
                sb.append(c);
            }else {
                break;
            }
        }


        long lo = 0L;
        java.math.BigDecimal b = null;
        try {
            b = new java.math.BigDecimal(sb.toString());
            if(b.compareTo(min) < 0) {
                lo = Integer.MIN_VALUE;
                return (int)lo;
            }
            if(b.compareTo(max) > 0) {
                lo = Integer.MAX_VALUE;
                return (int)lo;
            }
            lo = Long.parseLong(sb.toString());
        }catch(Exception e) {
            return 0;
        }
        return (int)lo;
    }
	
	//这题非常坑，各种边界问题需要特别注意
	//这里给出测试用例
    public void go() {
        System.out.println("-+1 ->"+myAtoi("-+1"));
        System.out.println("20000000000000000000 ->"+myAtoi("20000000000000000000") );
        System.out.println("42 ->"+myAtoi("42"));
        System.out.println("   -42 ->"+myAtoi("   -42"));
        System.out.println("4193 with words ->"+myAtoi("4193 with words"));
        System.out.println("words and 987 ->"+myAtoi("words and 987"));
        System.out.println("-91283472332 ->"+myAtoi("-91283472332"));
        System.out.println("1234567890 ->"+myAtoi("1234567890"));
        System.out.println("+-2 ->"+myAtoi("+-2"));
        System.out.println("  -0012a42 ->"+myAtoi("  -0012a42"));
        System.out.println("3.14159 ->"+myAtoi("3.14159"));
        System.out.println("  -0012a42 ->" + myAtoi("  -0012a42"));
        System.out.println("-13+8 ->" + myAtoi("-13+8"));
    }
	
	
	
}