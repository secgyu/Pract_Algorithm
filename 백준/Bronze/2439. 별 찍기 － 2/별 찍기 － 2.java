import java.util.Scanner;

public class Main {

	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		
		int num = in.nextInt();
		
		for(int i = 0; i < num; i++) {
			for(int j = num; j>i+1; j--) {
				System.out.print(" ");
			}
			for(int k = 0; k<i+1; k++) {
				System.out.print("*");
			}
			System.out.println();
		}
	}
}
