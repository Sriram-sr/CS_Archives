public class square_check{
	static boolean check_square(int number){
		if (number<1){
			return false;
		}
		
		while(number%3==0){
			number/=3;
		}

		return number==1;
	}

	public static void main(String args[]){
		int number = 45;
		System.out.println(check_square(number));
	}
}				
