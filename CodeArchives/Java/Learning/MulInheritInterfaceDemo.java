class Mobile{
    void phonecall(){
        System.out.println("Phone call function");
    }
}

interface Smartphone{
    int number = 98;
    void sms();

    void camera();
}

interface Smartwatch{
    void blutooth();

    public static void ownMethod(){
        System.out.println("Method inside interface");
    }

    default void meth(){
        System.out.println("Access using implemented");
    }
}

class User extends Mobile implements Smartphone, Smartwatch{
    void phonecall(){
        System.out.println("User phonecall");
    }

    public void sms(){
        System.out.println("User sms function");
    }

    public void camera(){
        System.out.println("User camera function");
    }

    public void blutooth(){
        System.out.println("User blutooth function");
        // number = 32;  // you cannot change the value as it is final by default because of interface
    }

}

public class MulInheritInterfaceDemo {
    public static void main(String args[]){
        User sriram = new User();
        sriram.phonecall();
        sriram.sms();
        sriram.blutooth();
        sriram.meth();
        Smartwatch.ownMethod();
    }
}
