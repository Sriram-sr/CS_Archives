public class JoinString {
    public static void main(String args[]){
        String[] test = {"Hello","The","Java"};
        String result = "";
        for(int i=0;i<test.length;i++){
            result+=test[i];
            if(i!=test.length-1){
                result+="-";
            }
        }

        System.out.println(result);
    }
}
