import java.util.Arrays;
import java.util.ArrayList;

public class LeastFreq {
    public static void main(String args[]){
        String str = "GeekGee";
        String strarray[] = str.split("");
        ArrayList count_list = new ArrayList<>();
        for(int idx=0;idx<str.length();idx++){
            int tempCount = getCount(str, str.charAt(idx));
            count_list.add(tempCount);
        }
        int[] array = new int[count_list.size()];
        for(int i=0;i<array.length;i++){
            array[i] = (int) count_list.get(i);
        }
        int min_freq = array[0];
        for(int val : array){
            if(val<min_freq){
                min_freq = val;
            }
        }
         int min_idx = count_list.indexOf(min_freq);
        //  System.out.println(min_idx);
         System.out.println(strarray[min_idx]);
    }    

    static int getCount(String str, char val){
        int count = 0;
        for(int i=0;i<str.length();i++){
            if(str.charAt(i)==val){
                count+=1;
            }
        }
        return count;
    }
}
