class Solution {
    public void sortColors(int[] nums) {
		if(nums==null || nums.length==0) {
			return;
		}
		int p0 = 0;
		int p2 = nums.length-1;
		int cur = 0;
		while(cur<=p2) {
			if(nums[cur]==0) {
				swap(nums,cur,p0);
				++cur;
				++p0;
			} else if(nums[cur]==2) {
				swap(nums,cur,p2);
				--p2;
			} else {
				++cur;
			}
		}
    }
	
	void swap(int[] arr,int i,int j) {
		int tmp = arr[i];
		arr[i] = arr[j];
		arr[j] = tmp;
	}
}	