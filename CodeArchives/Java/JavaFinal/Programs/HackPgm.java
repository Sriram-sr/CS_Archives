import java.io.*;
import java.util.*;

class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String first = sc.nextLine();
        String second = sc.nextLine();
        String third = sc.nextLine();
        String[] fList = first.split(" ");
        String[] sList = second.split(" ");
        String temp = sList[1];
        sList[1] = "0"+temp;
        String[] tList = third.split(" ");
        temp = tList[1];
        tList[1] = "0"+temp;
        System.out.println("================================");
        System.out.println(fList[0]+"           "+fList[1]);
        System.out.println(sList[0]+"            "+sList[1]);
        System.out.println(tList[0]+"         "+tList[1]);
        System.out.println("================================");
    }
}

