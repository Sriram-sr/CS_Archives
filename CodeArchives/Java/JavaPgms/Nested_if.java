import java.util.Scanner;

public class Nested_if {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter your marital status : ");
        String  marital = input.nextLine();
        System.out.println("Enter your age : ");
        int age = input.nextInt();
        System.out.println("Enter your gender: ");
        String gender = input.nextLine();
        
        if(marital == "married") {
            System.out.println("You are eligible");

        }
    }
    
}
