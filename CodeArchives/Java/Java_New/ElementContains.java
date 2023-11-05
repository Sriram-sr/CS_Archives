public class ElementContains {
    static boolean checkelement(int array[], int element){
        int flag = 0;
        for(int i: array){
            if (i==element){
                flag = 1;
            }
        }
        if (flag==1){
            return true;
        }
        else{
            return false;
        }
    }

    public static void main(String[] args){
        int[] array = {2,3,4,5,6,7};
        System.out.println(checkelement(array, -4));
    }
}
