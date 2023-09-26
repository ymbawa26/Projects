/*
* File: Deck.java
* Author: Yazan Bawaqna
* Date: 09/12/2023
*/

import java.util.ArrayList;
import java.util.Random;

public class Deck {
    private ArrayList<Card> cards;

    /**
     * Creates the underlying deck as an ArrayList of Card objects. 
     * Calls build() as a subroutine to build the deck itself.
     */
    public Deck() {
      cards =  new ArrayList<Card>();
      build();
    }

    /**
     * Builds the underlying deck as a standard 52 card deck. 
     * Replaces any current deck stored. 
     */
    public void build() {
        cards.clear();
        for ( int i  = 2; i<= 9; i++){
            for (int j = 0; j < 4; j++) {
                cards.add(new Card(i));
            }
        }
    }

    /**
     * Returns the number of cards left in the deck. 
     * @return the number of cards left in the deck
     */
    public int size() {
        return cards.size();
        
    }

    /**
     * Returns and removes the first card of the deck.
     * @return the first card of the deck
     */
    public Card deal() {
        if (!cards.isEmpty()) {
            return cards.remove(0);

        } else {
            throw new IllegalStateException("The deck is empty");
        }
    }

    /**
     * Shuffles the cards currently in the deck. 
     */
    public void shuffle() {
        Random rand = new Random();
        for (int i = cards.size()-1; i>0; i--){
            int j = rand.nextInt(i + 1);
           // Swap the cards at indices i and j.
        Card temp = cards.get(i);
        cards.set(i, cards.get(j));
        cards.set(j, temp);
        }
    }

    /**
     * Returns a string representation of the deck.
     * @return a string representation of the deck
     */
    public String toString() {
    String result = "Deck";
    for (Card card: cards){
        result += card.toString() + "\n";
    }
    return result;

    }
}