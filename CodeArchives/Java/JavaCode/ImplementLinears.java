public class ImplementLinears{
    public static void main(String args[]){
        int array[] = {2,3,4,5,6};
        int key = 41,flag=0;
        for(int i=0;i<array.length;i++){
            if (array[i] == key){
                flag=1;
                break;
            }
        }
        if (flag==1){
            System.out.println("Key is found");
        }
        else{
            System.out.println("Key not found");
        }
        
    }
}