public class Problem_35 {
    int searchIndex(int[] nums, int target) {
        int idx, len = nums.length;
        if (target<nums[0]){
            return 0; 
        }
        for(idx=0;idx<len;idx++){
            if (nums[idx]==target){
                return idx;
            }
        }
        for(idx=1;idx<len;idx++){
            if (nums[idx-1]<target && nums[idx]>target){
                return idx;
            }
        }
        return len;
    }

    public static void main(String args[]){
        Problem_35 instance = new Problem_35();
        int[] nums = {2,3,18,54,91};
        int target = 1;
        System.out.println(instance.searchIndex(nums, target));
    }
}