import java.io.FileWriter;
import java.io.IOException;

public class FileCr {
    public static void main(String args[]) throws IOException{
        FileWriter writefile = new FileWriter("temp.txt",true);
        int i=0;
        while(i<5){
            writefile.write("\nHello Java");
            i++;
        }
        writefile.close();
    }    
}
