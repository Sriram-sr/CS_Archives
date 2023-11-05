import java.math.BigDecimal;
import java.util.Scanner;

public class StrtoNum {
    public static void main(String args[]){
        String instant = System.console().readLine("Enter: ");
        System.out.println(instant);
        Scanner sc = new Scanner(System.in);
        String newline = sc.nextLine();
        System.out.println(newline);
        BigDecimal num1 = new BigDecimal("23");
        BigDecimal num2 = new BigDecimal("3.23");
        BigDecimal result = num1.add(num2);
        BigDecimal result2 = num1.subtract(num2);
        System.out.println(result2);
        System.out.println(result);
        String str = "198";
        int num = 234;
        int numstr = Integer.valueOf(str);
        String strnum = Integer.toString(num);

        int check = 21;
        switch (check){
            case 1:
                System.out.println("The number is one");
                break;
            case 2:
                System.out.println("The number is two");
                break;
            case 3:
                System.out.println("The number is three");    
                break;
            default:
                System.out.println("No number is found");    
        }

        
    }
}
