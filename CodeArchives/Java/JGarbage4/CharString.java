import java.util.Arrays;

public class CharString {
    static void frequencyChars(String str, char[] arr){
        int[] match_array = new int[arr.length];
        int temp = 0;
        for(char j : arr){
            int count = 0;
            for(int i=0;i<str.length();i++){
                if(j==str.charAt(i)){
                    count+=1;
                }
            }
            match_array[temp] = count;
            temp+=1;
        }
        for(int i=0;i<match_array.length;i++){
            System.out.println("Character : "+arr[i]+" Frequency : "+match_array[i]);
        }
    }

    public static void main(String args[]){
        String str = "geeksforgeeks is best for geeks";
        char[] char_array = {'e','f','g'};
        frequencyChars(str, char_array);
    }
}
