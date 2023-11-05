import java.io.FileWriter;
import java.io.BufferedWriter;
import java.io.IOException;

public class WriteFile {
    public static void main(String args[]) throws IOException{
        BufferedWriter appender = new BufferedWriter(new FileWriter("temp.txt",true));
        appender.write("loop");
        appender.close();
        System.out.println("Success append");
    }
}
