class Solution {
    public int reverse(int x) {
		if(x==0) {
			return 0;
		}
        long num = 0L;
		boolean is_negative = false;
		if(x < 0) {
			is_negative = true;
			x = -x;
		}
		//将 12345 转换为 54321，每次取模得到末数，再加上 num*10
		//因为num第一次是0，会自动忽略边界问题
		//如果x是120，第一次计算就是  num*10-> 0*10,  x%10->0, 0+0=0，自动忽略了边界问题
		while(x > 0) {
			num = num*10 + x%10;
			x /= 10;
		}
		if(is_negative) {
			return (int)(-num<Integer.MIN_VALUE? 0 : -num);
		}
		return (int)(num>Integer.MAX_VALUE? 0 : num);
    }
}