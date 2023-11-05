public class overLoadConst {
    overLoadConst(int num,String txt){
        num = num;
        txt = txt;
        System.out.println(num);
    }

    // overLoadConst(int num,String txt){
    //     num = num;
    //     txt = txt;
    // }

    public static void main(String args[]){
        overLoadConst obj = new overLoadConst(21, "Hello");
    }
}
