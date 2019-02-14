package madhavi;
 import java.util.Scanner;

/**
 * Hello world!
 *
 */
public class Driver 
{
    public static void main( String[] args )
    {
        System.out.println( "Hello World! from Driver class" );
    	Scanner input = new Scanner (System.in);
    	System.out.print("Input your first name: ");
    	String fname = input.next();
    	System.out.print("Input your last name: ");
    	String lname = input.next();
    	System.out.println();
    	System.out.println("Hello \n"+fname+" "+lname);
  

    }
}
