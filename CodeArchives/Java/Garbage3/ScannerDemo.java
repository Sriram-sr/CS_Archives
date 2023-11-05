import java.util.Scanner;

public class ScannerDemo {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String fullstring = sc.nextLine();
        try{ Thread.sleep(2000); } catch (Exception e){}
        System.out.println(fullstring);
    }    
}
