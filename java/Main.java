import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int m=0;
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int a;
        while(n>0){
        a = n%10;
        a++;
        m =m*10+a;
        n = n/10;
        }
        n = m;
        m = 0;
        while(n>0){
        a = n%10;
        m =m*10+a;
        n = n/10;
        }


        
     System.out.println(m);
    }
}