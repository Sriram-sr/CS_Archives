package Programs;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

class Student implements Comparator<Student>
{
    int roll,marks;

    Student(int roll, int marks)
    {
        this.roll = roll;
        this.marks = marks;
    }

    @Override
    public String toString()
    {
        return "Roll: "+roll+" Marks: "+marks;
    }

    public int compare(Student s1, Student s2)
    {
        if(s1.marks<s2.marks)
        {
            return 1;
        }
        return -1;
    }
}
public class CompObj {
    public static void main(String args[])
    {
        ArrayList<Student> instanceList = new ArrayList<>();
        instanceList.add(new Student(1, 87));
        instanceList.add(new Student(2, 47));
        instanceList.add(new Student(3, 35));
        instanceList.add(new Student(4, 72));
        instanceList.add(new Student(5, 63));
        
        Collections.sort(instanceList,(s1,s2) -> {
            if(s1.marks > s2.marks){
                return 10;
            }
            return -1;
        });

        // Collections.sort(instanceList);

        for(Student s:instanceList){
            System.out.println(s);
        }
        
    }
}
