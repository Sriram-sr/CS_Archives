import java.util.Scanner;

public class New_file{
    public int adhoc(int num1,int num2){
        int result;
        result = num1 + num2;
        return result;
    }
   
    public int subhil(int num1,int num2){
        int result = num1 - num2;
        return result;
    }
    
    public int multis(int num1,int num2){
        int result = num1 * num2;
        return result;
    }

    public int divine(int num1,int num2){
        int result = num1/num2;
        return result;
    }
    
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number: ");
        sc.nextLine();    
    }
}    