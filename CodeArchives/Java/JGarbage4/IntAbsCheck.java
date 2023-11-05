interface myInt{
    int num = 21;
    void sum();
}

class Implementer implements myInt{
	public void sum(){
		System.out.println("Sum implemented");
	}
}

public class IntAbsCheck{
	public static void main(String args[]){
		Implementer ref = new Implementer();
		ref.sum();
		System.out.println(myInt.num);
	}
}