/*
file name:      LandscapeTests.java
Authors:        Max Bender & Naser Al Madi
last modified:  9/18/2022

How to run:     java -ea LandscapeTests
*/


import java.util.ArrayList;
/* The purpose of this class is to test the landscape class */

public class LandscapeTests {

    public static void landscapeTests() {

        // case 1: testing Landscape(int, int)
        
            // set up
            Landscape l1 = new Landscape(2, 4);
            Landscape l2 = new Landscape(10, 10);

            // verify
            System.out.println(l1);
            System.out.println("\n");
            System.out.println(l2);

            // test
            assert l1 != null : "Error in Landscape::Landscape(int, int)";
            assert l2 != null : "Error in Landscape::Landscape(int, int)";
        

        // case 2: testing reset()
        
                 // set up
                 Landscape l3 = new Landscape(3, 3);
                 l3.reset();
     
                 // verify
                 System.out.println("\nTest Case 2:");
                 System.out.println("Landscape l3 after reset:");
                 System.out.println(l3);
     
                 // test
                 assert true;
             
        
            
        

        // case 3: testing getRows()
        
            Landscape l4 = new Landscape(5, 5);
            l4.getRows();


            // verify
            System.out.println("Test Case 3:");
            System.out.println("Number of rows in l4: " + l4.getRows());


            // test
            assert l4.getRows() == 5: "Error in Landscape::getRows()";
        

        // case 4: testing getCols()
        
            Landscape l5 = new Landscape(5, 5);
            l5.getRows();


            // verify
            System.out.println("Test Case 4:");
            System.out.println("Number of rows in l4: " + l4.getCols());


            // test
            assert l4.getCols() == 5: "Error in Landscape::getRows()";

        // case 5: testing getCell(int, int)
            // set up
            Landscape l6 = new Landscape(3, 3);

            // verify
            System.out.println("\nTest Case 5:");
            System.out.println("Cell at (2, 2) in l6: " + l6.getCell(2, 2));

            // test
            assert l6.getCell(2, 2) != null : "Error in Landscape::getCell(int, int)";

        // case 6: testing getNeighbors()


        Landscape l7 = new Landscape(3, 3);

        // verify
        System.out.println("\nTest Case 6:");
        System.out.println("Neighbors of cell at (1, 1) in l7:");
        ArrayList<Cell> neighbors = l7.getNeighbors(1, 1);
        for (Cell neighbor : neighbors) {
            System.out.println(neighbor);
        }

        // test
        assert neighbors.size() == 8 : "Error in Landscape::getNeighbors(int, int)";

        // case 7: testing advance()
        
      
        Landscape l8 = new Landscape(4,4);
          l8.advance();
        System.out.println("\nTest Case 7:");
        System.out.println("Landscape l8 after advancing:");
        System.out.println(l8);

        

    }


    public static void main(String[] args) {

        landscapeTests();
    }
}