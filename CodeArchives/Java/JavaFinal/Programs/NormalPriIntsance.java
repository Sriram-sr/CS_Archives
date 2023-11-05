class CheckSingleton{
    int cvar = 23;

    private CheckSingleton(){
        System.out.println("Object is instantiated");
    }

    static CheckSingleton createInstance(){
        CheckSingleton ref = new CheckSingleton();

        return ref;
    }
}


public class NormalPriIntsance {
    public static void main(String args[]){
        CheckSingleton inst1 = CheckSingleton.createInstance();
        CheckSingleton inst2 = CheckSingleton.createInstance();
        CheckSingleton inst3 = CheckSingleton.createInstance();
        System.out.println(inst1.hashCode());
        System.out.println(inst2.hashCode());
    }
}
