class Solution {	
	public static final String QUOT = "&quot;";
	public static final String APOS = "&apos;";
	public static final String AMP = "&amp;";
	public static final String GT = "&gt;";
	public static final String LT = "&lt;";
	public static final String FRASL = "&frasl;";
	
    public String entityParser(String text) {
    	int n = text.length();
    	int i = 0;
    	while(i<n) {
    		if(text.charAt(i)=='&') {
    			if(i+5<n && QUOT.equals(text.subSequence(i,i+5+1))) {
    				String begin = text.substring(0, i);
    				String end = text.substring(i+5+1);
    				text = begin+"\""+end;
    				n = text.length();
    			}
    			else if(i+5<n && APOS.equals(text.subSequence(i,i+5+1))) {
    				String begin = text.substring(0, i);
    				String end = text.substring(i+5+1);
    				text = begin+"'"+end;
    				n = text.length();
    			}
    			else if(i+4<n && AMP.equals(text.subSequence(i,i+4+1))) {
    				String begin = text.substring(0, i);
    				String end = text.substring(i+4+1);
    				text = begin+"&"+end;
    				n = text.length();
    			}
    			else if(i+3<n && GT.equals(text.subSequence(i,i+3+1))) {
    				String begin = text.substring(0, i);
    				String end = text.substring(i+3+1);
    				text = begin+">"+end;
    				n = text.length();
    			}
    			else if(i+3<n && LT.equals(text.subSequence(i,i+3+1))) {
    				String begin = text.substring(0, i);
    				String end = text.substring(i+3+1);
    				text = begin+"<"+end;
    				n = text.length();
    			}
    			else if(i+6<n && FRASL.equals(text.subSequence(i,i+6+1))) {
    				String begin = text.substring(0, i);
    				String end = text.substring(i+6+1);
    				text = begin+"/"+end;
    				n = text.length();
    			}
    		}
    		++i;
    	}
    	return text;
    }
}