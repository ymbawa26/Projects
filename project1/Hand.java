/*
* File: Hand.java
* Author: Yazan Bawaqna
* Date: 09/12/2023
*/

import java.util.ArrayList;

public class Hand {

    /**
     * Creates an empty hand as an ArrayList of Cards.
     */
    private ArrayList<Card> cards;
    public Hand(){
        cards = new ArrayList<Card>();
    }

    /**
     * Removes any cards currently in the hand. 
     */
    public void reset(){
        cards.clear();
    }

    /**
     * Adds the specified card to the hand.
     * @param card the card to be added to the hand
     */
    public void add(Card card){
        cards.add(card);
    }

    /**
     * Returns the number of cards in the hand.
     * @return the number of cards in the hand
     */
    public int size(){
        return cards.size();
    }

    /**
     * Returns the card in the hand specified by the given index. 
     * @param index the index of the card in the hand.
     * @return the card in the hand at the specified index.
     */
    public Card getCard(int index){
        if (index >= 0 && index > cards.size()){
            return cards.get(index );
         } else {
                throw new IllegalArgumentException ("Invalid index");
            }
        }

    /**
     * Returns the summed value over all cards in the hand.
     * @return the summed value over all cards in the hand
     */
    public int getTotalValue(){
        int totalValue = 0;
        for (Card card: cards){
            totalValue += card.getValue();
        }
        return totalValue;
    }

    /**
     * Returns a string representation of the hand.
     * @return a string representation of the hand
     */
    public String toString(){
        StringBuilder sb = new StringBuilder("[");
        for (int i =0; i<cards.size(); i++){
            sb.append(cards.get(i));
            if (i < cards.size() - 1) {
                sb.append(", ");
            }
        }
        sb.append("] : ").append(getTotalValue());
        return sb.toString();
    }
}
