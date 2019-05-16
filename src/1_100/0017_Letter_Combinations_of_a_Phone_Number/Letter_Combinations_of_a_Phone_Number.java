class Solution {
    public List<String> letterCombinations(String digits) {
     
    	Map<String,List<String>> map = new HashMap<>();
		List<String> tmp = new ArrayList<>();
		tmp.add(" ");
		map.put("0", tmp);
		
		tmp = new ArrayList<>();
		tmp.add("*");
		map.put("1", tmp);
		
		tmp = new ArrayList<>();
		tmp.add("a");
		tmp.add("b");
		tmp.add("c");
		map.put("2", tmp);
		
		tmp = new ArrayList<>();
		tmp.add("d");
		tmp.add("e");
		tmp.add("f");
		map.put("3", tmp);
		
		tmp = new ArrayList<>();
		tmp.add("g");
		tmp.add("h");
		tmp.add("i");
		map.put("4", tmp);
		
		tmp = new ArrayList<>();
		tmp.add("j");
		tmp.add("k");
		tmp.add("l");
		map.put("5", tmp);
		
		tmp = new ArrayList<>();
		tmp.add("m");
		tmp.add("n");
		tmp.add("o");
		map.put("6", tmp);
		
		tmp = new ArrayList<>();
		tmp.add("p");
		tmp.add("q");
		tmp.add("r");
		tmp.add("s");
		map.put("7", tmp);
		
		tmp = new ArrayList<>();
		tmp.add("t");
		tmp.add("u");
		tmp.add("v");
		map.put("8", tmp);
		
		tmp = new ArrayList<>();
		tmp.add("w");
		tmp.add("x");
		tmp.add("y");
		tmp.add("z");
		map.put("9", tmp);
		
   
    	loop(digits,map,new StringBuilder());
    	return null;
    }
    
    public void loop(String str, Map<String,List<String>> map,StringBuilder sb) {
    	if(str==null || str.length()==0) {
    		return;
    	}
    	List<String> list = map.get(str.substring(0, 1));
    	for(int i=0;i<list.size();i++) {
    		list.get(i);
    	}
    	System.out.println(list.toString());
    	
    	loop(str.substring(1),map,sb);
    	
    }
}