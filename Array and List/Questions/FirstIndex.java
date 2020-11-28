public class Solution {
    
    private int getMax(int[] arr) {
        int maxIndex = 0;
        if (arr.length == 1)
            return 0;
        
        for (int i = 1; i < arr.length; i++) {
            if (arr[maxIndex] < arr[i]) {
                maxIndex = i;
            }
        }
        
        return maxIndex;
    }
    
    public int[] solve(int[] A, int[] B) {
        int[] ans = new int[B.length];
        int max = getMax(A);
        
        for (int i = 0; i < B.length; i++) {
            if (B[i] > A[max])
                ans[i] = -1;
            else {
                int j = 0;
                while (A[j] < B[i])
                    j++;
                ans[i] = j;
                
            }
        }
        
        return ans;
        
    }
}
