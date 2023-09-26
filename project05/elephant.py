"""
Yazan Bawaqna
CS152-B
Lab06
Oct 25th
elephants 1 project
This project will simulate the elephant population in Kruger National Park. it wuill retuen back the total population after N numbernumber opf years. The population will also return back the number of female and male elephants, adults, calfs, and senior.
To run this program cd to the file location then type py main argumrnts
"""
import random
import sys


#naming index variables for Parameter list
IDXCalvingInterval = 0
IDXPercentDarted = 1
IDXMinAge = 2
IDXMaxAge = 3
IDXProb_CalfSurvival = 4
IDXProb_AdultSurvival = 5
IDXProb_SeniorSurvival = 6
IDXCarrying_Capacity = 7
IDXNumber_Years = 8
#defining the index variables in the Elephant lsit
IDXGender = 0
IDXAge = 1
IDXMonthsPregnant = 2
IDXMonthsContraceptiveRemaining = 3
IDXpopulation = 0
IDXnumCalves = 1
IDXnumJuveniles = 2
IDXnumAdultMale = 3
IDXnumAdultFemales = 4
IDXnumSeniors = 5
IDXnumCulled = 6


def newElephant(parameter_list, age):
    """The function newElephant should create and return a list with all of the necessary features of an individual elephant.
    input: the list of simulation parameters, and the age of the elephant to create.
    It should return a list of Gender, Age, Months pregnant integer, Months contraceptive remaining """
    #initializing the elephant list
    elephant = [0,0,0,0]
    #assigning a random gender for each elephant
    elephant[IDXGender] = random.choice("m" "f")
    elephant[IDXAge] = age
    #If the elephant is female, then, if the elephant is of breeding age, test if the elephant is pregnant.  
    if (elephant[IDXGender] == "f" and elephant[IDXAge] > parameter_list[IDXMinAge] and elephant[IDXAge]<=parameter_list[IDXMaxAge]):
            ProbPregnancy = random.random()
            #If the elephant is pregnant, pick a random number between 1 and 22 and assign that to the IDXMonthsPregnant position in the elephant list.
            if ProbPregnancy < 1/parameter_list[IDXCalvingInterval]:
                elephant[IDXMonthsPregnant] = random.randint(1,22)
    #return the elephant list
    return elephant

def initPopulation(parameter_list):
    """ The initPopulation function should take in the parameter list and return a list of
new elephants (which are also lists)."""
    population = []
    #loop for the number of elephants to create and append a new elephant list
    for i in range(0,parameter_list[IDXCarrying_Capacity]):
        elephant = newElephant(parameter_list, random.randint(1,parameter_list[IDXMaxAge]))
        population.append(elephant)
    return population

def incrementAge(population):
    """ This function should take in a population list and return a population list. Inside the function, it should increment each elephant&#39;s age by 1"""
    print("population: ", population)
    for i in population:
        i[IDXAge] += 1
    return population

def Calc_survival(parameter_list, population):
    """The function returns the population list after a survival claculation which is correlated with the elephant age .
    The function takes the parameter list and population list as arguments. return the new population list."""
    
    #Create an empty list, new_population.
    new_population = []
    for items in population:
        #Use the age of the elephant to determine which survival probability applies, then use the appropriate survival probability to see if the elephant should be added to the new_population list.
        if IDXAge > 60:
            if random.random < parameter_list[IDXProb_CalfSurvival]:
               new_population.append(items)
        if IDXAge < 60 and IDXAge > 12:
            if random.random < parameter_list[IDXProb_AdultSurvival]:
                new_population.append(items)
        else:
            if random.random < parameter_list[IDXProb_CalfSurvival]:
                new_population.append(items)
    # return the new_population list            
    return new_population

def dartElephants(parameter_list, population):
    """Thif unction goes through the adult females and randomly selects individuals for darting based on the dart probability parameter. 
    inputs: The parameter list, The population list
    output: returns the population list.""" 
    female = 0
    # assign the three parameters--probability of darting, juvenile age, and maximum age--into local variables.
    probDarting = float((parameter_list[IDXPercentDarted]))
    juvenAge = parameter_list[IDXMinAge]
    maximumAge = parameter_list[IDXMaxAge]
    #The function should loop over each elephant in the population list. I
    for e in population:
        if e[IDXGender] == 'f':
            female += 1
    #inside the loop, it should test if the elephant is a female and is older than the juvenile age and is less than the maximum age.
    for e in population: 
       if e[IDXGender] == 'f' and e[IDXAge] >= juvenAge and e[IDXAge] <= maximumAge: 
           #determine if the elephant should be darted by testing if a call to random.random() is less than the probability of darting.
           if random.random < probDarting:
                e[IDXMonthsPregnant] = 0 
                e[IDXMonthsContraceptiveRemaining] = 22
    #After the loop, return the population list.
    return population


def cullElephants(parameter_list, population): 
    """checks if there are more elephants than the carrying capacity. If there are too many elephants, 
    it should remove enough randomly chosen elephants from the population
    so there are as many elephants as the carrying capacity
     Input: The parameter list and the population list
     Output: return a tuple containing first the new population list and second the number of elephants culled.."""
    newPopulation = []
    #Determine the number of animals that need to be culled
    Elephants_culled = len(population) - parameter_list[IDXCarrying_Capacity]
    #If there are too many elephants, then randomly shuffle the population list
    if Elephants_culled > 0:
        random.shuffle(population)
        newPopulation = population[:parameter_list[IDXCarrying_Capacity]]
    #Return a tuple containing this new list and then the number of animals culled.
    return (newPopulation, Elephants_culled)

def controlPopulation( parameter_list, population ):
    """Determines whetehr a population should be culled or Darted. 
    The input argumets are the parameter list and the population
    output: tuple of the population of the new list and the number of Elephants culled"""

    # if the parameter value for &quot;percent darted&quot; is zero:
    if parameter_list[IDXPercentDarted] == 0:
      # call cullElephants, storing the return values in a two variables  
     (latest_pop, numculled) = cullElephants(parameter_list, population)

    #else call dartElephants and store the result in a variable named newpop
    else:
        latest_pop = dartElephants(parameter_list, population)
        # set a variable named numCulled to zero
        numculled = 0
    # return (newpop, numCulled)    
    return (latest_pop, numculled)
def simulateMonth(parameter_list, population):
    """ The function simulateMonth moves the simulation forward by one month. It modifies only the
    adult females in the population, and it adds a new calf to the population if one should be born.
    The input: argumets are the parameter list and the population list 
    output: the population list """

    eNew = [0,1,0,0]
    calvingInterval = parameter_list[IDXCalvingInterval]
    juvenileAge = parameter_list[IDXMinAge]
    MaxAge = parameter_list[IDXMaxAge]
    #Loop over the population list.
    for e in population:
        # assign to gender the IDXGender item in e
        gender = e[IDXGender]
        #assign to age the IDXAge item in e
        age =  e[IDXAge]
        # assign to monthsPregnant the IDXMonthsPregnant item in e
        monthsPregnant = e[IDXMonthsPregnant]
        # assign to monthsContraceptive the IDXMonthsContraceptiveRemaining item in e
        monthsContraceptive = e[IDXMonthsContraceptiveRemaining]
        #if gender is female and the elephant is an adult
        if "f" in gender and age > juvenileAge and age < MaxAge:
           # if monthsContraceptive is greater than zero
            if monthsContraceptive > 0:
               #decrement the months of contraceptive left (IDXMonthsContraceptiveRemaining element of e) by one
               e[IDXMonthsContraceptiveRemaining] -= 1
            # else if monthsPregnant is greater than zero
            elif monthsPregnant > 0:
                # if monthsPregnant is greater than or equal to 22
                if monthsPregnant >= 22:
                    # create a new elephant of age 1 and append it to the population list
                    genderNew = ['f', 'm']
                    eNew[IDXGender] = random.choice(genderNew)
                    population.append(eNew)
                    # reset the months pregnant (the IDXMonthsPregnant element of e) to zero
                    e[IDXMonthsPregnant] = 0
                # else increment the months pregnant (IDXMonthsPregnant element of e) by 1
                else:  
                    e[IDXMonthsPregnant] += 1
        else:  
            # if the elephant becomes pregnant
                if random.random() < 1.0 / (calvingInterval * 12 - 22):
                    # set months pregnant (IDXMonthsPregnant element of e) to 1
                    e[IDXMonthsPregnant] = 1

def simulateYear(parameter_list, population):
    """ The function simulateMonth moves the simulation forward by one year.
    adult females in the population, and it adds a new calf to the population if one should be born.
    The input: argumets are the parameter list and the population list 
    output: the population list"""
    #calls calcSurvival, then it calls incrementAge,
    population = Calc_survival( parameter_list, population)
    population = incrementAge(parameter_list)
    month = 0
    #loops twelve times calling simulateMonth.
    while month < 12:
        month = month + 1
        population = simulateMonth(parameter_list, population)
    #returns the population list.   
    return population

def Calc_results(parameter_list, population, numculled):
    """ The cfunction calculates how many calves, juveniles, adult males, adult females, and seniors are in the population.
    input: The parameterlist,the  population list and the numculled value
    Output: returns a list with the number of calves, juveniles, adult males, adult females, and seniors are in the population and the total population"""
    juvenileAge = parameter_list[IDXMinAge]
    maxAge = parameter_list[IDXMaxAge]
    numCalves = 0
    numJuveniles = 0
    numAdultMales = 0
    numAdultFemales = 0
    numSeniors = 0
    for e in population:
        #checking the age parameter and counting needed individuals
        if e[IDXAge] <= 1:
            numCalves += 1
        elif e[IDXAge] > 1 and e[IDXAge] <= juvenileAge:
            numJuveniles += 1
        elif e[IDXAge] > juvenileAge and e[IDXAge] < maxAge and e[IDXGender] == 'f':
            numAdultFemales += 1
        elif e[IDXAge] > juvenileAge and e[IDXAge] < maxAge and e[IDXGender] == 'm':
            numAdultMales += 1
        else:
            numSeniors += 1
    return [len(population), numCalves, numJuveniles, numAdultMales, numAdultFemales, numSeniors, numculled]

def runSimulation(parameter_list):
    """input the parameter list and the number of years, N, to run the simulation.
    Output: list ot the results"""
    #Creating a new population, applying the control procedures
    popsize = parameter_list[IDXCarrying_Capacity]
    # init the population
    population = initPopulation( parameter_list )
    [population,numCulled] = controlPopulation( parameter_list, population )
     # run the simulation for N years, storing the results
    results = []
    for i in range(parameter_list[IDXNumber_Years]):
        population = simulateYear( parameter_list, population )
        [population,numCulled] = controlPopulation( parameter_list, population )
        results.append( Calc_results( parameter_list, population, numCulled ) )
        if results[i][0] > 2 * popsize or results[i][0] == 0 :
        # cancel early, out of control
            print('Terminating early')
            break
    return results
def test():

    ## assign each parameter to a variable with an informative name
    CalvingInterval = 3.1
    PercentDarted = 0.0
    MinAge = 12
    MaxAge = 60
    Prob_CalfSurvival = 0.85
    Prob_AdultSurvival = 0.996
    Prob_SeniorSurvival = 0.2
    Carrying_Capacity = 7000
    Number_Years = 200
    Gender = ""
    Age = 0
    MonthsPregnant = 0
    MonthsContraceptiveRemaining = 0

    #Making the parameter list
    parameter_list = [CalvingInterval, PercentDarted, MinAge, MaxAge, Prob_CalfSurvival, Prob_AdultSurvival, Prob_SeniorSurvival, Carrying_Capacity, Number_Years, Gender, Age, MonthsPregnant, MonthsContraceptiveRemaining]

    # print the parameter list
    print(parameter_list)
    population = []
    for i in range(15):
        population.append(initPopulation(parameter_list))
        random.randint(1,parameter_list[2])
       
    for e in population:
        print(e)
    print("Increment Age")
    incrementpopulation = []
    for i in range(15):
        incrementpopulation.append(incrementAge(population))
    for e in population:
        print(e)

def main(argv):
    """input: average results (average total population, average number of calves, average number of juveniles, and so on).
    output: average results (average total population, average number of calves, average number of juveniles, and so on)."""
    print("Usage: List of the parameters")
    probDart = float(argv[1])
    calvingInterval = 3.1
    #percentDarted = 0.0
    juvenileAge = 12
    maximumAge = 60
    probabilityOfCalfSurvival = 0.85
    probabilityOfAdultSurvival = 0.996
    probabilityOfSeniorSurvival = 0.20
    carringCapacity = 7000
    numberOfYears = 200
    # creating a paramters list 
    parameters = [calvingInterval, probDart, juvenileAge, maximumAge, probabilityOfCalfSurvival, probabilityOfAdultSurvival, probabilityOfSeniorSurvival, carringCapacity, numberOfYears]
    print(parameters)
    results = []
    results = runSimulation(parameters)
    print('runSimulation() last element in the list')
    print(results[-1])

    #initilaze all the population groups/classifications
    averageTotalPop = 0
    averageNumOfCalves = 0
    averageNumOfJuveniles = 0
    averageNumOfMales = 0
    averageOfAdultFemales = 0
    averageOfSeniors = 0
    averageOfCulled = 0
    TotalPop = 0
    NumOfCalves = 0
    NumOfJuveniles = 0
    NumOfMales = 0
    AdultFemales = 0
    Seniors = 0
    Culled = 0

    #loop over the results
    for e in results:
        #Add every item of the same population group to the same population group
        TotalPop += e[IDXpopulation]
        NumOfCalves += e[IDXnumCalves]
        NumOfJuveniles += e[IDXnumJuveniles]
        NumOfMales += e[IDXnumAdultMale]
        AdultFemales += e[IDXnumAdultFemales]
        Seniors += e[:][-2]
        Culled += e[:][-1]

    #calculating the average for the simulated groups
    averageTotalPop = TotalPop / len(results)
    averageNumOfCalves = NumOfCalves / len(results)
    averageNumOfJuveniles = NumOfJuveniles / len(results)
    averageNumOfMales = NumOfMales / len(results)
    averageOfAdultFemales = AdultFemales / len(results)
    averageOfSeniors = Seniors / len(results)
    averageOfCulled = Culled / len(results)

    #printing the outcomes of the simulation/number of indiviuals per group
    print('total population (averge):', averageTotalPop)
    print('Number of calves (average):', averageNumOfCalves)
    print('Number of juveniles(Average) :', averageNumOfJuveniles)
    print('Number of of adult males(Average):', averageNumOfMales)
    print('Number of adult females(Average):', averageOfAdultFemales)
    print(' number of seniors (Average):', averageOfSeniors)
    print(' number of culled elephants(Average):', averageOfCulled)



if __name__ == "__main__":
    main(sys.argv)