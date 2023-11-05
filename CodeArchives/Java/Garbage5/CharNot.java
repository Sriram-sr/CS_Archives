import java.util.ArrayList;

public class CharNot {
    public static void main(String args[]){
    String[] test_array = {"gfg", "is", "best", "for", "geeks"};
    char[] char_array = {'g', 'o'};
    ArrayList<String> result = new ArrayList<>();

    for(String word:test_array){
        int flag = 0;
        for(char each:char_array){
            if(word.contains(Character.toString(each))){
                flag = 1;
            }
        }
        if(flag==0){
            result.add(word);
        }
    }

    System.out.println(result);
    }
}
