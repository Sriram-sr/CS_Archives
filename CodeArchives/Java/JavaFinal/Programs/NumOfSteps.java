public class NumOfSteps {
    public static void main(String[] args)
    {
        int num = 123;
        int steps = 0;
        while(true)
        {
            if (num==0)
            {
                break;
            }
            if(num%2==0)
            {
                num = num/2;
                steps+=1;
            }
            else
            {
                num = num-1;
                steps+=1;
            }
        }
        System.out.println(steps);
    }
}
