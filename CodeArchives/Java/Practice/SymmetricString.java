import javax.swing.plaf.synth.SynthOptionPaneUI;

public class SymmetricString {
    String str;

    SymmetricString(){
        str = "level";
    }

    public boolean checkSymmetric(){
        String reverse = "";
        // boolean result;
        for(int i=str.length()-1;i>=0;i--){
            reverse+=str.charAt(i);
        }
        // result = str.equals(reverse);
        if (str==reverse){
            System.out.println(true);
        }
        else{
            System.out.println(false);
        }
        return true;
    }

    public static void main(String args[]){
        SymmetricString ref = new SymmetricString();
        ref.checkSymmetric();
    }
}
