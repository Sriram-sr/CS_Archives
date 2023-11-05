public class CheckLetNum {
    public static void main(String args[]){
        String sample = "lop 12Heloa";
        int flag = 0;
        StringBuilder result = new StringBuilder();
        for (int i=0;i<sample.length();i++){
            if (Character.isDigit(sample.charAt(i))==true){
                flag = 1;
            }
        }
        if (flag==1){
            System.out.println(true);
        }
        else{
            System.out.println(false);
        }
    }    
}
