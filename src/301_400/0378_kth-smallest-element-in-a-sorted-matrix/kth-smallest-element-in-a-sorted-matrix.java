class Solution {
    public int kthSmallest(int[][] matrix, int k) {
     	java.util.PriorityQueue<Integer> queue = new java.util.PriorityQueue<Integer>(new Comparator<Integer>() {
     		public int compare(Integer o1, Integer o2) {
				return o2-o1;
		}});
    	for(int i=0;i<matrix.length;i++) {
    		for(int j=0;j<matrix[i].length;j++) {
    			queue.add(matrix[i][j]);
    			if(queue.size()>k) {
    				queue.poll();
    			}
    		}
    	}
    	System.out.println(queue);
    	return queue.peek();
    }
}