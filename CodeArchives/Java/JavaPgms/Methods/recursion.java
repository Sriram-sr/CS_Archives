package Methods;

public class recursion {
    static int find_recursively(int num) {
        if (num==1){
            return num;
        }
        else{
            return num * find_recursively(num -1);
        }
    }

    public static void main(String args[]){
        System.out.println(find_recursively(5));
    }
    }

