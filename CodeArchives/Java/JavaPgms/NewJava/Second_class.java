class First_class {
    
    void str_method(String txt){
        System.out.println("The statement is "+txt);
    }

    void int_method(int number){
        int result = number + 5;
        System.out.println("The result is " + result);
    }
}

public class Second_class {
    public static void main(String[] args){
        First_class obj = new First_class();
        obj.str_method("Hello java");
        obj.int_method(90);
    }
}