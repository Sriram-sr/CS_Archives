import java.util.Arrays;

public class Array_demo {
    public static void main(String args[]) {
        int numbers[] = new int[5];
        System.out.println(Arrays.toString(numbers));  // to print the declared array 
        numbers[0] = 24;
        numbers[1] = 88;
        numbers[2] = 98;
        // numbers[9] = 99;
        System.out.println(Arrays.toString(numbers));

        int[] new_array = {2,3,4,5,'e',67};  // declaration of a array  // for char s ASCII value will be printed
        System.out.println(Arrays.toString(new_array));

        int array[] = {};  // declasring a emtpy array
        System.out.println(Arrays.toString(array));
        
        String[] str_array = {"Hello","Java"};  // declaring a string array
        System.out.println(Arrays.toString(str_array));

        char[] char_array = {'a','e','i','o','u'};
        System.out.println(Arrays.toString(char_array));

    }
    
}
