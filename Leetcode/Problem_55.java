//attempted

public class Problem_55 {
    static boolean jump_game(int[] nums){
        int pos = 0, idx;
        for(idx=0;idx<nums.length;idx++){
            if(idx==0 || idx==pos && idx!=nums.length-1){
                pos+=nums[idx];
            }
        }
        if(pos==nums.length-1){
            return true;
        }

        return false;
    }

    public static void main(String... args){
        int nums[] = {3,2,1,0,4};
        System.out.println(jump_game(nums));
    }
}