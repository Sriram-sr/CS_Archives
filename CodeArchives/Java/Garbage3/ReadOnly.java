import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;

public class ReadOnly {
    public static void main(String args[]){
        try{
            File readfile = new File("temp.txt");
            Scanner file = new Scanner(readfile);

            while (file.hasNextLine()){
                String templine = file.nextLine();
                System.out.println(templine);
                Thread.sleep(500);
            }

            file.close();
        }
        catch (Exception e){
            e.printStackTrace();
        }
    }
}
