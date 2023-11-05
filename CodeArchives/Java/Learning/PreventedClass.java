class PreventedClass {
    // private PreventedClass(){ //this will make any subclasses not to create a object of class as constructor is private
    PreventedClass(){
        System.out.println("Constructor created");
    }

    protected void display(){
        System.out.println("Simple display");
    }
}

class Derived extends PreventedClass{
    void callSuper(){
        super.display(); // calling the super class method using super keyword.
    }
    public static void main(String args[]){
        Derived ref = new Derived();
        ref.display();
        ref.callSuper();
    }
}