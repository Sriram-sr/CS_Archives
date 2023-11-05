public class GetPosition {
    static int getPosition(int n, int[] arr){
        int pos, res = -1;
        for(pos=0;pos<arr.length;pos++){
            if(arr[pos] == pos+1){
                res = pos+1; 
            }
        }
        return res;
    }
    public static void main(String args[]){
        int N = 5;
        int Arr[] = {15, 2, 45, 12, 7};
        System.out.println(getPosition(N, Arr));
    }
}