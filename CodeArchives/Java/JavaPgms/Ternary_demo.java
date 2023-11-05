import java.util.Scanner;
public class Ternary_demo{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.print("Enter your marks : ");
        double marks = input.nextDouble();
        
        // if (marks > 35){
        //     System.out.println("student is passed");
        // }
        // else if (marks < 35){
        //     System.out.println("student is failed");
        // }

        String result = (marks > 35) ? "Passed" : "Failed"; // if else using ternary operation ?:
        System.out.println(result);

        int x=23,y=35,z;
        z = (x<y) ? x : y;    // to store less value using ternary
        System.out.println(z);

        }    

        }
    