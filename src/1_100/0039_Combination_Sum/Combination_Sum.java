class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
    	Arrays.sort(candidates);
    	dfs(candidates,target,0,new Stack<Integer>());
    	return res;
    }
    
    List<List<Integer>> res = new ArrayList<List<Integer>>();
    void dfs(int[] candidates, int target, int index, Stack<Integer> cur) {
    	if(0 == target) {
    		res.add(new ArrayList<Integer>(cur));
    		return;
    	}
    	for(int i=index;i<candidates.length;i++) {
    		if(candidates[i] > target) {
    			break;
    		}
    		cur.push(candidates[i]);
    		dfs(candidates,target-candidates[i],i,cur);
    		cur.pop();
    	}
    }
}