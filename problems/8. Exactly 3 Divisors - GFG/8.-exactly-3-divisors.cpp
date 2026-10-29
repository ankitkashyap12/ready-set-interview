// { Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
//User function Template for C++

class Solution{
    public:
    //Just check if the prime number's square is within range
    //Squares of all prime numbers will always have 3 divisors
    int exactly3Divisors(int N)
    {
       int count=0;
       if(N<=1) return 0;
       for(int i=2;i*i<=N;i++){
           if(isPrime(i)) {
               if( i*i<=N)
                   count++;
           }
       }
       return count;
    }
    public:
    bool isPrime(int n){
        if(n==1) return false;
        if(n==2 or n==3) return true;
        if(n%2==0 or n%3==0) return false;
        for(int i=5;i*i<=n;i+=6){
            if(n%i==0 or n%(i+2)==0) return false;
        }
        return true;
    }
};

// { Driver Code Starts.


int main()
 {
    int T;
    
    //taking testcases
    cin>>T;
    while(T--)
    {
        int N;
        
        //taking N
        cin>>N;
        Solution ob;
        //calling function exactly3Divisors()
        cout<<ob.exactly3Divisors(N)<<endl;
    }
	return 0;
}  // } Driver Code Ends