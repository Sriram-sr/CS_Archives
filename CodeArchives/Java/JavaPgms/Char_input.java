import java.util.Scanner;
public class Char_input {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a word: ");
        String new_char = input.next();  // thsi will take only the first word even if you type in a sentence
        System.out.println(new_char);
        System.out.println("Enter a character: ");
        char new_c = input.next().charAt(2);  // this will return character of index in word
        System.out.println(new_c);
    }
}
