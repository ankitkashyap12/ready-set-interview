class Solution {
    public boolean isPalindrome(String s) {
        int left=0;
        int right= s.length()-1;
        s=s.toLowerCase();
        while(left<right){
            while(left<right && !Character.isLetterOrDigit(s.charAt(left))){
                left++;
            }
            while(left<right && !Character.isLetterOrDigit(s.charAt(right))){
                right--;  
            }
            char currLeft=Character.toLowerCase(s.charAt(left));
            char currRight = Character.toLowerCase(s.charAt(right));
            if(currLeft!=currRight)
                return false;
            left++;
            right--;

        }
        return true;
    }
}