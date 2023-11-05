import java.util.Arrays;

class Solution {
    public static int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[j] == target - nums[i]) {
                    return new int[] { i, j };
                }
            }
        }
        // In case there is no solution, we'll just return null
        return null;
    }

    public static void ownSolution(int[] nums, int target){
        for(int i=0;i<nums.length-1;i++){
            for(int j=i+1;j<nums.length;j++){
                if((nums[i]+nums[j])==target){
                    System.out.println(i+" "+j);
                }
            }
        }
    }
    public static void main(String args[]){
        int[] nums = {3,2,3};
        int target = 6;
        // System.out.println(Arrays.toString(twoSum(nums, target)));
        ownSolution(nums, target);
    }
}