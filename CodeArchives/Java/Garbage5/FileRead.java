import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class FileRead {
    public static void main(String args[]) throws FileNotFoundException{
        File readFile = new File("E:\\CSS\\first_file.html");
        Scanner file = new Scanner(readFile);
        while(file.hasNext()){
            String temp = file.nextLine();
            System.out.println(temp);
        }
    }
}
