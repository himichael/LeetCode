class Solution {
    public void nextPermutation(int[] nums) {
        if(nums==null || nums.length==0 || nums.length==1) {
            return;
        }
        int i = nums.length-2;
        while(i>=0 && nums[i+1]<=nums[i]) {
            i--;
        }
        if(i>=0) {
            int j = nums.length-1;
            while(j>0 && nums[j]<=nums[i]) {
                j--;
            }
            swap(nums,i,j);
        }
        reverse(nums,i+1);
    }

    void reverse(int[] arr, int start) {
        int i = start;
        int j = arr.length-1;
        while(i < j) {
            swap(arr,i++,j--);
        }
    }

    void swap(int[] arr, int i, int j) {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
}