class Solution {
    public void nextPermutation(int[] nums) {
        if(nums==null || nums.length==0 || nums.length==1) {
            return;
        }
        int pivot = nums.length-2;
        while(pivot>=0 && nums[pivot] >= nums[pivot+1]) {
            pivot--;
        }

        if(pivot >= 0) {
            int j = nums.length-1;
            while( j>=0 && nums[j]<=nums[pivot] ) {
                j--;
            }
            swap(nums,pivot,j);
        }
        reverse(nums,pivot+1);
    }

    void reverse(int[] arr, int start) {
        int i = start;
        int j = arr.length-1;
        while(i < j) {
            swap(arr,i,j);
            i++;
            j--;
        }
    }

    void swap(int[] arr, int i, int j) {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
}