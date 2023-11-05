public class Obj_Creation {
    
    class NewClass{
        int num1,num2;

        public void add(){
            int res;
            res = num1+num2;
            System.out.println(res);
        }
    }

    public static void main(String...args){
        NewClass obj.new NewClass();
        obj.num1 = 25;
        obj.num2 = 80;
        obj.add();

    }
    
}
