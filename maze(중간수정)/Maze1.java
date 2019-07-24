/*understood making BFS using stacks but couldn't 
create saving paths and unmark hasVisited for slower paths*/

import	java.util.*;
public class Maze1 {

	private	static final int NN = 10;
    private static Stack stack = new Stack( );
    /*using queues for BFS backtracking*/
	static Queue<Integer> queueRow = new LinkedList<>(); /****/
	static Queue<Integer> queueCol = new LinkedList<>(); /****/
	private static int exitRow = (NN - 1), exitCol = (NN - 1);
	private static boolean[ ][ ] hasVisited = new boolean[ NN ][ NN ];
	// boolean array is initialized to false by default
	
	public static void stackPush( int row, int col ) {
		int[ ] cod = { row, col };
		stack.push( cod );
//		System.out.println( "stackPush: [ " + stack.size( ) + " ] : [ " + cod[ 0 ] + " ][ " + cod[ 1 ] + " ]" );
		return;
	}
	
	
	public static int[ ] stackPop( ) {
		
		int[ ] cod = ( int[ ] )stack.pop( );
//		System.out.println( "stackPop: [ " + stack.size( ) + " ] : [ " + cod[ 0 ] + " ][ " + cod[ 1 ] + " ]" );
		return cod;	
	}
	
	public static void checkFourDirections( int maze[ ][ ], int row, int col ) {
        /*dequeue the head*/
        row=queueRow.remove();	/****/	
		col=queueCol.remove();	/****/
		int crow = row;
		int ccol = col;
		int dir = 0;
		
        stackPush(row, col);
		if( row == exitRow && col == exitCol ) {
			printSolution( );
	        return;
		}
		hasVisited[ row ][ col ] = true;
		boolean keep = false;
		while( dir >= 0 ) {
			
//			System.out.println( " Current row [ " + row + " ] col [ " + col + " ] dir [ " + dir + " ]");
			if( dir == 0 ) {			// north -- up
				if( ( row - 1 >= 0 ) && ( maze[ row - 1 ][ col ] == 1 ) && ( !hasVisited[ row - 1 ][ col ] ) ) {
				System.out.println( " up " );
					crow = row - 1;
                    ccol=col;
                    /*add candidates to queue*/
					queueRow.offer(crow);	/****/	
					queueCol.offer(ccol);	/****/
					keep=true;
		
				}
			} else if( dir == 3 ) {		// west -- left
				if( ( col - 1 >= 0 ) && ( maze[ row ][ col - 1 ] == 1 ) && ( !hasVisited[ row ][ col - 1 ] ) ) {
				System.out.println( " left " );
					ccol = col - 1;
					crow=row;
					queueRow.offer(crow);	/****/	
					queueCol.offer(ccol);	/****/
					keep=true;
		
				}
			} else if( dir == 1 ) {		// east -- right
				if( ( col + 1 < NN ) && ( maze[ row ][ col + 1 ] == 1 ) && ( !hasVisited[ row ][ col + 1 ] ) ) {
				System.out.println( " right " );
					ccol = col + 1;
					crow=row;
					queueRow.offer(crow);	/****/	
					queueCol.offer(ccol);	/****/
					keep=true;
		
				}
			} else if( dir == 2 ) {		// south -- down
				if( ( row + 1 < NN ) && ( maze[ row + 1 ][ col ] == 1 ) && ( !hasVisited[ row + 1 ][ col ] ) ) {
				System.out.println( " down " );
					crow = row + 1;
					ccol=col;
					queueRow.offer(crow);	/****/	
					queueCol.offer(ccol);	/****/
					keep=true;
				}
            } else {					// dir == 4?
                /*return by trying the other candidate*/
				System.out.println( " NONE " + row + " | " + col );
				stackPop();/****/
				crow=queueRow.peek();/****/
				ccol=queueCol.peek();/****/
				keep=false;/****/
				checkFourDirections( maze, crow, ccol );/****/
			}
            ++dir;
            /*BFS needs to check all directions*/ 
			if ((keep)&&(dir==4)){ /****/
				crow=queueRow.peek();/****/
				ccol=queueCol.peek();/****/
				keep=false;/****/
				checkFourDirections( maze, crow, ccol );/****/
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
        /*initiate queues with the start point*/
		queueRow.offer(0); /****/
		queueCol.offer(0); /****/
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

        System.exit(0);
		}
    
}

/**

//attempt to print all solutions but failed
//tried to store candidates nodes that have more
//than one path and recursively call with queues

import	java.util.*;
public class Maze3 {

	private	static final int NN = 10;
	private static Stack stack = new Stack( );
	//a queue for BFS backtracking and another for candidates that have more than one path
	static Queue<Integer> queueRow = new LinkedList<>(); ////
	static Queue<Integer> queueCol = new LinkedList<>(); ////
	static Queue<Integer> candidRow = new LinkedList<>(); ////
	static Queue<Integer> candidCol = new LinkedList<>(); ////
	private static int exitRow = (NN - 1), exitCol = (NN - 1);
	private static boolean[ ][ ] hasVisited = new boolean[ NN ][ NN ];
	// boolean array is initialized to false by default
	
	public static void stackPush( int row, int col ) {
		int[ ] cod = { row, col };
		stack.push( cod );
//		System.out.println( "stackPush: [ " + stack.size( ) + " ] : [ " + cod[ 0 ] + " ][ " + cod[ 1 ] + " ]" );
		return;
	}
	
	
	public static int[ ] stackPop( ) {
		
		int[ ] cod = ( int[ ] )stack.pop( );
//		System.out.println( "stackPop: [ " + stack.size( ) + " ] : [ " + cod[ 0 ] + " ][ " + cod[ 1 ] + " ]" );
		return cod;	
	}
	
	public static void checkFourDirections( int maze[ ][ ], int row, int col ) {
		System.out.println(row +" check  " +col);
		//initiate path counter and dequeue head of queue
		int pathInNode=0;	////
		row=queueRow.remove();		////	
		col=queueCol.remove();	////
		int crow = row;
		int ccol = col;
		int dir = 0;
		
        stackPush(row, col);
		if( row == exitRow && col == exitCol ) {
			printSolution( );
			//make all board nodes not visited and start from another candidate node
			for (int i=0;i<NN;i++)	
                for(int j=0; j<NN; j++)
                    hasVisited[i][j]=false;
            row=candidRow.remove();		
            col=candidCol.remove();	
            checkFourDirections(maze, row, col);
            return;
		}
		hasVisited[ row ][ col ] = true;
		boolean keep = false;
		while( dir >= 0 ) {
			
//			System.out.println( " Current row [ " + row + " ] col [ " + col + " ] dir [ " + dir + " ]");
			if( dir == 0 ) {			// north -- up
				if( ( row - 1 >= 0 ) && ( maze[ row - 1 ][ col ] == 1 ) && ( !hasVisited[ row - 1 ][ col ] ) ) {
				System.out.println( " up " );
					crow = row - 1;
					ccol=col;
					//enqueue the valid path
					queueRow.offer(crow);		
					queueCol.offer(ccol);	
					keep=true;
					pathInNode++;
		
				}
			} else if( dir == 3 ) {		// west -- left
				if( ( col - 1 >= 0 ) && ( maze[ row ][ col - 1 ] == 1 ) && ( !hasVisited[ row ][ col - 1 ] ) ) {
				System.out.println( " left " );
					ccol = col - 1;
					crow=row;
					queueRow.offer(crow);	
					queueCol.offer(ccol);	
					keep=true;
					pathInNode++;
		
				}
			} else if( dir == 1 ) {		// east -- right
				if( ( col + 1 < NN ) && ( maze[ row ][ col + 1 ] == 1 ) && ( !hasVisited[ row ][ col + 1 ] ) ) {
				System.out.println( " right " );
					ccol = col + 1;
					crow=row;
					queueRow.offer(crow);		
					queueCol.offer(ccol);	
					keep=true;
					pathInNode++;
		
				}
			} else if( dir == 2 ) {		// south -- down
				if( ( row + 1 < NN ) && ( maze[ row + 1 ][ col ] == 1 ) && ( !hasVisited[ row + 1 ][ col ] ) ) {
				System.out.println( " down " );
					crow = row + 1;
					ccol=col;
					queueRow.offer(crow);		
					queueCol.offer(ccol);	
					keep=true;
					pathInNode++;
		
				}
			} else {					// dir == 4?
				System.out.println( " NONE " + row + " | " + col );
				stackPop();
				crow=queueRow.peek();
				ccol=queueCol.peek();
				keep=false;
				checkFourDirections( maze, crow, ccol );
			}
			++dir;
			//when more than one path, save in another queue
			if (pathInNode>1){
				for (int i=0; i<queueRow.size();i++){
					int a = queueRow.peek();
					int b = queueCol.peek();
					candidRow.offer(queueRow.remove());
					candidCol.offer(queueCol.remove());
					queueRow.offer(a);
					queueCol.offer(b);			
			}
		}
			if ((keep)&&(dir==4)){ 
				crow=queueRow.peek();
				ccol=queueCol.peek();
				keep=false;
				checkFourDirections( maze, crow, ccol );
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
		queueRow.offer(0); 
		queueCol.offer(0); 
		checkFourDirections( maze, 0, 0 );
        System.out.println( "No paths have been found" );
		return;
	}
			
	public static void printSolution(  ) {

		System.out.println( "\n\n ----------" );
		System.out.println( " success " );
		System.out.println( "----------\n\n" );
		}
	//since all paths printed needed, erase the System.exit(0);
    
}


**/
