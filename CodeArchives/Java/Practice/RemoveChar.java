public class RemoveChar {
    public static void main(String args[]){
        String str = "HelloJava", newstr = "";
        System.out.println(str.indexOf("J"));
        for(int i=0;i<str.length();i++){
            if (str.charAt(i)=='J'){
                continue;
            }
            newstr+=str.charAt(i);
        }
        System.out.println(newstr);
    }
}
