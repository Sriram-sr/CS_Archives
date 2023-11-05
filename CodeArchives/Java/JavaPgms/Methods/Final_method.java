package Methods;

public class Final_method {
    static int addition(int num) {
        int current = 100;
        int answer = current + num;
        return answer;
    }

    static int subtraction(int num) {
        int result = 100 - num;
        return result;
    }

    static int factorial(int num) {
        int result = 1;
        while (num>0){
            result*=num;
            num--;
        }
        return result;
    }

    public static void main(String...args) {
        System.out.println(addition(8));
        System.out.println(subtraction(10));
        System.out.println(factorial(5));
    }
    }

