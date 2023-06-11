import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class Problem_49 {
    static List<List<String>> groupAnagrams(String[] strs) {
        int word, nxt, let, flag;
        List<List<String>> output = new ArrayList<>();
        List<Integer> indexes_list = new ArrayList<>();
        for (word = 0; word < strs.length; word++) {
            if (!(indexes_list.contains(word))) {
                List<String> sub_list = new ArrayList<String>();
                sub_list.add(strs[word]);
                for (nxt = word + 1; nxt < strs.length; nxt++) {
                    String string = strs[nxt];
                    flag = 0;
                    for (let = 0; let < string.length(); let++) {
                        if (!(strs[word].contains(Character.toString(string.charAt(let))))) {
                            flag = 1;
                        }
                    }
                    if (flag == 0) {
                        sub_list.add(string);
                        indexes_list.add(nxt);
                    }
                }
                output.add(sub_list);
            }
        }
        return output;
    }

    public static void main(String args[]) {
        String[] strs = { "eat", "tea", "tan", "ate", "nat", "bat" };
        System.out.println(groupAnagrams(strs));
    }
}