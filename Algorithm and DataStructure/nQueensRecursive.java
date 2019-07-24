import java.util.Scanner;
public class nQueensRecursive {

	static int NN;		

	public static boolean isSafePositionQ(int[][] board, int row, int col){ 
			int i, j; 

            
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

	public static boolean solveNQforThisColumn( int board[ ][ ], int col ) {
		
		if( col >= NN )						// Stop a recursive call
			return true;

		for( int rowCnt = 0; rowCnt < NN; rowCnt++ ) {

		// found a position for queen and finish this column
		if( isSafePositionQ( board, rowCnt, col ) )	{
			board[ rowCnt ][ col ] = 1;	
	
			if ( solveNQforThisColumn( board, col + 1 ) )
				return true;
			
			board[ rowCnt ][ col ] = 0;
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
		//print error
		if( !solveNQforThisColumn ( board, 0 ) ) {
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