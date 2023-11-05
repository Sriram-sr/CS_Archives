class Base{
    protected void display(){
        System.out.println("Base class");
    }
}

class User extends Base{
    public void display(String sub){
        System.out.println("Subclass");
        System.out.println(sub);
    }
}


public class InheritOverload extends User{
    public static void main(String args[]){
        User ref = new User();
        ref.display();
        ref.display("Hell");
    }
}
