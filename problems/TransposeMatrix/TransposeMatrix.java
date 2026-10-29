package arrays;

/**
 * @author Ankit Kashyap on 27-08-2023
 */
public class TransposeMatrix {

    public int[][] transposeMatrix(int[][] matrix) {
        // Write your code here.
        int row=matrix.length;
        int col=matrix[0].length;
        int[][] transpose= new int[col][row];
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                transpose[j][i]=matrix[i][j];
            }

        }
        return transpose;
    }
}
