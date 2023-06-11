import java.util.Arrays;

public class Problem_34 {
    static int[] findRange(int nums[], int target) {
        int[] rangeArray = new int[2];
        int idx, flag = 0;
        if (nums.length == 1 && nums[0] == target) {
            rangeArray[0] = 0;
            rangeArray[1] = 0;
            return rangeArray;
        }
        for (idx = 0; idx < nums.length; idx++) {
            if (idx == 0 && nums[idx] == target) {
                rangeArray[0] = 0;
                rangeArray[1] = 0;
                flag = 1;
            } else if (nums[idx] == target) {
                flag = 1;
                rangeArray[0] = idx - 1;
                rangeArray[1] = idx;
            }
        }
        if (flag == 0) {
            rangeArray[0] = -1;
            rangeArray[1] = -1;
        }

        return rangeArray;
    }

    public static void main(String args[]) {
        int[] nums = { 6, 5, 8, 8, 2, 1 };
        int target = 8;
        // int[] result = findRange(nums, target);
        // System.out.println(Arrays.toString(result));
        int stIdx = search(nums, target, true);
        System.out.println(stIdx);
    }

    static int search(int[] nums, int target, boolean findStartIndex) {
        int ans = -1;
        int start = 0;
        int end = nums.length - 1;
        while (start <= end) {
            System.out.println("start " + start + " end " + end);
            int mid = start + (end - start) / 2;
            System.out.println("mid " + mid);
            if (nums[mid] > target)
                end = mid - 1;
            else if (nums[mid] < target)
                start = mid + 1;
            else {
                ans = mid;
                if (findStartIndex)
                    end = mid - 1;
                else
                    start = mid + 1;
            }
            System.out.println("ans " + ans);

        }
        return ans;
    }
}