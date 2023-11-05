public class ReplaceBuilder {
    public static void main(String[] args) {
        StringBuilder st = new StringBuilder("HelloJava");
        st.replace(1,2,"");
        System.out.println(st);
    }
}
