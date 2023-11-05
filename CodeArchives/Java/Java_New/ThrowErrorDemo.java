public class ThrowErrorDemo {
    static void throwdemo(){
        int num = 917;
        if (num<18){
            throw new ArrayIndexOutOfBoundsException("Access Denied");
        }
        else{
            System.out.println("Access permitted");
        }
    }

    public static void main(String args[]){
        throwdemo();
    }
}
