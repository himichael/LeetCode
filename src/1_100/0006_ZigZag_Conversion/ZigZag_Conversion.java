class Solution {
    public static String convert(String s, int numRows) {
        if(s==null || numRows==1) {
            return s;
        }

        int size = Math.min(s.length(),numRows);
        StringBuilder[] arr = new StringBuilder[size];
        for(int i=0;i<size;i++) {
            arr[i] = new StringBuilder();
        }
        int i = 0;
        int n = s.length();
        while(i < n) {
            for (int j = 0; j < numRows; j++) {
                if (i < n) {
                    char c = s.charAt(i);
                    arr[j].append(c);
                    i++;
                }
            }
            for (int j = numRows - 2; j > 0; j--) {
                if (i < n) {
                    char c = s.charAt(i);
                    arr[j].append(c);
                    i++;
                }
            }
        }
        for(int k=1;k<arr.length;k++) {
            arr[0].append(arr[k]);
        }
        return arr[0].toString();
    }
}