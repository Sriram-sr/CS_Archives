import java.util.Arrays;
import java.util.ArrayList;

public class ReturnUnique {
    static ArrayList<Integer> returnUnique(int array[]){
        ArrayList<Integer> unique_list = new ArrayList<>();
        for(int i=0;i<array.length;i++){
            int[] fwd = Arrays.copyOfRange(array,0,i);
            int[] bwd = Arrays.copyOfRange(array, i+1, array.length);
            if (findIndex(fwd, array[i])==-1 && findIndex(bwd, array[i])==-1){
                unique_list.add(array[i]);
            }
        }

        return unique_list;
    }

    static int findIndex(int[] sArray,int element ){
        for(int i=0;i<sArray.length;i++){
            if (sArray[i]==element){
                return i;
            }
        }
        return -1;
    }
    public static void main(String args[]){
        int array[] = {2,4,1,6,2,1,0,8,6,9,11,3,11};
        System.out.println(returnUnique(array));
        
    }
}
