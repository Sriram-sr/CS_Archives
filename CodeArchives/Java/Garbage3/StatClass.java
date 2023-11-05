import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class StatClass {
    public static void main(String args[]){
        int[] array = {2,3,4,1,2,3,4,5,6,8};
        ArrayList list = new ArrayList<>();
        for(int i: array){ list.add(i); }
        ArrayList result = new ArrayList<>();
        for(int num: array){
            if (!(result.contains(num))){
                result.add(num);
            }
        }  
        System.out.println(result);    
    }
}
