package Programs;
import java.util.ArrayList;

public class SpacesintoString
{
    static String combinetoString(char[][] charArray)
    {
        ArrayList<String> strArray = new ArrayList<>();
        for(char[] sub:charArray){
            String temp = "";
            for(char each:sub){
                temp+=each;
            }
            strArray.add(temp);
        }
        String resultString = "";
        for(int idx=0;idx<strArray.size();idx++){
            resultString+=strArray.get(idx);
            if(idx!=strArray.size()-1){
                resultString+=" ";
            }
        }
        return resultString;
    }

    public static void main(String args[])
    {
        char[][] test_list = {{'g', 'f', 'g'}, {'i', 's'}, {'b', 'e', 's', 't'}};
        System.out.println(combinetoString(test_list));
    }
}
