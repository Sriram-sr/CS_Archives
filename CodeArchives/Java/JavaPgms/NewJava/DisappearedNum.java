import java.util.*;

public class DisappearedNum {
    public static void main(String args[]){
        int[] nums = {4,3,2,7,8,2,3,1};
        Arrays.sort(nums);
        int max_value = nums[nums.length-1];
        // List arraylist = Arrays.asList(nums);
        ArrayList res_list = new ArrayList();
        for(int i=1;i<=max_value;i++){
            if ((Arrays.binarySearch(nums, i))>=0){
                continue;
            }
            else{
                res_list.add(i);   
            }
        }
        System.out.println(res_list);
    }
}
