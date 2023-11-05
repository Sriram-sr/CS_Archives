package Collections;

import java.util.ArrayList;
import java.util.Collections;

class Laptop implements Comparable<Laptop>
{
    String model;
    int ram, price;

    Laptop(String model, int ram, int price)
    {
        this.model = model;
        this.ram = ram;
        this.price = price;
    }

    public String toString()
    {
        return "Model: "+model+" Ram: "+ram+" Price: "+price;
    }

    public int compareTo(Laptop lap)
    {
        if(this.price<lap.price){return 1;}
        return -1;
    }
    
}


public class comparableDemo
{
    public static void main(String args[])
    {
        ArrayList<Laptop> lapList = new ArrayList<>();
        lapList.add(new Laptop("Dell", 8, 40000));
        lapList.add(new Laptop("Lenovo", 8, 35000));
        lapList.add(new Laptop("Macintosh", 16, 80000));

        Collections.sort(lapList);
        
        for(Laptop lap:lapList){
            System.out.println(lap);
        }
    }
}
