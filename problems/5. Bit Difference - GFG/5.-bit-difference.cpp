// { Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
//User function Template for C++

class Solution{
    public:
    // Function to find number of bits needed to be flipped to convert A to B
    // XOR of two number will have set bits only at 
    // those places where A differs from B. 
    int countBitsFlip(int a, int b){
        
        // Your logic here
        return countSetBits(a^b);
        
    }
    int countSetBits(int n){
        int count=0;
        while(n > 0){
            count++;
            n&=(n-1);
        }
        return count;
    }
};

// { Driver Code Starts.

// Driver Code
int main()
{
	int t;
	cin>>t;// input the testcases
	while(t--) //while testcases exist
	{
		int a,b;
		cin>>a>>b; //input a and b

        Solution ob;
		cout<<ob.countBitsFlip(a, b)<<endl;
	}
	return 0;
}  // } Driver Code Ends