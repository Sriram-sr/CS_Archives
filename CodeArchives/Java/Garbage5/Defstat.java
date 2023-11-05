interface Robuster{
    default void defaltMethod(){
        System.out.println("default of parent interface");
    }

    static void staticMethod(){
        System.out.println("static method in parent interface");
    }
    
    void normalMethod();
}


public class Defstat implements Robuster{
    public void normalMethod(){
        System.out.println("abstart method implemented ");
    }

    public static void main(String args[]){
        System.out.println(true);
    }
}
