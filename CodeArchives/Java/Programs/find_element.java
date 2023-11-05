public class find_element{
    static int search(int nums[], int target){
        int i;
        for(i=0;i<nums.length;i++){
            if (nums[i]==target){
                return i;
            }
        }
        return -1;
    }
    public static void main(String[] args) {
        int[] nums = {4,5,6,7,0,1,2}; 
        int target = 3;
        System.out.println(search(nums, target));
    }
}