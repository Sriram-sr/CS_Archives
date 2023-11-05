import java.io.FileWriter;
import java.io.IOException;

public class JustWrite {
    public static void main(String args[]) throws IOException{
        FileWriter wf = new FileWriter("temp.txt",true);
        wf.write("\nappended");
        wf.append("dono");
        wf.close();
        System.out.println("Go and check");
    }
}
