class Solution {
    public int sumFourDivisors(int[] nums) {
    	int res = 0;
    	for(int n : nums) {
    		if(n==1) {
    			continue;
    		}
    		ArrayList<Integer> list = new ArrayList<Integer>();
    		list.add(1);
    		int size = (n/2)+1;
    		for(int j=2;j<size;++j) {
    			if(n%j==0) {
    				list.add(j);
    			}
    			if(list.size()>4) {
    				break;
    			}
    		}
    		list.add(n);
    		if(list.size()==4) {
    			res += list.get(0)+list.get(1)+list.get(2)+list.get(3);
    		}
    	}
    	return res;
    }
}