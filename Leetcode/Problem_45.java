public class Problem_45 {
    static int jump_game(int[] nums) {
        if (nums.length == 1) {
            return 0;
        }
        int pos = 1, count = 1;

        while (pos < nums.length - 1) {
            pos += nums[pos];
            count += 1;
        }

        return count;
    }

    public static int jump(int[] nums) {
       
        int n = nums.length;
        if (n == 1) return 0;
        
        // max steps that we can make in one window
        int max_steps = 0;
        int cur = 0;
        
        // jumps that we need to calculate
        int jumps = 0;
        
        // till n-1 because we have to reach at the end point which is n-1
        
        
        for (int i=0;i<n-1;i++){
            // System.out.println(i);
            // calculating the max at every point
            max_steps = Math.max(max_steps,i + nums[i]);
            System.out.println("Max "+max_steps+ " i "+i+" jump "+jumps);
            // whenever you reached the point where you dont have steps
            // you need to update the step with the max_steps till this index
            System.out.println("i "+i+ " curr "+ cur);
            if (cur == i){
                System.out.println("entered...");
                cur = max_steps;
                jumps++;
            }
            
            // if you already reached to end then no need to iterate further
            if (cur>n-1){
                System.out.println("curr end "+cur);
                return jumps;
            } 
            
        }
        return jumps;
    }

    public static void main(String args[]) {
        int[] nums = { 2,3,0,1,4 };
        System.out.println(jump(nums));
    }
}