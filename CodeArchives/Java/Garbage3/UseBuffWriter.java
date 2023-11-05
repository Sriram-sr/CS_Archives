import java.io.FileWriter;
import java.io.BufferedWriter;

public class UseBuffWriter {
    public static void main(String args[]){
        try{
            // FileWriter writefile = new FileWriter("temp.txt");
            String fileName = "temp.txt";
            BufferedWriter out = new BufferedWriter(
                new FileWriter(fileName, true));
            // BufferedWriter bw = new BufferedWriter(writefile,true);
            out.write("\nHello World");
            out.close();
        }
        catch (Exception e){
            e.printStackTrace();
        }
    }
}
