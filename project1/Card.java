public class Card {

    /**
     * The value of the card.
     */
    private int value;

    /**
     * Constructs a card with the specified value.
     * @param val
     */
    public Card(int val) {
        //To check if the value is between 2 and 11
        if (val >= 1 && val<=11){
            this.value = val;
        } else {
            throw new IllegalArgumentException("Invalid card value. Must be between 1 and 11.");
        }
        
    }

    /**
     * Returns the value of the card.
     * @return the value of the card
     */
    public int getValue() {
        return value;
    }
    
    /**
     * Returns a string representation of this card.
     * @return a string representation of this card
     */
    public String toString() {
        if (value == 1){
            return "Ace ";
    } else {return String.valueOf(value);}
}
}