public class calling_below_fn {
    public static void main(String args[]){
        calling_below_fn obj = new calling_below_fn();
        var result = obj.method();  // using var type variable to store the object result
        System.out.println(result);
        // System.out.println(obj.check(211));
        obj.check(211);

    }

    public int method(){
        System.out.println("Im called by object above");
        int num = 33;
        int mod=num%10;
        System.out.println(mod);
        return num;
    }

    public String check(int num){
        String str = String.valueOf(num);
        return str;
    }
}
