public class CurrClassMeth {
    
    void inner(){
        System.out.println("Im inner method");
    }

    void outer(){
        System.out.println("Going to call inner");
        this.inner();
        System.out.println("Im outer");
    }

    public static void main(String args[]){
        CurrClassMeth o = new CurrClassMeth();
        o.outer();
    }
}
