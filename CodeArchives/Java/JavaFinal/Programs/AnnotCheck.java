class Provider{
    @Deprecated
    void funtner(){
        System.out.println("sheee");
    }
}

class Getter extends Provider{
    void funtner(){
        System.out.println("Overrided");
    }
}

public class AnnotCheck {
    public static void main(String[] args) {
        Provider ref = new Getter();
        ref.funtner();        
    }
}
