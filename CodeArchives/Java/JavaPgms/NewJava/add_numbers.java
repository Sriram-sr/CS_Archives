public class add_numbers{

    static void my_func(int num){
        String number = Integer.toString(num);
        System.out.println(number);
        String type = number.getClass().getSimpleName();
        System.out.println(type);
    }
    public static void main(String args[]){
        // amstong using strings
        int num = 20;
        System.out.println((object)num)
        my_func(num);
    
        
    }
}