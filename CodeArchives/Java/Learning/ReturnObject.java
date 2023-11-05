class Base{
    void display(){
        System.out.println("Parent class");
    }
}

public class ReturnObject {
    public Base createObject(){
        Base ref = new Base();
        ref.display();
        return ref;
    }

    public static void main(String args[]){
        ReturnObject obj = new ReturnObject();
        System.out.println(obj.createObject());
    }
}
