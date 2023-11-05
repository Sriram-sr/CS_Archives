import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class WriteDemo {
    public static void main(String args[]) throws IOException{
        BufferedWriter writeFile = new BufferedWriter(new FileWriter("temp.txt",true));
        writeFile.write("\nHello Shell");
        writeFile.close();
    }
}
