import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int size = in.nextInt();
		int how = in.nextInt();
		
		for(int i = 0; i < size; i++) {
			int num = in.nextInt();
			
			if(num < how) {
				System.out.print(num+" ");
			}
		}
	}
}

