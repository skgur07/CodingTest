package algorithm;

import java.util.Scanner;

public class NumberFlipAndComparison {
    public static void main(String[] args) {
        Scanner sc1 = new Scanner(System.in);
        Scanner sc2 = new Scanner(System.in);

        int a = sc1.nextInt(); // 1234
        int b = sc2.nextInt(); // 5678

        int tmp1 = 0;
        int tmp2 = 0;

        int num1 = 0;
        int num2 = 0;

        int imsi1 = a;
        int imsi2 = b;

        while(a / 10 != 0) {

            tmp1 = a % 10;     //2
            a = a / 10;        //1
            num1 = num1 * 10 + tmp1;   //

        }
        num1 = num1 * 10 + a % 10;

        while(b / 10 != 0) {
            tmp2 = b % 10;
            b = b / 10;
            num2 = num2 * 10 + tmp2;
        }
        num2 = num2 * 10 + b % 10;

        if (num1 > num2) {
            System.out.println(num1);
        }
        if (num2 > num1) {
            System.out.println(num2);
        }

    }
}


// 1234, 5678

// 4321, 8765


