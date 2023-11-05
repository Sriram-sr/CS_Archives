public class SumNPrdctArry {
    public static void main(String args[]){
        SumNPrdctArry instance = new SumNPrdctArry();
        int array[] = {2,3,4,5,7,};
        instance.sumofArray(array);
    }

    void sumofArray(int[] array){
        int sum,product;
        sum = 0;
        product = 1;
        for (int i=0;i<array.length;i++){
            sum+=array[i];
            product*=array[i];
        }
        System.out.println("Sum is "+sum);
        System.out.println("Product is "+product);
        
    }
}
