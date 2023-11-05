package Programs;

import java.util.Random;

public class CalcTime {
    static void randomFromList(){
        int array[] = {2,3,4,5,1,9,8,7,11,17};

        for(int i=0;i<10;i++){
            System.out.println(array[new Random().nextInt(array.length)]);
        }
    }
    public static void main(String args[])
    {
        Random rand = new Random();
        System.out.println(rand.nextInt(1,2));
        // randomFromList();
    }
}
