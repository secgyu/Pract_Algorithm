
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		int x, y;
		
		Scanner in = new Scanner(System.in);
		
		x = in.nextInt();
		y = in.nextInt();
		
		if(x>0 && y>0)
		{
			System.out.println("1");
		}
		if(x < 0 && y > 0)
		{
			System.out.println("2");
		}
		if(x < 0 && y < 0)
		{
			System.out.println("3");
		}
		if(x > 0 && y <0)
		{
			System.out.println("4");
		}
	}
}
