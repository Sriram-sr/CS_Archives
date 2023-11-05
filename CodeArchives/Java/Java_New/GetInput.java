import java.util.Scanner;

public class GetInput {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        String skip = sc.next();
        if (skip=="p"){
            System.out.println(false);
        }
        System.out.println(skip);
        sc.nextLine();
        String another = sc.nextLine();
        if (another=="p"){
            System.out.println(true);
        }
        System.out.println(another);
    
    }
}
