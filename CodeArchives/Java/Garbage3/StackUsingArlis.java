import java.util.ArrayList;

public class StackUsingArlis {
    ArrayList<Integer> stack;
    int size_limit;
    int stack_size;

    StackUsingArlis(){
        stack = new ArrayList<Integer>();
        size_limit = 5;
        stack_size = 0;
    }

    ArrayList<Integer> add(int element){
        if(stack_size<size_limit){
            stack.add(element);
            stack_size+=1;
        }
        else{
            System.out.println("Stack full");
        }
        return stack;
    }

    ArrayList<Integer> pop(){
        stack.remove(stack_size-1);
        stack_size-=1;
        return stack;
    }

    public static void main(String args[]){
        StackUsingArlis user = new StackUsingArlis();
        int num = 100;
        double d = num;
        System.out.println(d);
    }
}
