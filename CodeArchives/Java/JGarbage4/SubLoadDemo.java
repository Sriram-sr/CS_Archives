class Base{
    void show(){
        System.out.println("Show metho siper");
    }

    static {
        System.out.println("Super class static bloack");
    }
}

class Sub extends Base{
    static {
        System.out.println("Subclass static bloack");
    }
}

public class SubLoadDemo {
    public static void main(String args[]){
        Base ref = new Sub();
        
    }
}

