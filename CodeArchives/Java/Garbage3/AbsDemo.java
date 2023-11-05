abstract class AbsClass{
    abstract void show();

    void display(){
        System.out.println("Method in Absclass");
    }
}

interface Int{
    void show();

    default void displayInt(){
        System.out.println("Method in interface");
    }

    static void statmethod(){
        System.out.println("staticccc");
    }
}

class Commanner extends AbsClass implements Int{
    public void show(){
        System.out.println("I should write for absclass");
    }
}


public class AbsDemo {
    public static void main(String args[]){
        Commanner ref = new Commanner();
        ref.show();
        Int.statmethod();
    }
}
