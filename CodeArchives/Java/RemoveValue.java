import java.util.Arrays;
import java.lang.reflect.Array;
import java.util.ArrayList;

public class RemoveValue{
    static int removeElement(int nums[], int value){
        int i;
        ArrayList<Integer> newList = new ArrayList<>();
        for(i=0;i<nums.length;i++){
            if (nums[i]!=value){
                newList.add(nums[i]);
            }
        }

        for(i=0;i<newList.size();i++){
            nums[i] = newList.get(i);
        }
        
        return newList.size();
    }

    public static int remove(int[] nums, int val) {
        int k = 0;
        int i = 0;
    
        while (i < nums.length) {
            if (nums[i] != val)
                System.out.println("K before "+k);
                nums[k++] = nums[i];
                System.out.println("K after "+k);
            i++;
        }
        return k;
    }
    public static void main(String args[]){
        int[] nums = {0,1,2,2,3,0,4,2};
        int val = 2;
        System.out.println(remove(nums, val));
    }
}