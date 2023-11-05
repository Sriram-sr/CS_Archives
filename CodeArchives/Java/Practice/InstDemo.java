public class InstDemo {
    static int num;
    static String numvar = "124";

    InstDemo(int num){
        this.num = num;
    }

    public static void main(String args[]){
        InstDemo ref = new InstDemo(76);
        String var = Integer.toString(num);
        System.out.println(var);
        int ret = Integer.valueOf(numvar);
        System.out.println(ret);
        System.out.println("Hello Java");
    }
}

