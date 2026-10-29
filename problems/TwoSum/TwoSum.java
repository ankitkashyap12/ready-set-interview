package arrays;

import java.util.*;

/**
 * Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 *
 * You may assume that each input would have exactly one solution, and you may not use the same element twice.
 *
 * You can return the answer in any order.
 *
 * Variation : if it has duplicate
 * @author Ankit Kashyap
 */
class TwoSum {
    public static int[] twoNumberSumUsingMap(int[] array, int targetSum) {
        // O(n) & O(n)
        Map<Integer, Integer> indicesValue = new HashMap<>();
        for (int i = 0; i < array.length; i++) {
            int diff = targetSum - array[i];
            Integer diffInd;
            //instead can store as number as key and value as true and just return num if it's present in map
            if ((diffInd = indicesValue.get(diff)) != null) {
                return new int[]{array[diffInd], array[i]};
            }
            indicesValue.put(array[i], i);
        }
        return new int[0];
    }

    //2nd efficient solution
    public static  int[] twoSumBinary(int[] array, int targetSum){
        //O(nlog(n)) and O(1)
        Arrays.sort(array);

        int right=array.length-1;
        int left=0;
        while(left<right){
            int currentSum= array[left]+array[right];
            if(currentSum==targetSum)
                return new int[]{array[left],array[right]};
            else if(currentSum < targetSum)
                left++;
            else
                right--;

        }
        return new int[0];
    }

    public static int[] twoSumUsingSet(int[] array, int target){
        //this handles duplicity better than solution using map
        Set<Integer> numSet = new HashSet<>();
        for(int num: array){
            int targetNum = target-num;
            if(numSet.contains(targetNum))
                return new int[]{num,targetNum};
            numSet.add(num);
        }
        return new int[0];
    }

    public static void main(String[] args) {
        int sum = 5;
        int[] arr= new int[]{1, 2, 3};
        int[] result = twoSumUsingSet(arr,sum);
        System.out.printf(result[0]+" "+result[1]);

        Set<Integer[]> set = new HashSet<>();
        Integer[] inArr = new Integer[]{1,2};
        Integer[] inArr2 = new Integer[]{1,2};
        set.add(inArr);
        set.add(inArr2);
        if(set.contains(inArr))
        {
            System.out.println("tru");
            System.out.println("size "+set.size());
        }
    }
}

