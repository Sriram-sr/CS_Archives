import java.util.ArrayList;

public class countList
{
    public static void main(String args[])
    {
        String test = "geekksforgggeeks";
        ArrayList<Integer> countList = new ArrayList<>();
        int length = test.length();
        
        for(int i=0;i<length;i++)
        {
            if(i!=0)
            {
                if(test.charAt(i)==test.charAt(i-1))
                {
                    continue;
                }
            }

            if(i<length-1)
            {
                if(test.charAt(i)==test.charAt(i+1))
                {
                    int count = 0;
                    char temp = test.charAt(i);
                    for(int j=i;j<length;j++)
                    {
                        if(test.charAt(j)==temp)
                        {
                            count+=1;
                        }
                        else
                        {
                            countList.add(count);
                            break;
                        }
                    }
                }
                else
                {
                    countList.add(1);
                }
            }
            
        }

        System.out.println(countList);
    }
}
