import java.util.Arrays;

class Handler<T>
{
    T instance;

    Handler(T reference)
    {
        instance = reference;
    }

    T getInstance()
    {
        return instance;
    }
}

public class GenericClassCreate {
    public static void main(String[] args) {
        int[] array1 = {1,2,2,1};
        int[] cloneArray = new int[array1.length];
        for(int i=0;i<cloneArray.length;i++){
            cloneArray[i] = array1[array1.length-1-i];
        }
        System.out.println(Arrays.toString(cloneArray));
        if(Arrays.equals(array1, cloneArray)){
            System.out.println(true);
        }
        else{
            System.out.println(false);
        }
    }
}
