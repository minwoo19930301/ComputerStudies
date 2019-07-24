import java.util.Scanner;
import java.util.Stack;
public class nQueensIterative{

	static int NN;		
	static Stack<Integer> stack = new Stack<Integer>( );  //recursive = iterative + stack

	public static boolean isSafePositionQ(int[][] board, int row, int col){ 
			int i, j; 
	        if (row>=NN || col>=NN)
            		return false;	
            
			// Check each column
			for (j = 0; j < NN; j++) 
				if (board[row][j] == 1) 
					return false; 
	  
			// Check diagonal  
			for (i=row, j=col; i>=0 && j>=0; i--, j--) 
				if (board[i][j] == 1) 
					return false; 
	  
			// Check diagonal 
			for (i=row, j=col; j>=0 && i<NN; i++, j--) 
				if (board[i][j] == 1) 
                    return false; 
                    
            //check diagonal
            for (i=row, j=col; i<NN && j<NN; i++, j++) 
				if (board[i][j] == 1) 
					return false; 

            //check diagonal
            for (i=row, j=col; i>=0 && j<NN; i--, j++) 
				if (board[i][j] == 1) 
                    return false;
             
	  
			return true; 
		} 

	public static boolean solveNQforThisColumn( int board[ ][ ]) {
		int col=0;
		int row=0;
		while( col < NN ) {
        	//if safe position make it a candidate by pushing row in stack
			if( isSafePositionQ( board, row, col ) )	{
				board[row][col]=1;
				stack.push(row);
				col=col+1;
				//if col==3 is Safe then succeeded, thus finish
				if (col==NN){
					return true;
				}
				row=-1;
			}
			row=row+1;
			//backtracking : go back to candidate, unmark it then continue 
    	    if ( row>=NN ) {	
				row=stack.pop();
				col=col-1;
				board[row][col]=0;
              	row=row+1;		// in order not to crash into same candidate
			}			

		}
		return false;
}
    public static void main( String args[ ] ) {
		System.out.println("Type a number for how many queens and how many rows & columns in a board: ");
        Scanner sc = new Scanner(System.in);
        NN=sc.nextInt();
		sc.close();
		//make board
        int[][] board = new int[NN][NN];
        for (int i=0;i<NN;i++){
            for (int j=0;j<NN;j++){
                board[i][j]=0;
            }
        }
		//print error if not able
		if( !solveNQforThisColumn ( board) ) {
			System.out.print( "Cannot solve the puzzle" );	
			return;
		}
      	//else
		System.out.println();
		printSolution( board );
		return;
	}

	/* A utility function to print solution */
	public static void printSolution( int board[][] ) {
		for ( int row = 0; row < NN; row ++ ) { 
			for ( int col = 0; col < NN; col ++ ) 
				System.out.print( " " + board[ row ][ col ] + " " ); 
            System.out.println( ); 
        }
    }
}