public class StringPool {
    public static void main(String args[]){
        String str1 = "Python";
        String str2 = new String("Python").intern();

        System.out.println(str1==str2);
        System.out.println(str1.hashCode());
        System.out.println(str2.hashCode());

    }
}
