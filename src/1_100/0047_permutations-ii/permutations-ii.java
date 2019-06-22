class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
    	Arrays.sort(nums);
    	ArrayList<Integer> queue = new ArrayList<Integer>();
    	for(int i:nums) {
    		queue.add(i);
    	}
    	permute_back_trace(queue, new Stack<Integer>());
        return new ArrayList<List<Integer>>(permute_uniq_res);
    }
    
    Set<List<Integer>> permute_uniq_res = new HashSet<List<Integer>>();
    void permute_back_trace(ArrayList<Integer> queue, Stack<Integer> stack) {
    	if(queue.size() == 0) {
    		permute_uniq_res.add(new ArrayList(stack));
    		return;
    	}
    	int size = queue.size();
    	for(int i=0;i<size;i++) {
    		stack.push(queue.remove(0));
    		permute_back_trace(queue,stack);
    		queue.add(stack.pop());
    	}
    }
}