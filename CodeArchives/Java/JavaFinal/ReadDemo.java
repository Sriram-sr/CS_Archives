import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ReadDemo {
    public static void main(String args[]) throws FileNotFoundException{
        File f = new File("notes.txt");
        Scanner readFile = new Scanner(f);

        while(readFile.hasNext()){
            System.out.println(readFile.nextLine());
        }
    }
}
