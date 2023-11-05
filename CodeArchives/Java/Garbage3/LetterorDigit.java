import java.util.Random;

import javax.swing.text.html.HTMLDocument.HTMLReader.IsindexAction;

public class LetterorDigit {
    public static void main(String args[]){
        Random rnd = new Random();
        System.out.println(rnd.nextInt(1,10));
        String str = "stringg";
        int numcount = 0, letcount = 0;
        boolean num,let;
        for(int i=0;i<str.length();i++){
                if (Character.isLetter(str.charAt(i))){
                    letcount+=1;
                }
                if (Character.isDigit(str.charAt(i))){
                    numcount+=1;
                }
            }
            if (numcount>0 && letcount>0){
                System.out.println(true);
            }
            else{
                System.out.println(false);
            }
        }
    }
