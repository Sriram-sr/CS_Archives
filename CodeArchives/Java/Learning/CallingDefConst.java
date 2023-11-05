public class CallingDefConst {
    CallingDefConst(){
        this(8); // calling parametrised const from default const
        System.out.println("I'm just printing");
    }

    CallingDefConst(int x){
        // this();
        System.out.println("I will take a parameter");
    }

    public static void main(String... array){
        // CallingDefConst o = new CallingDefConst(9);
        CallingDefConst o = new CallingDefConst();
    }
}
