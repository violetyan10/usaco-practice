//student teach and perosn.....
//extend
class Person{
    // eat wow
    public double eat(){
        System.out.println("I am eating wow so fat");
        return 100.0;
    } 
}
class Teacher extends Person{
    public double teach(){
        System.out.println("I am teaching wow");
        return 2.00;
    }
}
class Student extends Person{
    public double learn(){
        System.out.println("I am learning so boring");
        return 4.0;
    }
}
public class School{
    public static void main(String[] args){
        Teacher feng= new Teacher();
        feng.teach();
        
    }
}