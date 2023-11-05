class A {
    private int a = 0;

    private int getA() {
        System.out.println("getA() method");
        return a;
    }

    public void setA(int aa) {
       if (aa > 10)
          a = aa;
    }

    public static void main(String[] args) {
        A aObject = new A();
        aObject.setA(100); // No way to set 'a' to such value as this method call will
                           // fail due to its enforced rule.
        System.out.println("aObject value is: " + aObject.getA());
     }

}
    

// class B{
//     public static void main(String args[]){
//         A obj = new A();
//         obj.setA(100);
//         System.out.println(obj.getA());
//     }
// }

