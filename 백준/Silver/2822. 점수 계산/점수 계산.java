import com.sun.security.jgss.GSSUtil;

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int max = 8;
        int[] arr = new int[max];
        int[] tmp = new int[max];

        for( int i = 0; i < max; i++ ) {
            arr[i] = Integer.parseInt(bf.readLine());
        }

        System.arraycopy(arr, 0, tmp, 0, arr.length);
        Arrays.sort(tmp);

        int[] arr2 = new int[5];

        for(int i = 1; i <= 5; i++) {
            arr2[i-1] = tmp[max-i];
        }

        int total = 0;
        for (int i :
                arr2) {
            total += i;
        }

        System.out.println(total);

        for (int i = 0; i < 8; i++){
            for(int j = 0; j < 5; j++){
                if (arr[i] == arr2[j])
                    bw.write(i + 1 + " ");
            }
        }

        bw.flush();
        bw.close();

    }
}
