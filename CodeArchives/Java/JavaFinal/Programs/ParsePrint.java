public class ParsePrint {
    public static void main(String[] args) {
        String string = "a1b10";
        int contValue = 0;
        for(int i=0;i<string.length()-1;i++){
            if(i==contValue){
                continue;
            }
            if(Character.isDigit(string.charAt(i))){
                char temp = string.charAt(i-1);
                if(Character.isDigit(string.charAt(i+1))){
                    int loopRange = Integer.parseInt(Character.toString(string.charAt(i)))*10 + Integer.parseInt(Character.toString(string.charAt(i+1)));
                    for(int j=0;j<loopRange;j++){
                        System.out.print(temp);
                    }
                    contValue = i+1;
                }
                else{
                    for(int k=0;k<Integer.parseInt(Character.toString(string.charAt(i)));k++){
                        System.out.print(string.charAt(i-1));
                    }
                }
            }
        }
    }
}
