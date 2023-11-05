import java.util.Map;
import java.util.HashMap;

public class HashCheck{

    static int customCount(Integer[] numArray,int element){
        int count = 0;
        for(int i=0;i<numArray.length;i++){
            if(numArray[i]==element){
                count++;
            }
        }
        return count;
    }
    public static void main(String args[]){
        Integer numArray[] = {1,2,3,4,1,5,2,2,1,9,6,5,4,8,1,3,2,5};
        Map<Integer,Integer> hashMap = new HashMap<>();
        for(Integer i:numArray){
            hashMap.put(i, customCount(numArray, i));
            System.out.println(hashMap);
        }
    }
}