class Editor {
    public void supermeth(){
        System.out.println("Super class");
    }
}

public class Staff extends Editor{
    public void submethod(){
        System.out.println("Sub class");
    }
    public static void main(String args[]){
        Editor reference = new Staff();
        reference.supermeth();
        ((Staff)reference).submethod();
    }
}

