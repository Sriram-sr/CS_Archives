interface Newest{
	void something();
}

class Olest implements Newest{
	public void something(){
		System.out.println(false);
	}
}

public class Instant{
	public static void main(String args[]){
		Olest ref = new Olest();
		System.out.println(ref instanceof Newest);
	}
}