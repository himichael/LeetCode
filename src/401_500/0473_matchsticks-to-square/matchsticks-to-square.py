class Solution {
    int[] counter = new int[4];
    int[] arr = null;
    int target = 0;
    public boolean makesquare(int[] matchsticks) {
        if(matchsticks == null || matchsticks.length < 4) {
            return false;
        }
        int sum = 0;
        for(int i : matchsticks) {
            sum += i;
        }
        if(sum % 4 != 0) {
            return false;
        }
        target = sum / 4;
        Arrays.sort(matchsticks);
        //reverse
        int len = matchsticks.length;
        for(int i = 0; i < len / 2; ++i) {
            int tmp = matchsticks[i];
            matchsticks[i] = matchsticks[len - i - 1];
            matchsticks[len - i - 1] = tmp;
        }
        if(matchsticks[0] > target) {
            return false;
        }
        arr = matchsticks;
        return dfs(0);
    }

    private boolean dfs(int index) {
        if(index == arr.length) {
            return counter[0] == counter[1] && counter[1] == counter[2] && counter[2] == counter[3];
        }
        for(int i = 0; i < 4; ++i) {
            if(counter[i] + arr[index] <= target) {
                counter[i] += arr[index];
                if(dfs(index + 1)) {
                    return true;
                }
                counter[i] -= arr[index];
            }
        }
        return false;
    }
}