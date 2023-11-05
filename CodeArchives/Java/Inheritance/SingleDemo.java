class Baseclass {
    public void display(){
        System.out.println("This is base class method");
    }
}

public class SingleDemo extends Baseclass{
    public static void main(String args[]){
        SingleDemo instance = new SingleDemo();
        // Baseclass obj = new Baseclass();
        // obj.display();
        instance.display();
    }
}