class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        if(triangle==null || triangle.size()==0) {
			return 0;
		}
		int size = triangle.get(triangle.size()-1).size();
		int[] arr = new int[size+1];
		
		for(int i=triangle.size()-1;i>=0;i--) {
			List<Integer> list = triangle.get(i);
			for(int j=0;j<list.size();j++) {
				arr[j] = Math.min(arr[j],arr[j+1])+list.get(j);
			}
		}
		return arr[0];
    }
}
