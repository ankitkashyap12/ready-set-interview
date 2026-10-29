// { Driver Code Starts
//Initial Template for Java

/*package whatever //do not write package name here */

import java.io.*;
import java.util.*;
class Main {
	public static void main (String[] args) {
		Scanner sc=new Scanner(System.in);
		
		//taking total testcases
		int T=sc.nextInt();
		
		while(T-->0)
		{
		    Solution obj=new Solution();
		    int N;
		    
		    //taking N
		    N=sc.nextInt();
		    
		   //calling method digitsInFactorial()
		   System.out.println(obj.digitsInFactorial(N));
		    
		}
		
	}
}
// } Driver Code Ends


//User function Template for Java
// We know,
// log(a*b) = log(a) + log(b)

// Therefore
// log( n! ) = log(1*2*3....... * n) 
//           = log(1) + log(2) + ........ +log(n)

// Now, observe that the floor value of log base 
// 10 increased by 1, of any number, gives the
// number of digits present in that number.

// Hence, output would be : floor(log(n!)) + 1.

class Solution{
    public int digitsInFactorial(int N){
        if(N<0){
           return 0;
       }
       if(N<=1){
           return 1;
       }
       
        double digits=0;
        for(int i=2;i<=N;i++){
            digits+=Math.log10(i);
       }
       return (int)(Math.floor(digits))+1;
    }
}
