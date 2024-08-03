import java.util.Scanner;
 
public class Main{
 
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		int H = in.nextInt();
		int M = in.nextInt();
		int T = in.nextInt();
		
		int min = 60 * H + M;
		min = min + T;
		
		int hour = (min / 60) % 24;
		int minute = min % 60;
		
		System.out.println(hour + " " + minute);
	}
}