import java.util.Arrays;
import java.util.List;

public class sum_Elem {
    public String twosum(int[] array,int target){
        List arraylist = Arrays.asList(array);
        System.out.println(arraylist);
        // System.out.println(arraylist.contains(5));
        int length = array.length - 1;
        int[] res_array = new int[2];
        for (int i=0;i<length;i++){
            int sum = array[i] + array[i+1];
            if (sum == target){
                res_array[0] = array[i];
                res_array[1] = array[i+1];
            }  
        }
        // var oriarray = Arrays.toString(res_array);
        // System.out.println(oriarray.getClass().getSimpleName());
        return Arrays.toString(res_array);
    }
    public static void main(String args[]){
        int numbers[] = {1,2,3,4,5,6,8,9,10};
        int range = numbers[numbers.length - 1];
        int missing_number=0;
        for (int i=0;i<range;i++){
            if (numbers[i]==i+1){
                continue;
            }
            else{
                missing_number = i+1;
                break;
            }   
        }
        System.out.println(missing_number);
        sum_Elem instance = new sum_Elem();
        int array[] = {2,3,4,7,9,8,1,6};
        int target = 16;
        System.out.println(instance.twosum(array, target));
    }
}
