class Solution {
	private final Map<Integer,Integer> map = new HashMap<>();
	public TreeNode buildTree(int[] preorder, int[] inorder) {
		for(int i=0;i<preorder.length;i++){
			map.put(inorder[i],i);
		}
		return build(preorder, 0, preorder.length - 1, inorder, 0 , inorder.length - 1);
	}
	
	private TreeNode build(int[] pre, int pre_left, int pre_right, int[] in, int in_left, int in_right) {
		if(pre_left > pre_right || in_left > in_right) {
			return null;
		}
		TreeNode root = new TreeNode(pre[pre_left]);
		int i = map.get(pre[pre_left]);	
        root.left = build(pre, pre_left + 1, pre_left + i - in_left, in, in_left, i - 1);
        root.right = build(pre,pre_left + i - in_left + 1, pre_right, in, i + 1, in_right);
		return root;			
	}	
}