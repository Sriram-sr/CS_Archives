import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class CustomInput{
    public static void main(String args[]) throws IOException{
        // InputStreamReader ir = new InputStreamReader(System.in);
        // BufferedReader br = new BufferedReader(ir);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char cr = (char)br.read();
        String str = br.readLine();
        if (cr =='p'){
            System.out.println(true);
        }
        int num = Integer.parseInt(br.readLine());
        float fl = Float.parseFloat(br.readLine());
        System.out.println(num);
    }
}
