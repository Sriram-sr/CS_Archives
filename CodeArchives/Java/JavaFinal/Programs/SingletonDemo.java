class Singleton{
    private static Singleton singleinstance;

    int cvar = 23;

    private Singleton(){
        System.out.println("Singletion class is instantiated");
    }

    public static Singleton createInstance(){
        if (singleinstance==null){
            singleinstance = new Singleton();
        }
        return singleinstance;
    }
}


public class SingletonDemo {
    public static void main(String args[]){
        Singleton instance1 = Singleton.createInstance();
        Singleton instance2 = Singleton.createInstance();
        instance1.cvar = 98;
        System.out.println(instance2.cvar);
        System.out.println(instance2.hashCode());
    }
}
