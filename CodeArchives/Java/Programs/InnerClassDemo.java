class Outerclass{
    int outerclassVariable = 500;

    class Innerclass{
        int innerclassvariable = 100;

        void innerMethod(){
            System.out.println("This is innerClass Method");
        }   
    }

    void outerMethod(){
        System.out.println("This is outer class method");
        Innerclass reference = new Innerclass();
        reference.innerMethod();
    }
}


public class InnerClassDemo {
    public static void main(String args[]){
        Outerclass ref = new Outerclass();
        ref.outerclassVariable=12;
        ref.outerMethod();
        Outerclass.Innerclass obj = new Outerclass().new Innerclass();
        System.out.println("calling using commonObject");
        obj.innerMethod();
    }
}
