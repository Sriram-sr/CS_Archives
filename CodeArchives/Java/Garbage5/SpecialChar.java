public class SpecialChar {
    static boolean spclCharChecker(String test){
        System.out.println(Thread.currentThread());
        int flag = 0;
        for(int i=0;i<test.length();i++){
            if(Character.isLetter(test.charAt(i))){
                
            }
            else{
                flag = 1;
            }
        }
        if(flag!=1){
           return  true;
        }
        return false;
    }

    public static void main(String args[]){
        String test = "Geeks-ForGeeks";
        System.out.println(spclCharChecker(test));
        }    
}
