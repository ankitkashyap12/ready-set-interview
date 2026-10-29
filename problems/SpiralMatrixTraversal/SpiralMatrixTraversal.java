package arrays;

import java.util.ArrayList;
import java.util.List;

/**
 * @author Ankit Kashyap on 08-09-2023
 * <p>
 * <p>
 * Write a function that takes in an n x m two-dimensional array (that can be
 * square-shaped when n == m) and returns a one-dimensional array of all the
 * array's elements in spiral order.</p>
 * <p>
 * Write a function that takes in an n x m two-dimensional array (that can be
 * square-shaped when n == m) and returns a one-dimensional array of all the
 * array's elements in spiral order.</p>
 */
public class SpiralMatrixTraversal {


    public static List<Integer> spiralTraverse(int[][] array) {

        //same method can be mae recursive with base condition beiing one in while loop and while calling func again will increase/decrease row
        // Write your code here.
        int startRow = 0;
        int startCol = 0;
        int endRow = array.length - 1;
        int endCol = array[0].length - 1;
        List<Integer> result = new ArrayList<>();
        while (startRow <= endRow && startCol <= endCol) {
            //print remaining top row
            for (int col = startCol; col <= endCol; col++) {
                result.add(array[startRow][col]);
            }
            // print last remaining col
            for (int row = startRow + 1; row <= endRow; row++) {
                result.add(array[row][endCol]);
            }
            // print last remaining row in reverse(clocakwise)
            for (int bottomCol = endCol - 1; bottomCol >= startCol; bottomCol--) {
                //edge case
                //handle cae when there is single row in middle of matrix, we won;t need to count it it twice
                if (startRow == endRow) break;
                result.add(array[endRow][bottomCol]);
            }
            //print remaing left col from bottom to top
            for (int leftRow = endRow - 1; leftRow >= startRow + 1; leftRow--) {
                if (startCol == endCol) break;
                result.add(array[leftRow][startCol]);
            }
            startRow++;
            startCol++;
            endRow--;
            endCol--;
            System.out.println("array formed is " + result);
        }
        return result;
    }
}
