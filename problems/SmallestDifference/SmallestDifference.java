package arrays;

import java.util.Arrays;

/**
 * @author Ankit Kashyap on 30-08-2023
 * <p>
 * Write a function that takes in two non-empty arrays of integers, finds the
 * pair of numbers (one from each array) whose absolute difference is closest to
 * zero, and returns an array containing these two numbers, with the number from
 * the first array in the first position.
 * <p>
 * Note that the absolute difference of two integers is the distance between
 * them on the real number line. For example, the absolute difference of -5 and 5
 * is 10, and the absolute difference of -5 and -4 is 1.
 */
public class SmallestDifference {

    public static int[] smallestDifferenceNaive(int[] arrayOne, int[] arrayTwo) {
        // Write your code here.
        int currentMinDiff = Math.abs(arrayOne[0]-arrayTwo[0]);
        int[] closestPair = new int[2];
        for(int i=0;i<arrayOne.length;i++){
            for(int j=0;j<arrayTwo.length;j++){
                if(Math.abs(arrayOne[i]-arrayTwo[j]) < currentMinDiff){
                    closestPair[0]=arrayOne[i];
                    closestPair[1]=arrayTwo[j];
                    currentMinDiff = Math.abs(arrayOne[i]-arrayTwo[j]);
                }
            }
        }
        return closestPair;
    }

    public static int[] smallestDifference(int[] arrayOne, int[] arrayTwo) {
        // optimal using two pointers.
//        when firstNum is smaller thand num in second array we move forward in 1st
//        array as we want to minimize difference,moving in second one would have effectively
//        meant increasing gap between them

        int idx1=0;
        int idx2=0;
        Arrays.sort(arrayOne);
        Arrays.sort(arrayTwo);
        int[] smallestPair=new int[2];
        int currentDiff=Math.abs(arrayOne[0]-arrayTwo[0]);
        while(idx1 <arrayOne.length && idx2< arrayTwo.length){
            int firstNum=arrayOne[idx1];
            int secondNum=arrayTwo[idx2];
            System.out.println(" first  & second num "+firstNum+" "+secondNum);
            if(Math.abs(firstNum-secondNum) < currentDiff){
                currentDiff=Math.abs(firstNum-secondNum);
                smallestPair[0]=arrayOne[idx1];
                smallestPair[1]=arrayTwo[idx2];
            }
            //this is important as if we don;t have this condition, idx of both arrays won't be updated and will be in infinite loop
            if(firstNum==secondNum)
                return new int[]{firstNum,secondNum};
            if(firstNum < secondNum)
                idx1++;
            else if(firstNum > secondNum)
                idx2++;
            System.out.println("current index "+idx1+" "+idx2);
        }

        return smallestPair;
    }
}
