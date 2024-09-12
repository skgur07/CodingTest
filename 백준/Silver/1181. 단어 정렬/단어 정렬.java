import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());


        ArrayList<String> ls = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            ls.add(s);
        }

        ls = ls.stream().distinct().collect(Collectors.toCollection(ArrayList::new));
        
        Collections.sort(ls, new Comparator<String>() {
            public int compare(String s1, String s2) {

                if (s1.length() == s2.length()) {
                    return s1.compareTo(s2);
                }

                return s1.length() - s2.length();
            }
        });

        for (String str :
                ls) {
            System.out.println(str);
        }
    }
}
