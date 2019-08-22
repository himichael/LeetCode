class TrieNode {
	TrieNode[] childrens = new TrieNode[26];
	char val;
	boolean is_end = false;
}

class Trie {
	final TrieNode root;
    /** Initialize your data structure here. */
    public Trie() {
        root = new TrieNode();
        root.val = ' ';
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        TrieNode node = root;
        for(int i=0;i<word.length();i++) {
        	char c = word.charAt(i);
        	if( node.childrens[c-'a']==null ) {
        		node.childrens[c-'a'] = new TrieNode();
        	}
        	node = node.childrens[c-'a'];
        }
        node.is_end = true;
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        TrieNode node = root;
        for(int i=0;i<word.length();i++) {
        	char c = word.charAt(i);
        	if( node.childrens[c-'a']== null ) {
        		return false;
        	}
        	node = node.childrens[c-'a'];
        }
        return node.is_end;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
    	TrieNode node = root;
    	for(int i=0;i<prefix.length();i++) {
    		char c = prefix.charAt(i);
    		if( node.childrens[c-'a']==null ) {
    			return false;
    		}
    		node = node.childrens[c-'a'];
    	}
    	return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */