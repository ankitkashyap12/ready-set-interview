class Solution {
    public boolean isPalindrome(int x) {
        if(x<10 && x>=0)
            return true;
        //negatives cannot be palindrome nor can nums ending with zero
        if(x<0 || x%10==0)
            return false;
        int rev=0;
        int num=x;
        while(x>rev){
            int dig=x%10;
            x=x/10;
            rev=rev*10+dig;
        }
        return (rev==x || rev/10==x);
        
    }
}