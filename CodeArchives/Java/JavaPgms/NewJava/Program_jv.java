public class Program_jv {
    void function(){
        System.out.println("Touch if You can");
    }

    public static void main(String args[]){
        Program_jv obj = new Program_jv(); // since function is non static you have to create object
        obj.function();
    }

}