// { Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

 public class GFG_2 {
	
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		
		//Input testcases
		int testcases = sc.nextInt();
		while(testcases-- > 0)
		{
		    //input size of Array
		    int sizeOfArray = sc.nextInt();
		    int arr[] = new int[sizeOfArray];
		    
		    //input elements in the Array
		    for(int i = 0; i < sizeOfArray-1; i++)
		    {
		        int x;
		        x = sc.nextInt();
		        arr[i] = x;
		    }
		    
		    //input index
		    int index = sc.nextInt();
		    //input element
		    int element = sc.nextInt();
		    
		    Solution_2 obj = new Solution_2();
		    
		    //calling insertAtIndex() function
		    obj.insertAtIndex(arr,sizeOfArray,index,element);
		    
		    //Printing the array for verification
		    for(int i = 0; i < sizeOfArray;i++)
		    {
		        System.out.print(arr[i] + " ");
		        
		    }
		    
		    System.out.println();
		}
	}
}


// } Driver Code Ends


//User function Template for Java

//Complete this function, Geeks
class Solution_2
{
    // You need to insert the given element at the given index. 
    // After inserting the elements at index, elements
    // from index onward should be shifted one position ahead
    // You may assume that the array already has sizeOfArray - 1
    // elements.
    public void insertAtIndex(int arr[],int sizeOfArray,int index,int element)
    {
        for(int i = sizeOfArray-1; i > index; i--) {
            arr[i] = arr[i-1];
        }
        arr[index] = element;
    }

    public static void main(String[] args) {
        Solution_2 sol = new Solution_2();
        int sizeOfArray = 6;
        int[] arr = new int[sizeOfArray];
        
        // Initializing the array with 5 elements (sizeOfArray - 1)
        arr[0] = 1;
        arr[1] = 2;
        arr[2] = 4;
        arr[3] = 5;
        arr[4] = 6;
        
        int index = 2;
        int element = 3;
        
        System.out.println("Original Array (first 5 elements): " + Arrays.toString(Arrays.copyOf(arr, sizeOfArray - 1)));
        
        sol.insertAtIndex(arr, sizeOfArray, index, element);
        
        System.out.println("Modified Array: " + Arrays.toString(arr));
    }
}
