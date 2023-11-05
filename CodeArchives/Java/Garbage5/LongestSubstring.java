import java.util.Arrays;
import java.util.ArrayList;

public class LongestSubstring {
    static String subString(String[] strList){
        String sample = strList[0];
        String[] trimmedList = Arrays.copyOfRange(strList, 1, strList.length);
        ArrayList<String> subStrings = new ArrayList<>();
        for(String word:trimmedList){
            String temp="";
            for(int idx=0;idx<sample.length();idx++){
                if (idx<word.length()){
                    if(sample.charAt(idx)==word.charAt(idx)){
                        temp+=word.charAt(idx);
                    }
                }
            }
            subStrings.add(temp);
        }
        String min_str = subStrings.get(0);
        for(String sub:subStrings){
            if(sub.length()<min_str.length()){
                min_str = sub;
            }
        }
        return min_str;
    }

    public static void main(String ars[]){
        String[] strList = {"float", "flower", "flight", "floor"};
        System.out.println(subString(strList));
    }
}
