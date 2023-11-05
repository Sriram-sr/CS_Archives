package Programs;

import java.util.ArrayList;
import java.util.List;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;

public class CompIntf {
    public static void main(String args[]){
        Collection<Integer> collRefList = new ArrayList<>();
        List<Integer> listRefList = new ArrayList<>();
        ArrayList<Integer> plainArList = new ArrayList<>();

        collRefList.add(237);
        listRefList.add(237);
        plainArList.add(237);

        collRefList.add(133);
        listRefList.add(133);
        plainArList.add(133);

        collRefList.add(756);
        listRefList.add(756);
        plainArList.add(756);

        collRefList.add(398);
        listRefList.add(398);
        plainArList.add(398);

        Comparator<Integer> comp = new Comparator<Integer>() {
            public int compare(Integer num1,Integer num2){
                if(num1%10>num2%10){
                    return 1;
                }
                return -1;
            }
        };
        
        Collections.sort(plainArList,comp);
        System.out.println(plainArList);

    }
}
