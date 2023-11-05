import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class GetUsingBuffer {
    public static void main(String args[])throws IOException{
        String str = "";
        int i;
        while((i=System.in.read())!=13){
            str+=i;
            System.out.println(i);
        }
        System.out.println(str);
    }
}
