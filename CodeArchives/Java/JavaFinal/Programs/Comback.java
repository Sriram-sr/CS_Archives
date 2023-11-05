
import java.util.ArrayList;


public class Comback {
    public static void main(String args[])
	{
		String[] ar1 = { "Article", "in", "Geeks", "for", "Geeks" };

		String[] ar2 = { "Geeks", "for", "Geeks" };

        notInList(ar1, ar2);

	}
	
	static void notInList(String[] ar1, String[] ar2)
	{
        ArrayList<String> result = new ArrayList<>();
		for(String ar:ar1){
            for(String ab: ar2){
                if(ar==ab){
                    System.out.println(ar);
                }
            }
        }
			
	}
}
