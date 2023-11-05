class Check {
    static{
        System.out.println("This is static block");
    }

    {
        System.out.println("Instance bloack");
    }
}

public class InstatntBlock{
    public static void main(String args[]){
        System.out.println("not known");
        Check ref = new Check();
    }
}
