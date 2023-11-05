// A Java program to convert an ArrayList to arr[]
import java.io.*;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

class GFG {
	public static void main(String[] args)
	{
		ArrayList<Integer> al = new ArrayList<Integer>();
		al.add(10);
		al.add(20);
		al.add(30);
		al.add(40);

		Integer[] arr = new Integer[al.size()];
		arr = al.toArray(arr);
        System.out.println(Arrays.toString(arr));
		// for (Integer x : arr)
		// 	System.out.print(x + " ");
	}
}
