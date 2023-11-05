import java.io.*;
import java.util.*;

public class Solution {
    static int cvar = 21;
    Solution(){
        int numbers = 23;
    }
    public static void main(String[] args) {
        // this.cvar = 21;
        System.out.println(cvar);
        Scanner input = new Scanner(System.in);
        int number = input.nextInt();
        Double doub_val = input.nextDouble();
        input.nextLine();
        String txt = input.nextLine();
        Solution obj = new Solution();
    
        System.out.println("String: "+ txt);
        System.out.println("Double: "+ doub_val);
        System.out.println("Int: "+ number);  
              
    }
}

// import java.util.*;

// class UserInputDemo1 {
//     public static void main(String[] args) {
//         // Scanner sc = new Scanner(System.in); // System.in is a standard input stream
//         // // System.out.print("Enter a string: ");
//         // Double doub_val = sc.nextDouble();
//         // String str = sc.nextLine(); // reads string
//         // System.out.print("You have entered: " + str);
//         String txt = "1a3";
//         Integer number = Integer.valueOf(txt);
//         System.out.println(number.getClass().getSimpleName());
//     }
// }
