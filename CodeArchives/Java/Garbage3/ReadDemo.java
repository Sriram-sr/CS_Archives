import java.util.Scanner;
import java.io.File;

public class ReadDemo {
    public static void main(String args[]){
        try{
            File readfile = new File("notes.txt");
            Scanner scan = new Scanner(readfile);

            while(scan.hasNextLine()){
                String templine = scan.nextLine();
                System.out.println(templine);
            }
            scan.close();
        }
        catch(Exception e){
            e.printStackTrace();
        }
    }
}
