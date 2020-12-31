class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> q = new PriorityQueue<Integer>((a, b) -> b - a);
        for(int i : stones) {
            q.offer(i);
        }
        while(q.size() > 1) {
            int a = q.poll();
            int b = q.poll();
            if(a > b) {
                q.offer(a - b);
            }
        }
        return q.size() == 0 ? 0 : q.poll();
    }
}