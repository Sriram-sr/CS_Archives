class Student {
    private int num1 = 22;
    protected String txt = "Hello";
    public int num2 = 33;
    
}

class Person extends Student {
    public static void main(String[] args){
        Person obj = new Person();
        System.out.println("Accesible variables are " + obj.num2);
    }
}
