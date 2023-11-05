import java.util.ArrayList;

public class LongestPalStr {
    public static String longestPalindrome(String txt) {
        ArrayList<String> palindromeList = new ArrayList<>();
        if (txt.length() == 1) {
            palindromeList.add(Character.toString(txt.charAt(0)));
        }
        for (int i = 0; i < txt.length() - 1; i++) {
            String temp = Character.toString(txt.charAt(i));
            for (int j = i + 1; j < txt.length(); j++) {
                temp += txt.charAt(j);
                String rev = reverseString(temp);
                if (temp.equals(rev)) {
                    palindromeList.add(rev);
                }
            }
        }
        if (palindromeList.size() > 0) {
            int max_len = palindromeList.get(0).length();
            String max_str = palindromeList.get(0);
            for (String rev : palindromeList) {
                if (rev.length() > max_len) {
                    max_len = rev.length();
                    max_str = rev;
                }
            }
            return max_str;
        }

        return "c";
    }

    static String reverseString(String temp) {
        String t = "";
        for (int i = temp.length() - 1; i >= 0; i--) {
            t += temp.charAt(i);
        }
        return t;
    }

    static String cllone(String s){
        int start=0,end=0;//the pointers which extract the substring which is longest palindrome
        for(int i=0;i<s.length();i++)
        {
         int even_len=expandfromcentre(s,i,i+1);//compares the abba type
         System.out.println(even_len);
         int odd_len=expandfromcentre(s,i,i);//compares the aba type
         int len=Math.max(odd_len,even_len);//finds whose length of substring is greater
         if((end-start)<len)
         {
             start=i-(len-1)/2;  //arting and ending of longest substring
            end=i+(len/2);
         }
      } 
        return s.substring(start,end+1);
    }

    static int expandfromcentre(String s,int i,int j)
    {
    
        while(i>=0 && j<s.length() && s.charAt(i)==s.charAt(j))
            {
                i--;//goes toward the left side of centre
                j++;//goes toward the right side of centre
            }
            return j-i-1;//-1 because the j increments 1 to get out of loop
            //return the length of the palindromic substring
        }

    public static void main(String[] args) {
        String s = "babad";
        System.out.println(cllone(s));
    }
}
