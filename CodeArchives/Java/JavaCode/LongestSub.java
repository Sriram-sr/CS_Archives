import java.util.ArrayList;
import java.util.Collections;

public class LongestSub {
    static int findLongest(String word){
        int idx, nxt, len = word.length(), resultInt = 0, alphaFlag = 0;
        for(idx=0;idx<len;idx++){
            if(!Character.isAlphabetic(word.charAt(idx))){
                alphaFlag = 1;
            }
        }
        ArrayList<String> subList = new ArrayList<>();
        ArrayList<Integer> lenList = new ArrayList<>();
        for(idx=0;idx<len;idx++){
            String sub = Character.toString(word.charAt(idx));
            for(nxt=idx+1;nxt<len;nxt++){
                if (!sub.contains(Character.toString(word.charAt(nxt)))){
                    sub+=word.charAt(nxt);
                }
                else{
                    break;
                }
            }
            subList.add(sub);
        }
        for(String sub: subList){
            lenList.add(sub.length());
        }
        if (word.length()>0){
            resultInt = Collections.max(lenList);
        }
        return resultInt;
    }

    public static void main(String[] args) {
        String s = " ";
        // checkNull(s);
        System.out.println(findLongest(s));
    }

    static void checkNull(String s){
        if (s==null){
            System.out.println(true);
        }
        else{
            System.out.println(false);
        }
    }
}
