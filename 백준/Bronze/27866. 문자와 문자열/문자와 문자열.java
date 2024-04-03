import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		String string = in.next();
		int n = in.nextInt()-1;
		
		System.out.println(string.charAt(n));
	}
}