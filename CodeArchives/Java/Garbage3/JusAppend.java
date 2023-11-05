import java.io.FileWriter;
import java.io.BufferedWriter;
import java.io.IOException;

public class JusAppend {
    public static void main(String args[]){
        try{
            BufferedWriter writefile = new BufferedWriter(new FileWriter("temp.txt",true));
            writefile.write("\n appended");
            writefile.close();
        }
        catch (IOException e){
            e.printStackTrace();
        }
    }
}
