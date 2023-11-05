public class ReinitialiseDemo {
    String ivar;

    ReinitialiseDemo(String cvar){
        ivar = cvar;
        System.out.println(ivar);
    }

    ReinitialiseDemo(ReinitialiseDemo instance){
        ivar = instance.ivar;
        System.out.println(ivar);
    }

    public static void main(String args[]){
        ReinitialiseDemo o = new ReinitialiseDemo("Sriram");
        ReinitialiseDemo o2 = new ReinitialiseDemo(o);
    }

}
