class Base{
    static void dummy(){
        System.out.println(true);
    }
}

public class InstanceCheck {
    public static void main(String args[]){
        // Base ref = new Base();
        Base.dummy();
        // System.out.println(ref instanceof Base);
    }
}
