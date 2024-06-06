import java.util.Scanner;
import java.util.Arrays;

public class hh {

    public static void main(String[] args) {
    //String cars [][]= new String [][]{{"bmw","mersdes","cadelac","roserise"},{"good","bad","ugle","snta"}};
    Scanner sc=new Scanner(System.in);
    System.out.println("enter number");
    int size = sc.nextInt();
    int[] x=new int[size];
    int [] y = new int[size];
    int [] both = new int[size*2];
    System.out.println("enter x");
    for(int i=0;i<x.length;i++){
        x[i]=sc.nextInt();
}
System.out.println("enter y");
for(int i=0 ; i<y.length;i++){
    y[i]=sc.nextInt();
}

    for(int i=0 ; i<size*2;i++){
        if(i<size){

            both[i]=x[i];
        }
        else{
                    both[i]=y[i-size];
                }
}
System.out.println("z is ");
for(int j=0 ; j<both.length;j++){
    System.out.print(both[j]+ " ");
}
System.out.println(" ");
System.out.println("what number do you search");
int userInput = sc.nextInt();
for(int i=0 ; i<both.length;i++){
    if(both[i]==userInput){
        System.out.println("found you search for "+i);
    }
}

for(int i=0 ; i<size;i++){
    for(int j=0;j<size;j++){
        if(x[i]==y[j]){
            System.out.println("the comman number "+x[i]);
        }
    }
}
    
}}


