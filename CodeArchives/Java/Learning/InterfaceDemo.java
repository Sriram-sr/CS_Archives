interface Animal{
    void display();
    void enter();
}

class UseInterface implements Animal{
    public void display(){
        System.out.println("Hello");
    }

    public void enter(){
        System.out.println("Entering....");
    }
}

public class InterfaceDemo {
    public static void main(String[] args){
        UseInterface ref = new UseInterface();
        ref.display();
    }
}
