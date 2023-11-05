import java.io.File;
import java.io.IOException;

public class CreateRead {
    public static void main(String args[]){
        try{
            File file = new File("temp.txt");
            file.createNewFile();
        }
        catch (IOException error){
            error.printStackTrace();
        }
    }
}
