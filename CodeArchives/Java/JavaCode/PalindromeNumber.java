public class PalindromeNumber {
    static boolean checkPalindrome(int num){
        int temp = 0, rem, result = num;
        while (num>0){
            rem = num%10;
            temp = temp*10 + rem;
            num/=10;
        }
        if (result==temp){
            return true;
    }
    return false;    
}

    public static void main(String args[]){
        int num = 121;
        System.out.println(checkPalindrome(num));
    }
}
