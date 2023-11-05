import java.util.Collections;
import java.util.ArrayList;

class Manager implements Comparable<Manager>{
    int roll, marks;

    Manager(int roll, int marks){
        this.roll = roll;
        this.marks = marks;
    }

    public String toString(){
        return "Roll: "+roll+" Marks: "+marks;
    }

    public int compareTo(Manager ref){
        if(this.marks < ref.marks){
            return 1;
        }
        return -1;
    }
}


public class ComparableDemo {
    public static void main(String args[]){
        ArrayList<Manager> mnList = new ArrayList<>();
        mnList.add(new Manager(1, 76));
        mnList.add(new Manager(2, 89));
        mnList.add(new Manager(3, 63));
        Collections.sort(mnList);

        for(Manager mn:mnList){
            System.out.println(mn);
        }
    }
}
