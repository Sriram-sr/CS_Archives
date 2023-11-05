class Inherit_class {
    public void method(){
        System.out.println("Create a object in subclass");
    }    
}

public class Subclass extends Inherit_class{
    public static void main(String args[]){
        Inherit_class obj = new Inherit_class();
        obj.method();
    }
}
