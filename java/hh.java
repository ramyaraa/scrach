

public class hh {

    public static void main(String[] args) {
        int row = 5;
        for (int i=0;i<row;i++){
           for(int j=0;j<row;j++){
            if(i==j || i+j==4){
              if(i<=2){
                System.out.print("# ");
              }
              else{
                System.out.print("* ");
              }   
        }
        else if(j==2 && i>2){
          System.out.print("# ");
        }
        else{
          System.err.print("* ");
        }
}
System.out.println("  ");
}}
}

