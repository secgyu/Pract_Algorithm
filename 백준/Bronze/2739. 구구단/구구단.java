import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);

		int a = in.nextInt();

		for(int j = 1; j<=9; j++) {
			System.out.println(a+" "+"*"+" "+j+" = "+(a*j));
		}
	}
}
