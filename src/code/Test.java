package code;

public class Test {
    public static void main(String[] args) {


        System.out.println((1 + 1/(double)2 + 1/(double)4));


        System.out.println(1/(double)2);
//        int[] arr = new int[3];
//
//        for (int i = 0; i < arr.length; i++) {
//
//            arr[i] = i;
//        }
//
//        for(int i: arr)
//            System.out.println(i);
    }
    int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }
}

