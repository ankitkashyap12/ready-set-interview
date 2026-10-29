class Solution {
    public int triangleNumber(int[] nums) {
        //valid traingle (a,b,c)
        //a>b+c
        //b>a+c
        //c>a+b

        //sort
        Arrays.sort(nums);
        //2,3,4,4
        //traverse from last to second last
        int count=0;
        for(int i=nums.length-1;i>=2;i--){
            int l=0;
            int r= i-1;
            while(l<r){
                if(nums[l]+nums[r]>nums[i]){
                    count+=r-l;
                    r--;
                }
                else
                    l++;

            }
        }
        return count;
        
    }
}