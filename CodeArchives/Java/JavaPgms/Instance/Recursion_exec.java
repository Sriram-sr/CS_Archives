public class Recursion_exec {
    
    static void return_steps(int number,int count){
        if (number==1){
            System.out.println("It reached last step");
            System.out.println("The count is " + count);
        }
        else{
            count+=1;
            return_steps(number-1,count);
        }
    }

    public static void main(String args[]){
        int number = 20;
        int count = 0;
        return_steps(number, count);
    }
}
