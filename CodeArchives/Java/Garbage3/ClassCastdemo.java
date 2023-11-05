class Super{
    void meth(){
        System.out.println("Super class");
    }
}

class Sub extends Super{
    void meth(){
        System.out.println("Sub class");
    }

    static void createCast(Super ref){
        Sub obj = (Sub)ref;
        System.out.println("referenced ...");
    }
}


public class ClassCastdemo {
    public static void main(String args[]){
        Super ref = new Sub();
        Sub.createCast(ref);
    }
}
