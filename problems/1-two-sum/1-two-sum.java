class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> indicesValue=new HashMap<>();
        for(int i=0;i<nums.length;i++){
            int diff = target-nums[i];
            Integer diffInd;
            if((diffInd = indicesValue.get(diff))!=null){
               return new int[] {diffInd,i};
            }
            indicesValue.put(nums[i],i);
        }
        return null;
}
}