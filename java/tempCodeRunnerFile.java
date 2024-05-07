 // average=sum/count;import java.util.Scanner;

import java.util.Scanner;

public class tempCodeRunnerFile {
    public static void main(String[] args) {
        int n;
        int larg=0;
        double average=0;
        double sum=0;
        int count=0;
        int sumEven=0;
        Scanner sc = new Scanner(System.in);
        for(;;){
            n = sc.nextInt();
            if(n>30){
                break;
            }
            else if(n<0){
                continue;
            }
            else{
                if(n>larg){
                    larg=n;
                }
                sum+=n;
                count++;
                if(n%2==0){
                    sumEven+=n; 
                }
            }
        }
        average=sum/count;
        System.out.println("sum of even number is: "+sumEven);
        System.out.println("average of all numbers: "+average);
        System.out.println("largest nimber is: "+larg);
        }

    }


