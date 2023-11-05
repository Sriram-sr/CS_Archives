public class ReferenceTest {
    String sname;
    int snumber;
    ReferenceTest(String sname, int snumber){
        this.sname = sname;
        this.snumber = snumber;
    }

    void printDetails(){
        System.out.println("The name is "+ sname);
    }

    public static void main(String args[]){
        ReferenceTest student1 = new ReferenceTest("Sriram",433);
        ReferenceTest student2 = new ReferenceTest("Mani", 9011);
        ReferenceTest student3 = new ReferenceTest("Hanish",112);
        student1.printDetails();
        student1.sname = "Verea";
        System.out.println(student1.sname);
        student1.printDetails();
        student2 = student1;
        System.out.println(student2.sname);

    }
}
