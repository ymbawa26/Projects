import java.util.ArrayList;


/*The purpose of this class is to develop the cell objects and their methods */
public class Cell {

    /**
     * The status of the Cell.
     */
    private boolean alive;

    /**
     * Constructs a dead cell.
     */
    public Cell(){
    this.alive = false; //Default to dead
    }
    // Constructs a cell with the specified status.
       public Cell(boolean alive) {
        this.alive = alive;
}
   // Returns whether the cell is currently alive.
   public boolean getAlive() {
    return alive;
}

   // Sets the current status of the cell to the specified status.
   public void setAlive(boolean status) {
   this.alive = status; }

   public void updateState(ArrayList<Cell> neighbors) {
    int aliveNeighbors = 0;
    for (Cell neighbor: neighbors ){if (neighbor.getAlive()) {aliveNeighbors++;}
   }
        // Apply Conway's Game of Life rules
          if (alive) {
         // Cell is currently alive
            if (aliveNeighbors != 2 && aliveNeighbors != 3) {
            // Less than 2 or more than 3 neighbors are alive, cell dies
                setAlive(false);
            }
        } else {
            // Cell is currently dead
            if (aliveNeighbors >= 3) {
                // Exactly 3 neighbors are alive, cell comes back to life
                setAlive(true);
            }
        }
    }
    /**
     * Returns a String representation of this Cell.
     * 
     * @return 1 if this Cell is alive, otherwise 0.
     */
    public String toString() {
        return alive ? "1" : "0";
    }
    /** 
     * Updates the state of the Cell based on its neighbors.
    * 
    * If this Cell is alive and if there are 2 or 3 alive neighbors,
    * this Cell stays alive. Otherwise, it dies.
    * 
    * If this Cell is dead and there are 3 alive neighbors,
    * this Cell comes back to life. Otherwise, it stays dead.
    * 
    * @param neighbors An ArrayList of Cells representing the neighbors of this Cell
    */

    
    //main function to test the code
    public static void main(String[] args) {
        // Create a Cell object with default (dead) state
        Cell deadCell = new Cell();
        System.out.println("Is the cell alive? " + deadCell.getAlive()); // Should print "false"
    
        // Create a Cell object with alive state
        Cell aliveCell = new Cell(true);
        System.out.println("Is the cell alive? " + aliveCell.getAlive()); // Should print "true"
    
        // Set the state of the dead cell to alive
        deadCell.setAlive(true);
        System.out.println("Is the cell alive? " + deadCell.getAlive()); // Should print "true"
    
        // Set the state of the alive cell to dead
        aliveCell.setAlive(false);
        System.out.println("Is the cell alive? " + aliveCell.getAlive()); // Should print "false"
    
        // Test the toString method
        System.out.println("Dead cell as string: " + deadCell.toString()); // Should print "0"
        System.out.println("Alive cell as string: " + aliveCell.toString()); // Should print "1"
    }
}