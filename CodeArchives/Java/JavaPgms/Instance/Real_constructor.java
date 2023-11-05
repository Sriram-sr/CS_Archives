public class Real_constructor {
    int val;
    Real_constructor(){
        val = 5;
        System.out.println("The value during initialisation is " + val);
    }

    public static void main(String[] args){
        Real_constructor obj = new Real_constructor();
        obj.val = 500;
        System.out.println("Val after creating object is " + obj.val);
        // String obj.brand = "Volvo";
        // System.out.println(obj.brand);
    }
}
