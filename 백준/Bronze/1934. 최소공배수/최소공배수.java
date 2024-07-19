import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int size = in.nextInt();

		for(int i = 0; i < size; i++) {
			int num1 = in.nextInt();
			int num2 = in.nextInt();
			
			int GCD = gcd(num1,  num2);
			long keep = (long) num1 * num2;
			long lcm = keep / GCD;

			System.out.println(lcm);
		}
	}

	private static int gcd(int a, int b) {
		int temp = 0;
		while(b != 0) {
			temp = a % b;
			a = b;
			b = temp;
		}
		return a;
	}
}
