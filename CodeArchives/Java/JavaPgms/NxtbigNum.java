import java.util.ArrayList;
import java.util.Arrays;
public class NxtbigNum{
    public static void main(String args[]){
        int[] array1 = {4,1,2};
        int[] array2 = {1,3,4,2};
        int[] resarray = new int[array1.length];
        ArrayList list = new ArrayList<>();
        for (int num: array2){
            list.add(num);
        }
        int count = 0;
        for (int num:array1){
            int idx = list.indexOf(num);
            if (idx != array2.length){
                int[] slice = Arrays.copyOfRange(array2,idx+1,array2.length);
                int flag = 0;
                for(int nxt=0;nxt<slice.length;nxt++){
                    if (slice[nxt]>num){
                        resarray[count] = slice[nxt];
                        flag = 1;
                        break;
                    }
                }
                if (flag==0){
                    resarray[count] = -1;
                }
            }
            else{
                resarray[count] = -1;
            }
            count+=1;
        }
        System.out.println(Arrays.toString(resarray));
    }
}