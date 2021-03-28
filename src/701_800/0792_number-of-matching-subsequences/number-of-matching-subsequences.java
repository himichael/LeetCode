class Solution {
    public int numMatchingSubseq(String S, String[] words) {
        ArrayList<Node>[] heads = new ArrayList[26];
        for(int i = 0; i < 26; ++i) {
            heads[i] = new ArrayList();
        }
        for(String word : words) {
            heads[word.charAt(0) - 'a'].add(new Node(word, 0));
        }
        int res = 0;
        for(char c : S.toCharArray()) {
            ArrayList<Node> tmp = heads[c - 'a'];
            heads[c - 'a'] = new ArrayList();
            for(Node node : tmp) {
                node.index++;
                if(node.index == node.word.length()) {
                    res++;
                }
                else {
                    heads[node.word.charAt(node.index) - 'a'].add(node);
                }
            }
        }
        return res;
    }
}
 
class Node {
    String word;
    int index;
    Node(String word, int index) {
        this.word = word;
        this.index = index;
    }
}