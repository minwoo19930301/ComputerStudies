//among arraylist savor, find the one with the minimum stacksize


package d;
import	java.util.*;

public class Maze3 {

	private	static final int NN = 10;
	private	static final int CC = 2;
	private static Stack stack = new Stack( );
	private static int exitRow = (NN - 1), exitCol = (NN - 1);
	private static boolean[ ][ ] hasVisited = new boolean[ NN ][ NN ];
	// boolean array is initialized to false by default
	//save the trues in an arraylist if already in the list try again
	static ArrayList saver;				/* XXXX*/
	
	public static void stackPush( int [ ] cod ) {
		stack.push( cod );
		System.out.println( "stackPush: [ " + stack.size( ) + " ][ " + cod[ 0 ] + " ][ " + cod[ 1 ] + " ]" );
		return;
	}
		 
	public static int[ ] stackPop( ) {
		
		int[ ] cod = ( int[ ] )stack.pop( );
		System.out.println( "stackPop: [ " + cod[ 0 ] + " ][ " + cod[ 1 ] + " ]" );
		return cod;	
	}
	
	public static void checkFourDirections( int maze[ ][ ], int coord[ ] ) {

		int row = coord[ 0 ];
		int col = coord[ 1 ];
		int dir = 0;

		hasVisited[ row ][ col ] = true;

		stackPush( coord );
		// find an exit: success
		if( row == exitRow && col == exitCol ) {
			printSolution( );
		}

		while( dir >= 0 ) {

			boolean keep = false;
//			System.out.println( " Current row [ " + row + " ] col [ " + col + " ][ " + dir + " ]");
			if( dir == 0 ) {			// north -- up
				if( ( row - 1 >= 0 ) && ( maze[ row - 1 ][ col ] == 1 ) && ( !hasVisited[ row - 1 ][ col ] ) ) {
					coord[ 0 ] = row - 1;
					coord[ 1 ] = col;
					keep = true;
				}
			} else if( dir == 3 ) {		// west -- left
				if( ( col - 1 >= 0 ) && ( maze[ row ][ col - 1 ] == 1 ) && ( !hasVisited[ row ][ col - 1 ] ) ) {
					coord[ 0 ] = row;
					coord[ 1 ] = col - 1;
					keep = true;
				}
			} else if( dir == 1 ) {		// east -- right
				if( ( col + 1 < NN ) && ( maze[ row ][ col + 1 ] == 1 ) && ( !hasVisited[ row ][ col + 1 ] ) ) {
					coord[ 0 ] = row;
					coord[ 1 ] = col + 1;
					keep = true;
				}
			} else if( dir == 2 ) {		// south -- down
				if( ( row + 1 < NN ) && ( maze[ row + 1 ][ col ] == 1 ) && ( !hasVisited[ row + 1 ][ col ] ) ) {
					coord[ 0 ] = row + 1;
					coord[ 1 ] = col;
					keep = true;
				}
			} else {					// dir == 4?
				stackPop( );
				break;
			}
			++dir;
			if (keep) {
				checkFourDirections( maze, coord );
			}
		}
		return;
	}

	public static void main(String[] args) {

 		int maze[][] = { 
 		//	 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
 			{1, 0, 0, 0, 1, 0, 0, 0, 0, 1}, // 0
 			{1, 1, 1, 0, 1, 1, 1, 1, 0, 0}, // 1
 			{0, 1, 0, 1, 1, 0, 0, 1, 0, 1}, // 2
 			{1, 1, 1, 1, 0, 1, 0, 1, 0, 0}, // 3
 			{0, 0, 1, 0, 1, 0, 1, 1, 1, 1}, // 4
 			{0, 1, 1, 0, 1, 1, 0, 0, 1, 0}, // 5
 			{0, 1, 0, 1, 0, 0, 1, 1, 1, 0}, // 6
 			{1, 1, 1, 1, 1, 0, 1, 1, 0, 0}, // 7
 			{0, 0, 1, 0, 0, 1, 0, 1, 0, 1}, // 8
 			{0, 0, 1, 1, 1, 1, 1, 1, 1, 1}, // 9
 	}; 

		int[ ] coord = new int[ CC ];
		try {
			checkFourDirections( maze, coord );
		}
		except{In /****/ // try other cases, 
		}
 		System.out.println( "No paths have been found" );
		return;
	}
			
	public static void printSolution(  ) {

		System.out.println( "\n\n----------" );
		System.out.println( " success " );
		System.out.println( "----------\n\n" );

		for( int idx = 0; idx < stack.size( ); idx++ ) {
			int cod[ ] = ( int[ ] )stack.get( idx );
			System.out.println( "[ " + cod[ 0 ] + " ][ " + cod[ 1 ] + " ] ==> " );
			saver.add(cod[0]);				/*XXXX*/
			saver.add(cod[1]);				/*XXXX*/
  	}
	
		System.exit( 0 );
    }
}
