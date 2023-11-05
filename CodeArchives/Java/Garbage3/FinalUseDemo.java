class FinalClass{
    void show(){
        System.out.println("Final class method");
    }
}

class Getter extends FinalClass{
    final void finalMethod(){
        System.out.println("This is final metod");
    }
}

public class FinalUseDemo {
    public static void main(String args[]){
        Getter g = new Getter();
        g.finalMethod();
    }
}
