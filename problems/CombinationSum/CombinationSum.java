package recursion;

import java.util.ArrayList;
import java.util.List;

/**
 * @author Ankit Kashyap on 04-11-2023
 */
/*
Given an array of positive integers arr[] and an integer x, The task is to find all unique combinations in arr[] where the sum is equal to x.
The same repeated number may be chosen from arr[] an unlimited number of times.
Elements in a combination (a1, a2, …, ak) must be printed in non-descending order.
(ie, a1 <= a2 <= … <= ak). If there is no combination possible print “Empty”.
 */
public class CombinationSum {
//    Time Complexity: O(2^t * k) where t is the target, k is the average length
    public void findCombination(List<Integer> array, int target, int index,
                                List<Integer> temp, List<List<Integer>> answer) {


    //base condition
    if(index==array.size())
    {
        if(target==0)
            answer.add(new ArrayList<>(temp));
        return;
    }

    // pick or not pick
        // to pick num at that index must  be smaller than target sum
        if(target >= array.get(index)){
            temp.add(array.get(index)); // add in list that potential combination
            //check for all combination when that index was picked
            findCombination(array,target-array.get(index),index,temp,answer);
            //when index was not picked
            temp.remove(array.get(index)); // back tracking and removing since it was picked already

        }
        //not picked
        findCombination(array,target,index+1,temp,answer);

}

    public static void main(String[] args) {
        ArrayList<Integer> arr = new ArrayList<>();

        arr.add(2);
        arr.add(4);
        arr.add(6);
        arr.add(8);

        int sum = 8;

        List<List<Integer> > ans = new ArrayList<>();
        CombinationSum combinationSum = new CombinationSum();
        combinationSum.findCombination(arr, sum,0,new ArrayList<>(),ans);
        for(List<Integer> list :ans){
            System.out.println(list);
        }
    }
}
