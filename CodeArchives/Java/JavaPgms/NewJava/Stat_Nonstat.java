public class Stat_Nonstat {
    
    static void mystaticmethod(){
        System.out.println("This is a static method that can be called without a object");
    }
    
    void myunstaticmethod(){
        System.out.println("You have to create object to call");
    }
    
    public static void main(String[] args){
        mystaticmethod();
        Stat_Nonstat obj = new Stat_Nonstat();
        obj.myunstaticmethod();
    }
}
