for (int i=0 ; i<n ;i++){
        for(int j=0;j<n; j++){
          if(i+j>=n-1){
        
              System.out.print("* ");
              //   continue;
            }
            else{
              System.out.print("  ");
          }
          }
          System.out.println(" ");
      }
      for (int i=0 ; i<n ;i++){
        for(int j=0;j<n; j++){
          if(i+j<n-1){
        
              System.out.print("* ");
              //   continue;
            }
            else{
                System.out.print("  ");
          }
          }
          System.out.println(" ");
      }