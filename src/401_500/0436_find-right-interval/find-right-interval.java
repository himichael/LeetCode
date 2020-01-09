class Solution {
    public int[] findRightInterval(int[][] intervals) {
		java.util.TreeMap<Integer,Integer> map = new java.util.TreeMap<Integer,Integer>();
		int[] res = new int[intervals.length];
		for(int i=0;i<intervals.length;i++) {
			map.put(intervals[i][0],i);		
		}
		for(int i=0;i<intervals.length;i++) {
			java.util.Map.Entry<Integer,Integer> entry = map.ceilingEntry(intervals[i][intervals[i].length-1]);
			res[i] = (entry==null? -1 : entry.getValue());
		}
		return res;
    }
}