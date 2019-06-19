class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        recursive(0, candidates, 0, new Stack<Integer>(), target);
        return new ArrayList<List<Integer>>(res);
    }

    Set<List<Integer>> res = new HashSet<List<Integer>>();
    void recursive(int i,int[] arr,int tmp,Stack<Integer> tmp_arr,int target) {
        if(tmp==target) {
            res.add(new ArrayList(tmp_arr));
        }
        for(int j=i;j<arr.length;j++) {
            if(tmp+arr[j] <= target) {
                tmp_arr.add(arr[j]);
                recursive(j + 1, arr, tmp + arr[j], tmp_arr, target);
                //tmp -= arr[j];
                tmp_arr.pop();
            }
        }
    }
}