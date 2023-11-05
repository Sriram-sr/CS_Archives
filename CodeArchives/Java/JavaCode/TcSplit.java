import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		int tc = sc.nextInt();
        sc.nextLine();
		for(int i=0;i<tc;i++){
		    String tcLine = sc.nextLine();
            String array[] = tcLine.split(" ");
		    System.out.println(Integer.parseInt(array[0])-(Integer.parseInt(array[1]))+(Integer.parseInt(array[2])));		    
		}
	}
}
