interface Major{
    void seeIt();

    default void catchIt(){
        System.out.println("catchIt from major class");
    }
}

class Minor implements Major{
    public void seeIt(){
        System.out.println("seeIt from minor class");
    }
}


public class DefaultInf {
    public static void main(String args[]){
        Minor mn = new Minor();
        mn.catchIt();
        mn.seeIt();
    }
}
