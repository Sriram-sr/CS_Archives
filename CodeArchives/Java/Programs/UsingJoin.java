package Programs;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Stack;

public class UsingJoin
{
    static void charToStrArray(char[][] charArray)
    {
        ArrayList<String[]> fakelist = new ArrayList<>();
        for(int i=0;i<charArray.length;i++)
        {
            String temp[] = new String[charArray[i].length];
            for(int j=0;j<charArray[i].length;j++)
            {
                temp[j] = Character.toString(charArray[i][j]);
            }
            String fakeString = "";
            for(String[] lis: fakelist){
                // fakeString+=
                String tempi = String.join("", lis);
                System.out.println(tempi);
            }
            System.out.println(fakeString);
        }
    }
    public static void main(String args[])
    {
        // String[][] test_list = {{"g", "f", "g"}, {"i", "s"}, {"b","e", "s", "t"}};
        // for(String[] sub:test_list){
        //     String temp = String.join("", sub);
        //     // System.out.println(temp);
        // }
        // char[][] charArray = {{'g', 'f', 'g'}, {'i', 's'}, {'b', 'e', 's', 't'}};
        // charToStrArray(charArray);
        Stack<Integer> stack = new Stack<>();
        stack.push(2);
        stack.push(12);
        stack.push(29);
        stack.push(82);
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
    }
}
