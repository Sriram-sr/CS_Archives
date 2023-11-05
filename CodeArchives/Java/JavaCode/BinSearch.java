public class BinSearch {
    public static void main(String[] args) {
        int array[] = {10,20,30,40,50,60};
        int key = 400, low = 0, high = 5, flag = 0;
        while (low<=high){
            int mid = (low+high)/2;
            if(key==array[mid]){
                flag = 1;
                break;
            }
            else if(key<array[mid]){
                high = mid-1;
            }
            else if(key>array[mid]){
                low = mid+1;
            }
        }
        if(flag==1){
            System.out.println("Key is found");
        }
        else{
            System.out.println("Key is not found");
        }
    }
}        