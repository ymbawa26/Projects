"""
Yazan Bawaqna
Cs 152 B
project08
Novemeber 11th 2022

"""

def main():
    """ this function creates a simply dictionary, run the function from the terminal and input some capitals names """
    #Print out a prompt for the user that tells them what to do.
    print("Please enter the capital of the following countries")
    #Create a list of about ten words, call it words.   
    words = ["Palestine ", "Jordan ", "Syria ", "Lebanon ", "Iraq ", "Egypt ", "Libya ", "Saudi_Arabia ", "Qatar ","Bahrain ", "Yemen " ]
    #Create an empty dictionary, called mapping ={}.
    mapping= {}
    #Loop over the  words list.
    for word in words:
        # First, assign a response the return value of input, using the word as the argument to input
        response = input(word)
        #Second, using the word as the key for the empty dictionary mapping, assign to your dictionary the response (the output from input)
        mapping[ word ] = response
        #Finally, loop over the keys in mapping (for key in mapping.keys()) and print out the key/response pairs using the dictionary .get(key) method to show the user their results.	
        for key in mapping.keys():
            print(key + "=" + mapping.get(key))

main()    
           
            
            
                
                

            
    

    
main()