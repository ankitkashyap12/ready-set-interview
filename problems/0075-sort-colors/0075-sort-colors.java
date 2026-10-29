class Solution {
    public void sortColors(int[] nums) {
        
        //reWrite(nums);
        //3 pointers
        //intution
        //0-low shoud be all zeroes
        //low-mid should be 1
        //mid-high unknown
        //high-end 2

        int mid=0;
        int low=0;
        int high= nums.length-1;
        while(mid<=high){
            if(nums[mid]==0){
                //move to 0-low region
                swap(nums,mid,low);
                low++;
                mid++;
            }
            else if(nums[mid]==1){
                mid++;
            }
            else{
                swap(nums,mid,high);
                high--;

            }
        }

        
    }

  static void swap(int[] nums,int i,int j){
    int temp=nums[i];
    nums[i]=nums[j];
    nums[j]=temp;

  }
    static void reWrite(int[] nums){
        int[] counts=new int[3];
        for(int color: nums){
            counts[color]+=1;
        }

        int color=0;
        int i=0;
        while(i<nums.length){

            if(counts[color]==0){
                //move to next color
                color++;
                continue;
            }
            nums[i]=color;
            counts[color]--;
            i++;
        }

    }
}