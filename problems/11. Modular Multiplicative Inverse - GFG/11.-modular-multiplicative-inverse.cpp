// { Driver Code Starts
//Initial Template for C++

#include<iostream>
using namespace std;


 // } Driver Code Ends
//User function Template for C++

class Solution{
    public:
    //Complete this function
    int modInverse(int a, int m)
    {
        int x,y;
        int gcd = gcdExtended(a,m,&x,&y);
        int res= (x % m + m) % m;
        if((a*res)%m==1)
            return res;
        else
            return -1;
    }
    
    //Extended Euclid algo
    int gcdExtended (int a, int b, int* x, int* y) {
	if (a == 0) {
		*x = 0; *y = 1;
		return b;
	}
	int x1, y1;
	int d = gcdExtended (b%a, a, &x1, &y1);
	*x = y1 - (b / a) * x1;
	*y = x1;
	return d;
}
};

// { Driver Code Starts.

int main()
{
	int T;
	
	//taking testcases
	cin>>T;
	while(T--){
		int a,m;
		
		//taking input a and m
		cin>>a>>m;
		Solution ob;
		//calling function modInverse()
		cout << ob.modInverse(a, m)<<endl;
	}
    return 0;
}  // } Driver Code Ends