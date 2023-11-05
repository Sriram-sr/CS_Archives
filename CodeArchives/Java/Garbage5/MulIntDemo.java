interface Alarm{
    default String turnalarmOff(){
        return "Alarm alarm off";
    }

    default void alarmOwnMethod(){
        System.out.println("Own alarm method");
    }
}

interface Vehicle{
    default void turnalarmOn(){
        System.out.println("Vehicle alarm on");
    }

    default String turnalarmOff(){
        return "Vehicle alarm off";
    }
}


class Car implements Alarm, Vehicle{
    void carMethod(){
        System.out.println("This is a method inside car");
    }

    public String turnalarmOff(){
        return Alarm.super.turnalarmOff();
    }
}


public class MulIntDemo {
    public static void main(String args[]){
        Car ref = new Car();
        System.out.println(ref.turnalarmOff());
    }
}
