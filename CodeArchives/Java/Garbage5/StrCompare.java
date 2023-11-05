import java.util.ArrayList;


public class StrCompare {
    public static void main(String args[]){
        String[] testArray = {"Gfg", "is", "not", "best", "and", "not", "cs"};
        String[] test = {"Its ok", "all ok", "wrong", "looks ok", "ok", "wrong","thats ok"};
        ArrayList<String> list = new ArrayList<>();
        String matchString = "ok";

        for(int word=0;word<test.length;word++){
            if(test[word].contains(matchString)){
                list.add(testArray[word]);
            }
        }
        System.out.println(list);
    }
}
