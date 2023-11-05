public class Multi_meth {
    
    public void method_1(){
        System.out.println("Create object and call");
    }

    public void method_2(){
        System.out.println("This is method two");
    }

    public static void main(String args[]){
        Multi_meth obj = new Multi_meth();
        obj.method_1();
        obj.method_2();
    }
}
