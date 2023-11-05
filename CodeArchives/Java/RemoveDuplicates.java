import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

public class RemoveDuplicates {
    static int remove_duplicates(int array[]){
        Integer[] newarray = Arrays.stream( array ).boxed().toArray( Integer[]::new );
        List<Integer> list = Arrays.asList(newarray);
        List<Integer> result = new ArrayList<>();
        for(int num: array){
            if (!(result.contains(num))){
                result.add(num);
            }
        }
        System.out.println(result);
        
        for(int idx=0;idx<array.length;idx++){
            if (idx<result.size()){
                array[idx] = result.get(idx);
                System.out.println(Arrays.toString(array));
            }
        }
        return result.size();
    }

    static int solution(int nums[]){
        int ans = 0;
        for(int i =0; i<nums.length; i++){
            if(i == nums.length-1){
                nums[ans] = nums[i];
                System.out.println(Arrays.toString(nums));
                ans++;
                break;
            }
            else if(nums[i] != nums[i+1]){
                System.out.println("i "+i);
                nums[ans] = nums[i];
                System.out.println(Arrays.toString(nums));
                ans += 1;
            }
        }
        System.out.println(Arrays.toString(nums));
        return ans;
    }
    public static void main(String args[]){
        int array[] = {0,0,1,1,1,2,2,3,3,4};
        System.out.println(remove_duplicates(array));
        // System.out.println(solution(array));
    }
}