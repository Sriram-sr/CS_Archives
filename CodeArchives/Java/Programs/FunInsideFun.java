public class FunInsideFun {
    public void outer(){
        class Excuter{
            void inner(){
                System.out.println("This is innner method inside class");
            }
        }

        new Excuter().inner();
    }

    public static void main(String args[]){
        new FunInsideFun().outer();
    }
}
