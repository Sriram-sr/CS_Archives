class Baser{
	void display(){
		System.out.println("Out in basser");
	}
}

class Deriver extends Baser{
	@Override
	@SuppressWarnings("unchecked")
	void display(){
		System.out.println("Out in deriver");
	}
}

public class AnnotCheck{
	public static void main(String args[]){
		Baser ref = new Baser();
		ref.display();
	}
}