/*
* File: Blackjack.java
* Author: Yazan Bawaqna
* Date: 09/12/2023
*/


import java.util.Random;
import java.util.Scanner;

public class Blackjack {
    private Deck deck = new Deck();
    private Hand playerHand; 
    private Hand dealerHand;
    private int reshuffleCutoff;
    private int playerMoney; // Player's initial money
    private int playerBet;   // Player's current bet


    public Blackjack(int reshuffleCutoff, int initialMoney) {
        this.reshuffleCutoff = reshuffleCutoff;
        this.playerMoney = initialMoney; // Initialize player's money
        reset();
    } 
    public Blackjack() {
    this(30, 100); // Defaults to reshuffle cutoff of 30 and $100 initial money
    }

    public void reset(){
        // Create new hands for the player and dealer
        playerHand = new Hand();
        dealerHand = new Hand();
        playerBet = 0; //Reset the player's bet
        // Check if the deck is null or if the number of cards in the deck is less than the reshuffle cutoff
        if (deck == null || deck.size()< reshuffleCutoff){
        deck = new Deck();
        deck.shuffle();
        }
    }
    
    public void deal(){
        //create a card and add it to the deck arrayList
        playerHand.add(deck.deal());
        dealerHand.add(deck.deal());
        playerHand.add(deck.deal());
        dealerHand.add(deck.deal());
    }
    public boolean playerTurn(){
        //As long as the total value in his hand is less than 16, excute
        while (playerHand.getTotalValue() < 16) {
            //retrive ane remove the top card from the deck
            Card card = deck.deal();
            if (card == null) {
                return false; // Deck is empty
            }
            playerHand.add(card);
        }
        //the method returns true if the player's hand total value is less than or equal to 21, indicating that the player did not bust
        return playerHand.getTotalValue() <= 21;
    }
    public boolean dealerTurn(){
        //As long as the total value in his hand is less than 16, excute
        while (dealerHand.getTotalValue() < 16) {
            //retrive ane remove the top card from the deck
            Card card = deck.deal();
            if (card == null) {
                return false; // Deck is empty
            }
            dealerHand.add(card);
        }
        //the method returns true if the player's hand total value is less than or equal to 21, indicating that the player did not bust
        return dealerHand.getTotalValue() <= 21; }

        //assign the new cutoff value to the internal reshuffle cutoff field
        public void setReshuffleCutoff(int cutoff) {
            reshuffleCutoff = cutoff;
        }
    
        //returns the current value of the reshuffle cutoff field.
        public int getReshuffleCutoff() {
            return reshuffleCutoff;
        }
        //returns the playerhand and the dealerhand as a string, alongside the total value inisde their hands.
        public String toString() {
            return "Player's Hand: " + playerHand + " (Total: " + playerHand.getTotalValue() + ")\n" +
                   "Dealer's Hand: " + dealerHand + " (Total: " + dealerHand.getTotalValue() + ")";
        }
        //Creates a method to play a single game.
        public int game(boolean verbose) {
            // Reset the game state
            reset();
        
            // Deal two initial cards to both player and dealer
            deal();
            
            // Player's turn
            boolean playerBusted = !playerTurn();
        
            // Dealer's turn (if player didn't bust)
            boolean dealerBusted = false;
            if (!playerBusted) {
                dealerBusted = !dealerTurn();
            }
        
            // Determine the game result
            if (playerBusted || (dealerBusted && !playerBusted)) {
                if (verbose) {
                    System.out.println("Player's hand: " + playerHand);
                    System.out.println("Dealer's hand: " + dealerHand);
                    System.out.println("Dealer wins!");
                }
                return -1; // Dealer wins
            } else if (dealerBusted || playerHand.getTotalValue() > dealerHand.getTotalValue()) {
                if (verbose) {
                    System.out.println("Player's hand: " + playerHand);
                    System.out.println("Dealer's hand: " + dealerHand);
                    System.out.println("Player wins!");
                }
                return 1; // Player wins
            
            } else if (playerHand.getTotalValue() == dealerHand.getTotalValue()) { //Incase of a tie
                if (verbose) {
                    System.out.println("Player's hand: " + playerHand);
                    System.out.println("Dealer's hand: " + dealerHand);
                    System.out.println("Push (Tie)!");
                }
                return 0; // Push (Tie)
            } else {
                // This should not happen in a properly implemented game
                return 0; // Default to tie in case of an error
            }
        }
        public void placeBet(int bet) {
            if (bet > 0 && bet <= playerMoney) {
                playerBet = bet;
            } else {
                System.out.println("Invalid bet. Please place a valid bet.");
            }
        }
        public int getPlayerMoney() {
            return playerMoney;
        }

  public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);  //The player inputs his current total money
        System.out.print("Enter your initial money: ");
        int initialMoney = scanner.nextInt();
        //creating a bBlackjack game object
        Blackjack blackjack = new Blackjack(30, initialMoney);
        
        int playerWins = 0;
        int dealerWins = 0;
        int ties = 0;
        int numGames = 3; // Number of games to play
    
    

        //iterating over the games and recording the results
        for (int i = 0; i < numGames; i++) {

            System.out.println("Game " + (i + 1));
            System.out.print("Place your bet: ");
            int bet = scanner.nextInt();

            blackjack.placeBet(bet);
            int result = blackjack.game(false); // Run the game without printing details
            if (result == 1) {
                playerWins++;
            } else if (result == -1) {
                dealerWins++;
            } else {
                ties++;
            }
            System.out.println("Player's current money: $" + blackjack.getPlayerMoney());
            System.out.println("----------------------------");
        }
                // Print out the results
                System.out.println("Player wins: " + playerWins);
                System.out.println("Dealer wins: " + dealerWins);
                System.out.println("Ties: " + ties);
                scanner.close();     
  }}

    