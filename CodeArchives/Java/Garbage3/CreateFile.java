import java.io.File;
import java.io.IOException;

public class CreateFile{
    public static void main(String args[]) throws IOException{
        File file = new File("temp.txtss");
        try{
            System.out.println(file.createNewFile());
        }
        catch (Exception error){
            // System.out.println(error);
            error.printStackTrace();
        }
}
}