// { Driver Code Starts
//Initial Template for C++

// C++ program to check if n is sparse or not
#include<iostream>
using namespace std;

 // } Driver Code Ends
//User function Template for C++

class Solution
{
    public:
    //Function to check if the number is sparse or not.
    // If we observer carefully, 
    // then we can notice that if we can use bitwise AND 
    // of binary representation of the "given number its "
    // right shifted number
    // "(i.e., half the given number) to figure out whether the number
    // is sparse or not. Result of AND 
    // operator would be 0 if number is sparse and non-zero if not sparse.
    bool isSparse(int n)
    {
        if (n & (n>>1))
            return false;
        return true;
    }
};

// { Driver Code Starts.

// Driver Code
int main()
{
    int t,n;
    
    //testcases
    cin>>t;
    while(t--)
    {
        //initializing n
        cin>>n;
        
        //printing 1 if isSparse() returns true
        //else 0
        Solution ob;
        if(ob.isSparse(n)){
            cout << "1" << endl;
        }
        else cout << "0" << endl;
        
    }
    return 0;
}
  // } Driver Code Ends