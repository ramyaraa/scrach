import java.util.Scanner;

public class hh {

    public static void main(String[] args) {
    //String cars [][]= new String [][]{{"bmw","mersdes","cadelac","roserise"},{"good","bad","ugle","snta"}};
    int [][] num= new int [][]{{1,2,3,},{4,5,6},{7,8,9}};
    // System.out.println(cars[0]);
    // Scanner sc = new Scanner(System.in);

    num[2][1]= 5848;
    // for(int i=0;i<cars.length;i++) {
    //  for(int j=0;j<cars[i].length;j++)
    //  System.out.println(cars[i][j]);
    // }
    for(int i=0;i<num.length;i++) {
        for(int j=0;j<num[i].length;j++){

            System.out.print(num[i][j]+" ");
        }
        System.out.println(" ");
    }
  
}}


