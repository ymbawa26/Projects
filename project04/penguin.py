"""
Yazan Bawaqna
CS152-B
Project04
Penguins survival Simulation program"""

import random
import sys

#Initialize populatio to the empty list.
population = []
def initPopulation(N, probFemale):
    """ This function takes two paramters, initial population size and probability an indiviual being a female, the function returns a list of the specified size"""

    #creat a while loop based on the size of the population
    i = 0
    while i < N:
        i = i + 1
        random_number = random.random()
        #If the value is less than the probability of an individual being female (probFemale), append an 'f' to the population list. 
        if random_number < probFemale:
            population.append("f")
        #Otherwise, append an 'm' to the population list.
        else:
            population.append("m")

    #return the population list
    return population

    


 
def simulateYear(pop, elNinoprob, stdRho,elNinorho, probFemale,  MaxCapacity):
    """This function takes 6 paramter as follows:
    pop: the population list
    elNinoProb: the probability of an El Nino
    stdRho: the growth factor in a regular year. This number is meant to allow the population to grow each year and is expected to be greater than 1.
    elNinoRho: the growth factor in an El Nino year. This number is meant to reduce the population and is therefore less than 1.
    probFemale: the probability of a new individual being female,
    maxCapacity: the max carrying capacity of the ecosystem. 
    The function returns back a list of the gender of the population after a El Nino year or a normal year, depending on the probability"""

    #Create an empty list names new_population
    new_population = []
    elNino_year = False
    #generate a random number
    random_value = random.random()
    if random_value < elNinoprob:
        elNino_year = True
    ## for each penguin in the original population list
    for penguin in pop:
        # if the length of the new population list is greater than maxCapacity
        # break, since we don't want to make any more penguins
        if MaxCapacity < len(new_population):
            break

        # if it is an El Nino year
        if elNino_year is True:
             # if random.random() is less than the El Nino growth/reduction factor
            if  random.random() < elNinorho:
                    # append the penguin to the new population list
                    new_population.append(penguin)
        else:
            #append the penguin to the new population list
            new_population.append(penguin)
            #if random.random() is less than the standard growth factor - 1.0
            if  random.random() < stdRho - 1:
                if random_value < probFemale:
                    new_population.append("f")
                #Otherwise, append an 'm' to the population list.
                else:
                    new_population.append("m")
    #return the new_population list
    return new_population

def runSimulation(N, initPopSize, ProbFemale, elNinoProb, StdRho, elNinoRho, MaxCapacity, minViable):
    """  N = numb of years to run the simulation
    initPopSize= initial population size
    probFemale = prob a penguin is female
    elNinoProb = prob El Nino occurs in a given year
    stdRho = population growth in non-El Nino year
    elNinoRho = pop growth in an El Nino year
    maxCapacity = max carrying capacity of ecosystem 
    minViable = min viable population 
    The function will either return the year the penguins population will go extinct or return the population after N years"""
    current_population = initPopulation(initPopSize, ProbFemale)
    #loop N times.
    EndDate = N
    i = 0
    while i < N:
        #inside the loop it should call simulateYear
        latest_population = simulateYear(current_population, elNinoProb, StdRho, elNinoRho, ProbFemale, MaxCapacity)
        # If, after simulating a year, the population is smaller than the minimum viable population the program returns the year of extension
        if (len(current_population)) >= minViable and ('f' in current_population ) and ('m' in current_population):
            current_population = latest_population
        else:
            EndDate = i
            break
        i = i + 1
    return EndDate

def main(argv):
    """ This function casts three arguments from cast, and output the probability of the penguins surviving extinction after N years """
    #test if there is at least three arguments on the command line.
    if len(argv) < 3:
        print("Argv list should contain 3 item, the first argument will be the name of the program, the second should be the number of simulations to run, and the third should be the typical number of years between an El Nino event.")
        quit
    else:
        # cast the second argument (argv[1]) to an integer and assign it to a variable that specifies the number of simulations to run 
        secondnum = int(argv[1])
        #Cast the third argument (argv[2]) to an integer and assign it to a variable that specifies the typical number of years between an El Nino event.
        years_between_elNino = int(argv[2])
        
        #Giving values for each parameter
        N = 201
        initPopSize = 500
        ProbFemale = 0.5 
        elNinoRho = 0.41
        MaxCapacity = 2000
        MinCapacity = 10
        elNinoProb = 1/years_between_elNino
        StdRho = 1.188
        ResultForSims = []
        #Loop for the number of simulations.
        for i in range(secondnum):
            #Inside the loop, append to your result list the result of calling runSimulation
            ResultForSims.append(runSimulation(N, initPopSize, ProbFemale, elNinoProb, StdRho, elNinoRho, MaxCapacity, MinCapacity))
        Extinction_prob = 0
        for num in ResultForSims:
            if num <  N:
                Extinction_prob = Extinction_prob + 1
        Extinction_prob = Extinction_prob/secondnum
        print("The probability of the pengians going extinctin in %i years is %.3f" % (N, Extinction_prob))
        return ResultForSims
    
def computeCEPD(data, N):
    """This function takes two arguments, 
    data = set of numbers indicating the last year in which the population was viable
    N = number of years 
    the function output is a cumulative extinction probability distribution (CEPD)."""
    List_CEPD = []
    for i in range(N):
        #appending N zeros to an empty list in a loop.
        List_CEPD.append(0)
    for i in range(len(data)):
        #If the extinction year is less than N, loop from the extinction year to N and add one to each of those entries in the CEPD list.
        if data[i]<N:
            for item in range(data[i], N):
                List_CEPD[item] = List_CEPD[item] + 1

    #loop over the CEPD list and divide each entry by the length of the extinction year results list            
    for item2 in range (len(List_CEPD)):
        List_CEPD[item2] /= len(data)
    #return the CEPD list.
    return List_CEPD


# test function for initPopulations"" "
def test(): 
    """This functions runs test for the functions above"""
    
    popsize = 10
    probFemale = 0.5
    print(initPopulation(10, 0.5))
    pop = initPopulation(popsize, probFemale)
    print( pop )
    newpop = simulateYear(pop, 1.0, 1.188, 0.4, 0.5, 2000)
    print( "El Nino year" )
    print( newpop )
    newpop = simulateYear(pop, 0.0, 1.188, 0.4, 0.5, 2000)
    print( "Standard year" )
    print( newpop )
    
    print("run simulation")
    print(runSimulation(201, 500, 0.5, 1/7, 1.188, 0.41, 2000, 10))
    print("main")
test()


if __name__ == "__main__":
    test() 
    #acknowledgement: this part was mostly achieved by the help of Kalyan
    main(sys.argv) 
    list_CEPD = computeCEPD(main(sys.argv), 201)
    for i in range(int(len(list_CEPD) / 10)):
        print(list_CEPD[10 * i + 9])
