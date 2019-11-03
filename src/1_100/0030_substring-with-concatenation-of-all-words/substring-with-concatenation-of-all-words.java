class Solution {
	public List<Integer> findSubstring(String s, String[] words) {
		if(s==null || "".equals(s) || words==null || words.length==0) {
			return new ArrayList<Integer>();
		}
		//将每个单词以及出现的频率记录到map中
		Map<String,Integer> words_map = new HashMap<String,Integer>();
		for(String str : words) {
			if(words_map.containsKey(str)) {
				words_map.put(str,words_map.get(str)+1);
			} else {
				words_map.put(str,1);
			}
		}
		List<Integer> res = new ArrayList<Integer>();
		//words中一个单词的长度，以及words的总长度
		int one_word_size = words[0].length();
		int all_word_size = words.length * one_word_size;
		//遍历整个字符串，注意循环的结束条件
		for(int i=0;i<s.length()-all_word_size+1;i++) {
			//每次取 all_word_size长度的子串
			String tmp = s.substring(i,i+all_word_size);
			HashMap<String,Integer> d = new HashMap<String,Integer>(words_map);
			//将子串和临时map进行比较
			for(int j=0;j<tmp.length();j+=one_word_size) {
				//从子串tmp中取出one_word_size长度的子串，看是否出现在临时map中
				//如果是就将临时map记录的频率-1，如果不在就跳出循环
				String key = tmp.substring(j,j+one_word_size);                
				if(d.containsKey(key)) {
					d.put(key,d.get(key)-1);
					if(d.get(key)==0) {
						d.remove(key);
					}
				} else {
					break;
				}
			}
			//当内层循环遍历完后，如果临时map为空则表示全部匹配上了
			//记录数组的下标
			if(d.size()==0) {
				res.add(i);
			}
		}
		return res;
	}
}