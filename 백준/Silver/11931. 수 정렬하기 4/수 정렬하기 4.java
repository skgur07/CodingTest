import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(bf.readLine());
        Integer[] arr = new Integer[n];

        for (int i = 0; i < n; i++ ){
            arr[i] = Integer.parseInt(bf.readLine());
        }

        Arrays.sort(arr, (a, b) -> b - a);


        for (int i :
                arr) {
            bw.write(i + " ");
        }
        
        bw.flush();
        bw.close();

    }
}
