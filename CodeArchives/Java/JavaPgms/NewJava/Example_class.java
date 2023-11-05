class Calculate{
    int num1,num2;

    public void execute(){
        int result = num1 + num2;
        System.out.println(result);
    }
}

public class Example_class{
    public static void main(String args[]){
        Calculate obj = new Calculate();
        System.out.println(obj.num1);   // after creating object if you don't assign variable(declared) will\
                   // print 0 
        obj.num1 = 21;    
        obj.num2 = 22;
        obj.execute();       
    }    
}