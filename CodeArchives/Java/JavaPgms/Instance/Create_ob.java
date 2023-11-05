public class Create_ob {

    Create_ob(){
        System.out.println("This is a constructor which is called when an object is created");
    }
    int x = 21;
    void method(){
        System.out.println("Welcome back Java");
    }

    static void jumpFunc(){
        for(int i=0;i<=10;i+=2){
            System.out.println(i);
        }
    }
    public static void main(String args[]){
        Create_ob newobj = new Create_ob();
        newobj.method();
        System.out.println(newobj.x);
        jumpFunc();
    }
}