import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class ReadFile {
    public static void main(String args[]) throws FileNotFoundException,IOException{
        // BufferedReader br = new BufferedReader(new FileReader("E:\\Java_New\\notes.txt"));
        BufferedReader br;
        br = new BufferedReader(new FileReader("E:\\Java_New\\notes.txt"));
        String content = br.readLine();
        System.out.println(content); 	


    }
}
