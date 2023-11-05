import java.utils.*;
public class Check_type {
    public static void main(String args[]){
        String newstr = "Hello Java";
        int number = 6;
        var dummy = 2.23342;
        
        System.out.println("The datatype of "+newstr+" is "+(newstr.getClass().getSimpleName()));
        System.out.println("The datatype of "+number+" is "+((Object)number).getClass().getSimpleName());
        // System.out.println("The datatype of var type initialized data is "+dummy.getClass().getSimpleName());
        System.out.println(((Object)dummy).getClass().getSimpleName());
        
    }
}
