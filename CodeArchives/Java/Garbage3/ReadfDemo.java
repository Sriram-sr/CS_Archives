import java.io.FileWriter;
import java.io.File;
import java.io.IOException;

public class ReadfDemo {
    public static void main(String args[]){
        try{
            File file = new File("temp.txt");
            FileWriter writefile = new FileWriter(file);
            writefile.write("Hello Java");
            writefile.close();
        }
        catch (IOException e){
            e.printStackTrace();
        }
    }
}
