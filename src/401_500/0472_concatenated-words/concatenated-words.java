class Solution {
    private HashSet<String> hashSet = new HashSet<>();
    private List<String> res = new LinkedList<>();;
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        for(String word : words) {
            if(!word.equals("")) hashSet.add(word);
        }
        for(String word : words){
            if(helper(word, 0)) res.add(word);
        }
        return res;
    }

    private boolean helper(String str, int index){
        if(hashSet.contains(str) && index > 0) return true;
        int sLen = str.length();
        for(int i = sLen; i >= 0; i--){
            String temp = str.substring(i,sLen);
            if(hashSet.contains(temp)){
//                这个错误已经犯了好几次了，一定要注意
//                return helper(str.substring(i), index + 1);
                if(helper(str.substring(0, i), index + 1)) return true;
            }
        }
        return false;
    }
}