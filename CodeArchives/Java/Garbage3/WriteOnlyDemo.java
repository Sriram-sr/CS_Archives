import java.io.FileWriter;
import java.io.IOException;

public class WriteOnlyDemo {
    public static void main(String args[]){
        try{
            FileWriter writefile = new FileWriter("temp.txt");
            writefile.write("demo");
            writefile.close();
        }        
        catch (IOException error){
            error.printStackTrace();
        }
    }
}
