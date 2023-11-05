import java.util.Arrays;

public class selectNinsert{
    public static int insertmethod(Integer[] array,Integer target){
        if (Arrays.asList(array).contains(target)){
            return Arrays.binarySearch(array, target);
        }
        for (int i=0;i<(array.length)-1;i++){
            if (array[i]<target && array[i+1]>target){
                return i+1;
            }
            else if (array[array.length-1]<target){
                return array.length;
            }
        }
        return 1;
        
    }

    public static void main(String args[]){
        Integer[] array = {1,3,5,6};
        int target = 7;
        System.out.println(insertmethod(array, target));    
    }
    
}