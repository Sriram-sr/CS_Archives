public class CheckBin {
    static boolean checkBinary(String test){
        int flag = 0;
        for(int letter=0;letter<test.length();letter++){
            if(!(test.charAt(letter)=='0' || test.charAt(letter)=='1')){
                flag=1;
            }                
        }
        if(flag==0){
            System.out.println(true);
            return true;
        }
        else{
            return false;
        }
    }
    

    public static void main(String args[]){
        String str = "0101010w01";
        System.out.println(checkBinary(str));
    }
}
