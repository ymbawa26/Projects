import java.awt.Color;
import java.awt.Graphics;
import java.util.ArrayList;

/* The purpose of this class is to develop a grid for the cells with methods for the game of life */
public class Landscape {

    /**
     * The underlying grid of Cells for Conway's Game
     */
    private Cell[][] landscape;

    /**
     * The original probability each individual Cell is alive
     */
    private double initialChance;

    /**
     * Constructs a Landscape of the specified number of rows and columns.
     * All Cells are initially dead.
     * 
     * @param rows    the number of rows in the Landscape
     * @param columns the number of columns in the Landscape
     */
    public Landscape(int rows, int columns) {
        landscape = new Cell[rows][columns];
        reset();
    }

    /**
     * Constructs a Landscape of the specified number of rows and columns.
     * Each Cell is initially alive with probability specified by chance.
     * 
     * @param rows    the number of rows in the Landscape
     * @param columns the number of columns in the Landscape
     * @param chance  the probability each individual Cell is initially alive
     */
    public Landscape(int rows, int columns, double chance) {
        landscape = new Cell[rows][columns];
        initialChance = chance;
        reset();
    }

    /**
     * Recreates the Landscape according to the specifications given
     * in its initial construction.
     */
    public void reset() {
        for (int row = 0; row < landscape.length; row ++){
            for ( int col = 0; col < landscape[row].length; col ++){ landscape[row][col] = new Cell(Math.random() <initialChance);

            }
        }
    }

    /**
     * Returns the number of rows in the Landscape.
     * 
     * @return the number of rows in the Landscape
     */
    public int getRows() {
        return landscape.length;
    }

    /**
     * Returns the number of columns in the Landscape.
     * 
     * @return the number of columns in the Landscape
     */
    public int getCols() {
        return landscape[0].length;
    }

    /**
     * Returns the Cell specified the given row and column.
     * 
     * @param row the row of the desired Cell
     * @param col the column of the desired Cell
     * @return the Cell specified the given row and column
     */
    public Cell getCell(int row, int col) {
        return landscape[row][col];
    }

    /**
     * Returns a String representation of the Landscape.
     */
    public String toString() {
        //Creating a string builder object since strings are immutable
        StringBuilder sbuilder = new StringBuilder();
        for (int row = 0; row < getRows(); row++) {
            for (int col = 0; col < getCols(); col++) {
                sbuilder.append(landscape[row][col].toString()); 
            }
            sbuilder.append('\n');
        }
        return sbuilder.toString();
    }

    /**
     * Returns an ArrayList of the neighboring Cells to the specified location.
     * 
     * @param row the row of the specified Cell
     * @param col the column of the specified Cell
     * @return an ArrayList of the neighboring Cells to the specified location
     */
    public ArrayList<Cell> getNeighbors(int row, int col) {
        ArrayList<Cell> neighbors = new ArrayList<>();

    // Define the bounds of the grid
    int numRows = getRows();
    int numCols = getCols();
    
        for (int r = row-1; r<row+2; r++){
            for (int c = col-1; c<col+2 ;c++){

            if (r >= 0 && r < numRows && c >= 0 && c < numCols && !(r == row && c == col)) {
                neighbors.add(getCell(r, c));
        }
        }
    }
    return neighbors;
    }

    /**
     * Advances the current Landscape by one step. 
     */
    public void advance() {

        //Create a copy of the current lanscape to store the next state
        int numRows = getRows();
        int numCols = getCols();
    
        Cell[][] nextLandscape = new Cell[numRows][numCols];
    
        // Loop through each cell in the landscape
        for (int row = 0; row < numRows; row++) {
            for (int col = 0; col < numCols; col++) {
                Cell currentCell = getCell(row, col);
                ArrayList<Cell> neighbors = getNeighbors(row, col);
    
                int aliveNeighbors = 0;
                for (Cell neighbor : neighbors) {
                    if (neighbor.getAlive()) {
                        aliveNeighbors++;
                    }
                }
    
                // Apply Conway's Game of Life rules
                if (currentCell.getAlive()) {
                    // Any live cell with fewer than two live neighbors dies (underpopulation)
                    // Any live cell with two or three live neighbors lives on to the next generation
                    // Any live cell with more than three live neighbors dies (overpopulation)
                    if (aliveNeighbors < 2 || aliveNeighbors > 3) {
                        nextLandscape[row][col] = new Cell(false); // Cell dies
                    } else {
                        nextLandscape[row][col] = new Cell(true);  // Cell survives
                    }
                } else {
                    // Any dead cell with exactly three live neighbors becomes a live cell
                    if (aliveNeighbors == 3) {
                        nextLandscape[row][col] = new Cell(true);  // Cell becomes alive
                    } else {
                        nextLandscape[row][col] = new Cell(false); // Cell remains dead
                    }
                }
            }
        }
    
        // Update the landscape to the next state
        landscape = nextLandscape; }
    /**
     * Draws the Cell to the given Graphics object at the specified scale.
     * An alive Cell is drawn with a black color; a dead Cell is drawn gray.
     * 
     * @param g     the Graphics object on which to draw
     * @param scale the scale of the representation of this Cell
     */
    public void draw(Graphics g, int scale) {
        for (int x = 0; x < getRows(); x++) {
            for (int y = 0; y < getCols(); y++) {
                g.setColor(getCell(x, y).getAlive() ? Color.green : Color.gray);
                g.fillOval(x * scale, y * scale, scale, scale);
            }
        }
    }

    public static void main(String[] args) {
    }
}
