import	java.util.*;
public class Maze2 {

	private	static final int NN = 10;
	/*make a new stack for push/popping direction*/
	static Stack<Integer> stack2 = new Stack(); /*XXXX*/
	private static Stack stack = new Stack( );
	private static int exitRow = (NN - 1), exitCol = (NN - 1);
	private static boolean[ ][ ] hasVisited = new boolean[ NN ][ NN ];
	// boolean array is initialized to false by default
	
	public static void stackPush( int row, int col ) {
		int[ ] cod = { row, col };
		stack.push( cod );
		return;
	}
		 
	public static int[ ] stackPop( ) {
		
		int[ ] cod = ( int[ ] )stack.pop( );
		return cod;	
	}
	
	public static void checkFourDirections( int maze[ ][ ], int row, int col ) {
		/*erased crow and ccol and keep because not needed in iterative*/
		/*XXXX*/
		int dir = 0;
		/*initiate dir stack with 0*/
		stack2.push(dir);/*XXXX*/
		/*remake function with loops and switching some statement orders*/
		while(!(row == exitRow && col == exitCol )) {/*XXXX*/
			stackPush( row, col );
			hasVisited[ row ][ col ] = true;
     	  	while( dir >= 0 ) {   
			if( dir == 0 ) {			// north -- up
				if( ( row - 1 >= 0 ) && ( maze[ row - 1 ][ col ] == 1 ) && ( !hasVisited[ row - 1 ][ col ] ) ) {
				System.out.println( " up " );
				/*change the row or col itself then put valid direction in stack then reset to 0*/
					row = row - 1;			/*XXXX*/
					stack2.push(dir);		/*XXXX*/
					dir=0;					/*XXXX*/
					break;					/*XXXX*/
				}
			} else if( dir == 3 ) {		// west -- left
				if( ( col - 1 >= 0 ) && ( maze[ row ][ col - 1 ] == 1 ) && ( !hasVisited[ row ][ col - 1 ] ) ) {
				System.out.println( " left " );
					col = col - 1;			/*XXXX*/
					stack2.push(dir);		/*XXXX*/
					dir=0;					/*XXXX*/
					break;					/*XXXX*/
				}
			 } else if( dir ==  1 ) {		// east -- right
				if( ( col + 1 < NN ) && ( maze[ row ][ col + 1 ] == 1 ) && ( !hasVisited[ row ][ col + 1 ] ) ) {
				System.out.println( " right " );
					col = col + 1;			/*XXXX*/
					stack2.push(dir);		/*XXXX*/
					dir=0;					/*XXXX*/
					break;					/*XXXX*/
				}
			} else if( dir == 2 ) {		// south -- down
				if( ( row + 1 < NN ) && ( maze[ row + 1 ][ col ] == 1 ) && ( !hasVisited[ row + 1 ][ col ] ) ) {
				System.out.println( " down " );
					row = row + 1;			/*XXXX*/
					stack2.push(dir);		/*XXXX*/
					dir=0;					/*XXXX*/
					break;					/*XXXX*/
				}	
			} else {					// dir == 4?
				System.out.println( " NONE " + row + " | " + col );
				/*if there are dead ends return back to the valid row col and dir*/
				stackPop( );/*XXXX*/
				/*no solution if there are no candidates left in the stack, so end fu*/
				if (stack.empty())/*XXXX*/
					return;
				/*because the arrays in stack are call by references we need getters for the value*/
				/*take out the top values and put in rows and cols*/
				int cod[ ] = ( int[ ] )stack.get( stack.size( )-1 );/*XXXX*/
				row=cod[ 0 ];/*XXXX*/
				col=cod[ 1 ];/*XXXX*/
				/*also take out but no need for getters in just values*/
				dir=stack2.pop();/*XXXX*/
			}
			++dir;
		}//end of while dir
		
		// find an exit: success
		if( row == exitRow && col == exitCol ) {
			/*since we should not return back up to the function (unlike recursively)just add this statement for accurate printing*/
			stackPush( row, col );/*XXXX*/
			printSolution( );
			return; /*end function when we have solution(however due to system.exit() in printsolution, this won't do anything anyway*/
			}
		}
		return;	
	}

	public static void main(String[] args) {

        final int maze[ ][ ] = { 
        //	 0  1  2  3  4  5  6  7  8  9
        	{1, 0, 0, 0, 1, 0, 0, 0, 0, 1}, // 0
            {1, 1, 1, 0, 1, 1, 1, 1, 0, 0}, // 1
            {0, 1, 0, 1, 1, 0, 0, 1, 0, 1}, // 2
            {1, 1, 1, 1, 0, 1, 0, 1, 0, 0}, // 3
            {0, 0, 1, 0, 1, 0, 1, 1, 1, 1}, // 4
            {0, 1, 1, 0, 1, 1, 0, 0, 1, 0}, // 5
            {0, 1, 0, 1, 0, 0, 1, 1, 1, 0}, // 6
            {1, 1, 1, 0, 1, 0, 1, 1, 0, 0}, // 7
            {0, 0, 1, 0, 0, 1, 1, 1, 0, 1}, // 8
            {0, 0, 1, 1, 1, 1, 0, 1, 1, 1}, // 9
        }; 

		checkFourDirections( maze, 0, 0 );
        System.out.println( "No paths have been found" );
		return;
	}
			
	public static void printSolution(  ) {

		System.out.println( "\n\n ----------" );
		System.out.println( " success " );
		System.out.println( "----------\n\n" );

		for( int idx = 0; idx < stack.size( ); idx++ ) {
			int cod[ ] = ( int[ ] )stack.get( idx );
			System.out.println( "[ " + cod[ 0 ] + " ][ " + cod[ 1 ] + " ] ==> " );
        }
		System.exit( 0 );
    }
}
