public class constructorDemo{
	int num;

	constructorDemo(int num){
		 num = num;
	}
	void meth(){
        	System.out.println(num);
	}

        public static void main(String args[]){
		constructorDemo obj = new constructorDemo(21);
		obj.meth();
	}
}	
