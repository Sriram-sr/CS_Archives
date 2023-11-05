import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class OddFreq {
    static ArrayList<String> oddFrequecyLetters(String str){
        HashMap<String,Integer> dict = new HashMap<String,Integer>();
        String[] str_list = str.split("");
        ArrayList<String> uniqueList = new ArrayList<String>();
        for(String each : str_list){
            if(!uniqueList.contains(each)){
                uniqueList.add(each);
            }
        }
        System.out.println(uniqueList);
        for(String each:uniqueList){
            int temp = getCount(str_list, each);
            dict.put(each,temp);
        }
        ArrayList<String> min_freqList = new ArrayList<String>();
        for(String key: dict.keySet()){
            if(dict.get(key)==1){
                min_freqList.add(key);
            }
        }
        return min_freqList;
    }

    static int getCount(String[] list, String element){
        int count = 0;
        for(String each:list){
            if(each.equals(element)){
                count+=1;
            }
        }
        return count;
    }

    public static void main(String args[]){
        // oddFrequecyLetters("geekforgeeks");
        int[] numArray = new int[5];
        numArray[0] = 1;
        System.out.println(Arrays.toString(numArray));
        numArray[1] = 1;
        System.out.println(Arrays.toString(numArray));
    }
}
