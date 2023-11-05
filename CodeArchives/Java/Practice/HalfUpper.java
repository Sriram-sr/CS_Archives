public class HalfUpper {
    static String usingToUpper(String text){
        int half = text.length()/2;
        String res_text="";
        for (int i=0;i<text.length();i++){
            if (i<half){
            res_text+=Character.toUpperCase(text.charAt(i));
            }
            else{
                res_text+=text.charAt(i);
            }
        }
        return res_text;
    }
    public static void main(String args[]){
        String text = "Hackerrank";
        System.out.println(usingToUpper(text));
    }
}
