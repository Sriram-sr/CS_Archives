import java.util.ArrayList;
import java.util.Arrays;

public class ImplementStack {
    int size;
    int stack[];

    ImplementStack(){
        size = 1;
        stack = new int[5];
    }

    String add(int element){
        try{
            stack[size-1] = element;
            this.size+=1;
            return Arrays.toString(stack);
        }
        catch (IndexOutOfBoundsException e){
            return "Stack is full";
        }
    }

    ArrayList<Integer> pop(){
        ArrayList<Integer> popped = new ArrayList<Integer>();
        for(int i=0;i<size-2;i++){
            popped.add(stack[i]);
        }
        System.out.println(popped);
        return popped;
    }

    public static void main(String args[]){
        ImplementStack user = new ImplementStack();
        System.out.println(user.add(5));
        System.out.println(user.add(5));
        System.out.println(user.add(5));
        System.out.println(user.add(5));
        System.out.println(user.pop());
        System.out.println(user.add(15));
    }
}
