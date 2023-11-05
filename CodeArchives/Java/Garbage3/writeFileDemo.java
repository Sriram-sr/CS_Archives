import java.io.FileWriter;
import java.io.IOException;

public class writeFileDemo {
   public static void main(String args[]) throws IOException{
    FileWriter file = new FileWriter("temp.txt");
    file.write("Helllo Java");
    file.close();
   } 
}
