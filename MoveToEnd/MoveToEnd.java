//package arrays;

import java.util.List;

/**
 * @author Ankit Kashyap on 30-08-2023
 * <p>
 * You're given an array of integers and an integer. Write a function that moves
 * all instances of that integer in the array to the end of the array and returns
 * the array.
 */
public class MoveToEnd {

    public static List<Integer> moveElementToEnd(
            List<Integer> array, int toMove
    ) {
        // two pointers and swap
        int start =0;
        int end = array.size()-1;
        while(start<end){
            //edge when all elements are same as toMove then it will go till -1 giving out of bound
            while( end >=0 && array.get(end)==toMove ){
                end--;
            }
            // again checkinf start<end because end ws decremented above
            if(start < end && array.get(start)==toMove ){
                //swap

                int num = array.get(end);
                System.out.println("swapping with "+num);
                array.set(end,array.get(start));
                array.set(start,num);
                start++;
                end--;
            }
            else{
                start++;
            }
        }
        return array;
    }

    //without two while
    public static List<Integer> moveElementToEndOneWhile(
            List<Integer> array, int toMove
    ) {
        // two pointers and swap
        int start =0;
        int end = array.size()-1;
        while(start<end){
            if(array.get(end)!=toMove){
                if(array.get(start)==toMove){
                    int num = array.get(end);
                    array.set(end,array.get(start));
                    array.set(start,num);
                }
                start++;
            }
            else{
                end--;
            }
        }
        return array;
    }
}
