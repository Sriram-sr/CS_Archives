import java.util.ArrayList;

public class LongestRep {
    public static void main(String args[]){
        String test = "aaaaa";
        String temp = "";
        ArrayList<String> SubList = new ArrayList<>();
        int length = test.length();

        for(int i=0;i<length;i++){
            if (temp.contains(Character.toString(test.charAt(i)))){
                SubList.add(temp);
                temp = "";
            }
            temp+=test.charAt(i);
            if(i==length-1){
                SubList.add(temp);
            }
        }

        System.out.println(SubList);
    }
}
