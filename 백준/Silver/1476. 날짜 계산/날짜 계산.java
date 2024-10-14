import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        final int E_MAX = 15;
        final int S_MAX = 28;
        final int M_MAX = 19;

        int[] arr = new int[3];
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < 3; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int[] arr1 = {1, 1, 1};

        int i = 1;
        while (true) {

            if (Arrays.equals(arr, arr1)) {
                break;
            }

            for (int j = 0; j < 3; j++ ) {
                arr1[j] += 1;
            }

            if (arr1[0] > E_MAX) {
                arr1[0] = 1;
            }
            if (arr1[1] > S_MAX) {
                arr1[1] = 1;
            }
            if (arr1[2] > M_MAX) {
                arr1[2] = 1;
            }

            i++;
        }


        bw.write(i +"");
        bw.flush();
        bw.close();
    }
}
