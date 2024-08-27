import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int[] arr1 = new int[n];
        Integer[] arr2 = new Integer[n];

        for (int i = 0; i < n; i++) {
            arr1[i] = sc.nextInt();
        }

        for (int i = 0; i < n; i++) {
            arr2[i] = sc.nextInt();
        }

        Arrays.sort(arr1);
        Arrays.sort(arr2);

//        System.out.println(Arrays.toString(arr1));
//        System.out.println(Arrays.toString(arr2));

        List<Integer> list = Arrays.asList(arr2);
        Collections.reverse(list);
        Integer[] reverse_arr2 = list.toArray(arr2);

//        System.out.println(Arrays.toString(reverse_arr2));

        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += arr1[i] * reverse_arr2[i];
        }

        System.out.println(sum);
    }
}