import java.util.ArrayList;

public class remove_dup {
    public static void main(String args[]){
    ArrayList result_array = new ArrayList();
        int[] array = {2,3,4,4,8,7,9,12,7,12,13};
        for(int i:array){
            if (result_array.contains(i)){
                continue;
            }
            else{
                result_array.add(i);
            }
        }
        System.out.println(result_array);
    }
}
