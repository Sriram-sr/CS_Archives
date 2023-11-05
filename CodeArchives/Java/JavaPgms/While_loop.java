import java.util.Scanner;

public class While_loop {
    public static void main(String[] list) {
    int n = 5;
    int i =0;

    while (i<=n){
        System.out.println("Number is " + i);
        i++;
        if (i == 3){
            break;
        }
    }

    // while (true) {
    //     System.out.println("Hello java");
    // }
}    
}
