/*The purpose of this class is to develop a main method to simulate the game of life "*/
public class LifeSimulation {
    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Usage: java LifeSimulation <gridSize> <numTimeSteps>");
            System.exit(1); // Exit the program with an error code
        }
              // Parse command line arguments to get gridSize and numTimeSteps
              int gridSize = Integer.parseInt(args[0]);
              int numTimeSteps = Integer.parseInt(args[1]);
      
              // Create a landscape with random initial conditions
              Landscape landscape = new Landscape(gridSize, gridSize, 0.2); // Adjust the initial chance as needed
      
              // Create a display to visualize the landscape
              LandscapeDisplay display = new LandscapeDisplay(landscape, 4);
                 // Visualize the initial board
               // Visualize the initial board
               display.repaint();
               try {
                   Thread.sleep(1000); // Pause for 1 second
                   //Source ChatGPT
               } catch (InterruptedException e) {
                   e.printStackTrace();
               }
            display.repaint(); // Update the display
        for (int t = 0; t < numTimeSteps; t++) {
            landscape.advance(); // Move the simulation forward by one time step
            display.repaint();  // Update the display
        }
        for (int t = 0; t < numTimeSteps; t++) {
            landscape.advance(); // Move the simulation forward by one time step
            display.repaint();  // Update the display
            try {
                Thread.sleep(250); // Pause for 250 milliseconds
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
}
}
