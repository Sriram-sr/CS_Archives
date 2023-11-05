public class constCheck{
    static int largestThree(int x, int y, int z){
        if (x > y && x > z){
            return x;
        }
        else if (y > x && y > z){
            return y;
        }
        else{
            return z;
        }
    }
    public static void main(String args[]){
        System.out.println(Math.max(12.13, 19.67));
        System.out.println(largestThree(4, 9, 8));
    }
}