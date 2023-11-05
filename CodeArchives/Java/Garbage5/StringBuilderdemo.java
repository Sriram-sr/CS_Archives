public class StringBuilderdemo {
    public static void main(String args[]){
        StringBuilder str = new StringBuilder("Hello");
        str.append(" World");
        System.out.println(str);
        str.insert(2, "okk");
        System.out.println(str);
        String nstr = str.toString();
        System.out.println(nstr.getClass().getSimpleName());
        System.out.println(str.reverse());
    }
}
