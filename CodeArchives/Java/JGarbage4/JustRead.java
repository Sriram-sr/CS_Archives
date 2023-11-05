import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;

public class JustRead {
    public static void main(String args[]) throws FileNotFoundException{
        File readfile = new File("notes.txt");
        Scanner sc = new Scanner(readfile);

        while(sc.hasNext()){
            String temp = sc.nextLine();
            System.out.println(temp);
            try{ Thread.sleep(500); }
            catch(InterruptedException e){}
        }
    }    
}
