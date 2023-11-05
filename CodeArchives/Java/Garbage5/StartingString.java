import java.util.Arrays;
import java.util.ArrayList;

public class StartingString {
    static void splitandFind(String[] testArray, String start){
        String splitted[][] = new String[testArray.length][];
        for(int str=0;str<testArray.length;str++){
            String temp[] = testArray[str].split(" ");
            splitted[str] = temp;
        }
        ArrayList<String> strings = new ArrayList<>();
        for(String[] outer:splitted){
            for(String inner:outer){
                strings.add(inner);
            }
        }
        for(String each:strings){
            if (Character.toString(each.charAt(0)).equals(start)){
                System.out.println(each);
            }
        }
    }
    public static void main(String args[]){
        String[] testArray = {"gfg is good for learning", "Gfg is for geeks", "I love Gfg"};
        String letter = "l";
        splitandFind(testArray, letter);
    }
}
