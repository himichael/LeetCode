class Solution {
    public List<String> letterCombinations(String digits) {
        if(digits==null || digits.length()==0) {
            return new ArrayList<>();
        }
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


        List<String> nums = new ArrayList<>();
        nums.add("");
        return loop(digits,map,nums);
    }

	
    public List<String> loop(String str, Map<String,List<String>> map, List<String> nums) {
        if(str==null || str.length()==0) {
            return nums;
        }
        List<String> list = map.get(str.substring(0, 1));
        List<String> new_list = new ArrayList<>();

		//递归执行，每次获取字符串的第一位，比如 "234" 第一次递归时获取“2”，然后将“2”对应的字母全部放到List中
		//之后将新拼接好的Lit，这里是 new_list，传给下一个递归函数执行
		//第一次调用这个函数loop()，外层只有一个元素，内层是3个元素
		//第二次调用这个函数loop()，外层是3个元素，内层也是3个元素
		//第三次调用这个函数loop()，外层是9个元素，内层是3个元素
        for(int i=0;i<nums.size();i++) {
            for(int j=0;j<list.size();j++) {
                String tmp = nums.get(i);
                String j_num = list.get(j);
                new_list.add(tmp+j_num);
            }
        }
		//下一次递归传入的参数str->"34"，List中的值就是 "a","b","c"
		//下下一次再递归，传入的参数str->"4",List中的参数是"ad","ae","af","bd","be","bf","cd","ce","cf"
        return loop(str.substring(1),map,new_list);
    }
}