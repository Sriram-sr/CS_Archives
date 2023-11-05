interface BaseInt{
    String execute(String str, int num);
}

class User implements BaseInt{
    public String execute(String name, int num){
        return name+" "+num;
    }
}
    
public class LambdaEx{
    public static void main(String args[]){
        BaseInt ref = (String name, int num) -> {
            return name+" "+num;
        };
        System.out.println(ref.execute("Sriram", 22));
    }
}