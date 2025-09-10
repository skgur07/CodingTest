import java.io.*;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {

        int[] arr = new int[3];

        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt(); int b = sc.nextInt(); int c = sc.nextInt();

        arr[0] = a;
        arr[1] = b;
        arr[2] = c;

        if(a == b && a == c ){
            System.out.println(10000 + a*1000);
        } else if (a == b || a == c || b == c){
            if ( a == b ) System.out.println(1000 + a*100);
            else if ( a == c ) System.out.println(1000 + a*100);
            else System.out.println(1000 + b*100);
        }else
            System.out.println(Arrays.stream(arr).max().getAsInt() * 100);
    }
}
