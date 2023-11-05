public class NesingClass {
    int x = 50;

    void display(){
        System.out.println("main method");
    }

    class Outer{
        void outermethod(){
            System.out.println(x);
            System.out.println("This is outer method");
        }
    } 
    
    class Inner extends Outer{
        void innermethod(){
            System.out.println("This is inner method");
        }
    }

    public static void main(String args[]){
        System.out.println(true);
        NesingClass ref = new NesingClass();
        ref.display();
        NesingClass.Inner obj = ref.new Inner();
        obj.innermethod();
        obj.outermethod();

    }
    
}
