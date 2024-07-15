import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str = scanner.nextLine();
        scanner.close();

        // 공백을 기준으로 나누어 토큰에 저장한다
        StringTokenizer st = new StringTokenizer(str, " ");
        System.out.println(st.countTokens());
    }
}