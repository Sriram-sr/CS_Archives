import java.util.*;

public class NoOfVowels {
    public static void main(String args[]){
        String input = "GeeksforGeeks";
        char[] vowels = {'a','e','i','o','u'};
        int count = 0;
        // change into arraylist
        List<Character> chararray = new ArrayList<Character>();
        for(char i: vowels){
            chararray.add(i);
        }
        for (int i=0;i<input.length();i++){
            // System.out.println(chararray.contains(input.charAt(i)));
            if (chararray.contains(input.charAt(i))){
                count+=1;
            }
        }
        System.out.println(count);
    }
}
