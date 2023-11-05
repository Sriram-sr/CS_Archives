class PrivateClass {
    private int number = 34;
    private String text = "anystring";
    static int statnumber = 223;

    String getter(){
        return text;
    }

    void setter(String altname){
        text = altname;
    }

}

public class GetterSetter{
    public static void main(String... args){
        // System.out.println(PrivateClass.statnumber);
        PrivateClass ref = new PrivateClass();
        ref.setter("dennis");
        System.out.println(ref.getter());
    }
}
