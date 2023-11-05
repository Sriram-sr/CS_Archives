import java.io.File;
import java.io.IOException;

public class CreateFile {
    public static void main(String args[]) throws IOException{
        String filename = "temp.txt";
        File file = new File(filename);
        System.out.println(file.createNewFile());
    }
}
