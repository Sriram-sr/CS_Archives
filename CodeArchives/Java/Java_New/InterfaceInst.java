interface A{
    void simple();
}

public class InterfaceInst {
    public static void main(String args[]){
        A ref = new A(){
            public void simple(){
                System.out.println("Created a instance for interface");
            }
        };
        ref.simple();
    }
}
