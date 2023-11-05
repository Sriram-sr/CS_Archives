abstract class AbsClass{
    abstract void abs();

    protected void display(){
        System.out.println(true);
    }
}

class User extends AbsClass{
    void normal(){
        System.out.println("this is normal");
    }

    protected void display(){
        System.out.println("Intermediate...");
    }
    
    public void abs(){
        System.out.println("abstract implemented successfully");
    }
}

public class AbstractDemo extends User{
    public static void main(String args[]){
        User ins = new User();
        ins.abs();
        ins.display();
    }
}
