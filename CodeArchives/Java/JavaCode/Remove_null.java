import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class Remove_null{
    static void remove_null(){
        List<Integer[]> nonNullList = new ArrayList<Integer[]>();
        Integer[][] bigList = {{2,3},{1,2},{},{4,3},{},{1,9}};
        for(Integer[] sub : bigList){
            int count = 0;
            for (int num:sub){
                count+=1;
            }
            if(count!=0){
                nonNullList.add(sub);
            }
        }
        int listSize = nonNullList.size();
        for(int i=0;i<listSize;i++){
            System.out.println(Arrays.asList(nonNullList.get(i)));
        }
    }

    public static int[] twoSum(int[] nums, int target) {
        int result[] = new int[2];
        int idx = 0;
        for(int i=1; i<nums.length;i++){
            for(int j=0;j<i;j++){
                    if ((nums[i]+nums[j])==target){
                        return new int[] {i, j};
                }
            }
            for(int k=i+1;k<nums.length;k++){
                if ((nums[i]+nums[k])==target){
                    return new int[] {i, k};
                }
            }
        }
        return null;
    }
    public static void main(String[] args) {
        int[] nums = {3,4,5,6,11,13,8,7};
        int target = 11;
        System.out.println(Arrays.toString(twoSum(nums, target))); 
    }
}