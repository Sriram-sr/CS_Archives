import java.util.ArrayList;

public class HighFreq {
    public static void main(String args[]){
        int[] array = {4, 6, 4, 3, 3,6,6, 3,6, 3, 8};
        ArrayList<Integer> uniqueList = new ArrayList<Integer>();
        for (int num:array){
            if (!uniqueList.contains(num)){
                uniqueList.add(num);
            }
        }
        ArrayList<Integer> countList = new ArrayList<Integer>();
        for (int num:uniqueList){
            int count = 0;
            for(int old:array){
                if (num==old){
                    count+=1;
                }
            }
            countList.add(count);
        }
        int max_count = countList.get(0);
        for(int num:countList){
            if (num>max_count){
                max_count = num;
            }
        }
        System.out.println(max_count);
        int matching_idx = countList.indexOf(max_count);
        System.out.println(matching_idx);
        System.out.println("Result is "+uniqueList.get(matching_idx));
    }
}
