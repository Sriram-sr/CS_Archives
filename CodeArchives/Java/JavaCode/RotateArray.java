import java.util.Arrays;
import java.util.ArrayList;

public class RotateArray {
    // A non-recursive code that makes n calls
    // but takes O(1) extra space.
    static int pairSumSequence(int n) {
        int sum = 0;
        for (int i = 0; i < n; i++)
            sum += pairSum(i, i + 1);
        return sum;
    }

    static int pairSum(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        int array[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        int value = 3;
        System.out.println(pairSumSequence(5));
    }
}