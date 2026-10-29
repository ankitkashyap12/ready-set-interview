// { Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;
 

 // } Driver Code Ends
//User function Template for C++

class Solution
{
    public:
    //Function to find the first position with different bits.
    int posOfRightMostDiffBit(int m, int n)
    {
        if(m==n) return -1;
        int diff = m ^ n;
        return getFirstSetBit(diff);
    }
    
    int getFirstSetBit(int n)
    {
       int count=0;
       if(n==0)
        return 0;
       while(n>0){
           if(!(n & 1)){
               count++; //it is zero here hence increase index count
           }
           else{
            return count+1; // got one at this position
           }
           n=n/2; // removes last digit
       }
    }
};

// { Driver Code Starts.

// Driver Code
int main()
{   
    int t;
    cin>>t; //input number of testcases
    while(t--)
    {
         int m,n;
         cin>>m>>n; //input m and n
         Solution ob;
         cout << ob.posOfRightMostDiffBit(m, n)<<endl;
    }
    return 0;     
}   // } Driver Code Ends