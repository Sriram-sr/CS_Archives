import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class RemoveElement {
    static ArrayList<Integer> removeByIndex(int[] array, int index){
        ArrayList list = new ArrayList<>();
        for(int i=0;i<array.length;i++){
            if(i!=index){
                list.add(array[i]);
            }
        }
        return list;
    }

    // static int[] removeByValue(int array, int value){

    // }

    public static void main(String args[]){
        int[] array = {2,3,9,6,1,2,8,7};
        System.out.println(removeByIndex(array, 2));
    }
}
