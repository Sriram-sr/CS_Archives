class A{
    public void show(){
        System.out.println("Method in A class");
    }
}


public class AnonymousDemo {
   public static void main(String args[]){
    A ref = new A(){
        public void show(){
            System.out.println("Method in Anonymous class");
        }
    };
    ref.show();
}
   }
