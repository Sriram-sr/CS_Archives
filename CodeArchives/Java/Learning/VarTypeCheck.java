public class VarTypeCheck {
    String cvar;
    static int count = 0;

    public int method(){
        count+=1;
        System.out.println(cvar);
        return 1;
    }

    public static void main(String args[]){
        VarTypeCheck obj1 = new VarTypeCheck();
        // System.out.println(obj1.cvar);
        // System.out.println(obj1.ivar);
        System.out.println(VarTypeCheck.count);
        System.out.println(obj1.method());
        System.out.println(obj1.method());
        System.out.println(obj1.method());
        System.out.println(obj1.method());
        System.out.println(VarTypeCheck.count);
        obj1.cvar = "value assigned with object";
    }
}
