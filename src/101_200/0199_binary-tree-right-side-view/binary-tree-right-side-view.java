
//解法一
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        if(root==null) {
            return new ArrayList<Integer>();
        }
        List<Integer> res = new ArrayList<Integer>();
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.offer(root);
        while(!queue.isEmpty()) {
            int size = queue.size();
            LinkedList<Integer> tmp = new LinkedList<Integer>();
            for(int i=0;i<size;++i) {
                TreeNode node = queue.poll();
                if(node.left!=null) {
                    queue.offer(node.left);
                }
                if(node.right!=null) {
                    queue.offer(node.right);
                }
                tmp.add(node.val);
            }
            res.add(tmp.pollLast());
        }
        return res;
    }
}



//解法二
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        if(root==null) {
            return new ArrayList<Integer>();
        }
		Queue<Pair<Integer,TreeNode>> queue = new LinkedList<Pair<Integer,TreeNode>>();
		Map<Integer,Integer> rightViewMap = new HashMap<Integer,Integer>();
		int maxDepth = Integer.MIN_VALUE;
		queue.offer(new Pair<Integer, TreeNode>(0,root));
		List<Integer> ans = new ArrayList<Integer>();
		while(!queue.isEmpty()) {
			Pair<Integer,TreeNode> pair = queue.poll();
			int depth = pair.key;
			TreeNode node = pair.value;
			if(node!=null) {
				maxDepth = Math.max(maxDepth,depth);
				rightViewMap.put(depth,node.val);
				queue.offer(new Pair<Integer, TreeNode>(depth+1,node.left));
				queue.offer(new Pair<Integer, TreeNode>(depth+1,node.right));
			}
		}
		for(int i=0;i<=maxDepth;++i) {
			ans.add(rightViewMap.get(i));
		}
        return ans;
    }
	
	static class Pair<K,V> {
		final K key;
		final V value;
		Pair(K key,V value) {
			this.key = key;
			this.value = value;
		}
		
		public K getKey() {
			return this.key;
		}
		
		public V getValue() {
			return this.value;
		}
	}
}



