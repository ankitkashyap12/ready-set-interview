package arrays;

import java.util.Arrays;

/**
 * @author Ankit Kashyap on 27-08-2023
 * <p>
 * Given an array of positive integers representing the values of coins in your
 * possession, write a function that returns the minimum amount of change (the
 * minimum sum of money) that you
 * create. The given coins can have
 * any positive integer value and aren't necessarily unique (i.e., you can have
 * multiple coins of the same value).</p>
 * <b>Approach:</b><p>so we will first sort array, then one by one will check starting from 1st
 * element if that change can be made.
 * It is observed that if change is made up say K it mean all integer between 1..k are changes
 * that can be made.
 * <br>we will track change and if next intger is greater than change+1 it means smallest change
 * that can be made is currenChange+1' Intuitively to think if next no is less than change +1
 * it means that all changes upto next intger V can be made using V+1,V+2,V+3...etc.  </p>
 * more :
 *
 * Iterating through the example array [1,1,3,6,13], where:
 * - S represents the set of numbers we have gone through in the for loop
 * - C represents the maximum achievable change for set S (i.e. change achievable in S is 1..C)
 *
 * S = {}
 * C = 0
 * ---
 * S = {} U {1} = {1}
 * C = 1
 * ---
 * S = {1} U {1} = {1,1}
 * C = 2 (we can make both 1 and 2, because above we were able to create 1 and then we add 1, so that means we can also create 1+1=2)
 * ---
 * S = {1,1} U {3} = {1,1,3}
 * C = 5 (we can make 1..5, because above, we were able to create 1 and 2, we just added 3; and since we know we could
 * create 1 and 2 from above, that means that we can create 3+1=4, as well as 3+2=5)
 * ---
 * S = {1,1,3} U {6} = {1,1,3,6}
 * C = 11 (we can make 1..11, because we know we can create 1..5 from above and, when we add 6 to the set, we can now create 6,
 * as well as 6+1=7, 6+2=8 ... 6+5=11)
 * ---
 * S = {1,1,3,6} U {13}
 * C = 11 (we should be able to make 1..24, but we know we can create 1..11 from above and now we are trying to add 13 to the set;
 * as we can see 1..24 is not achievable, since we don't have the element 12 in the set and no combination of previous
 * numbers can add up to 12 [previous set only goes to C=11])
 *
 * Therefore, the smallest unachievable change is C + 1 = 12 and the logic of checking coin < (change + 1) comes from here.
 */
public class NonConstructibleChange {

    public int nonConstructibleChange(int[] coins) {
        // Write your code here.
        int currentChange=0;
        Arrays.sort(coins);
        for(int coin : coins){
            if(currentChange+1 < coin)
                return currentChange+1;
            currentChange+=coin;
        }
        return currentChange+1;
    }
}
