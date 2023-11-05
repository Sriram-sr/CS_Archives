import java.util.Collections;
import java.util.Comparator;
import java.util.ArrayList;

class Student
{
    String name;
    int marks;
    int roll;

    Student(String name, int marks, int roll)
    {
        this.name = name;
        this.marks = marks;
        this.roll = roll;
    }

    public String toString()
    {
        return "Student: "+ name+" Roll: "+roll+" Marks: " +marks;
    }
}


public class ComparatorDemo {
    public static void main(String args[]){
        ArrayList<Student> stList = new ArrayList<>();        
        Student st1 = new Student("Sriram", 98, 1);
        Student st2 = new Student("Mani", 33, 2);
        Student st3 = new Student("Shankhar", 61, 3);
        Student st4 = new Student("Aravindh", 77, 4);
        Student st5 = new Student("Kumar", 87, 5);

        stList.add(st1);
        stList.add(st2);
        stList.add(st3);
        stList.add(st4);
        stList.add(st5);

        Comparator<Student> com = new Comparator<Student>() {
              public int compare(Student s1, Student s2)
              {
                if (s1.marks<s2.marks){
                    return 1;
                }
                return -1;
              }
    };
        Collections.sort(stList,com);

        for(Student st:stList){
            System.out.println(st);
        }
    }
}   


