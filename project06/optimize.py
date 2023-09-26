"""
Yazan Bawaqna
CS-152 B
project 06
November 1st 2022
This program optimizes the percantage of elephants getting darted for different/changing parameters. 
the program will plot a graph for the results using matplot
"""

import elephant
import random
import sys 
import matplotlib.pyplot as plt




def optimize( min, max, optfunc, parameters = None, tolerance = 0.001, maxIterations = 20, verbose=False ):
 # assign to the variable done, the value False
    Done = False

    # start a while loop that executes while done is not True
    while Done == False: 
        # increment count (which keeps track of how many times the loop executes

        # assign to testValue the average of min and max (use integer math)
        testValue = (min - max)/2
        #If verbose is True, print out testValue.
        if verbose == True:
            print(testValue)
        #Assign to result the return value of calling optfunc with testValue and parameters as the arguments.
        result = optfunc(testValue, parameters)
            #If the result is positive, assign to max the value of testValue.
        if result > 0:
            max = testValue
            # if the result is negative, assign to min the value of testValue.
        elif result < 0:
            min = testValue
            # assign to done the value True.
        else:
            Done == True
            #If max - min is less than the tolerance value, then assign to done the value True.
        if max - min < tolerance:
            Done == True
            #Decrement maxIterations. If maxIterations is less than or equal to zero, then set done to True.
            maxIterations = maxIterations - 1
        if maxIterations <= 0:
            Done == True 
    #Outside the loop, return testValue.
    return (testValue)
    
# a function that returns x - target
def target(x, pars):
    return x - 0.73542618

# Tests the binary search using a simple target function.
# Try changing the tolerance to see how that affects the search.
def testTarget():
    res = optimize( 0.0, 1.0, target, tolerance = 0.01, verbose=True)
    print (res)


def evalParameterEffect( whichParameter, testmin, testmax, teststep,defaults=None, verbose=False ):
    """
    inputs: Evaluates the effects of the selected parameter on the dart percentage
    whichParameter: the index of the parameter to test
     testmin: the minimum value to test
    testmax: the maximum value to test
    teststep: the step between parameter values to test
    defaults: default parameters to use (default value of None)"""

    # if defaults is None, assign to simParameters the result of calling elephant.defaultParameters.
    if defaults == None:
        simParameters = elephant.defaultParameters()
    # else, assign to simParameters a copy of defaults (e.g.simParameters = defaults[:])
    else:
        simParameters = defaults[:]

    # create an empty list (e.g. results) to hold the results
    results_list = []
    #if verbose:
    if verbose:
        print ("Evaluating parameter %d from %.3f to %.3f with step %.3f"%(whichParameter, testmin, testmax, teststep))
        # assign to t the value testmin
    t = testmin
    # while t is less than testmax
    while t < testmin:
    # assign to the whichParameter element of simParameters (e.g. simParameters[whichParameter]) the value t
        simParameters[whichParameter] = t
    # assign to percDart the result of calling optimize with the appropriate arguments, including simParameters
    PercDart = optimize(0, 1.0, elephant.elephantSim, parameters = simParameters, verbose = False)
    # append to results the tuple (t, percDart)
    results_list.append((t, PercDart))
    if verbose:
         print("%8.3f \t%8.3f"%(t,PercDart))
         # increment t by the value teststep
         t+=teststep
    if verbose:
        print("Terminating")
    # return the list of results
    return results_list
'''
if __name__ == "__main__":
    evalParameterEffect( elephant.IDXProb_AdultSurvival, 0.98, 1.0, 0.001, verbose=True )
'''
if __name__ == "__main__":
    #creating empty lists for plotting
    list1= []
    #assigning  alist for each point
    x1=[]
    y1=[]
    x2=[]
    y2=[]
    x3=[]
    y3=[]
    for x in range(1):
        #performing the evaluation 3 times
        results = evalParameterEffect( elephant.IDXProb_AdultSurvival, 0.98, 1, 0.1, verbose=True )
        list1.append(results)
        for a in results:
            #appending the values
            if len(x1) < 20: 
                x1.append(a[0])
                y1.append(a[1])
                print(x1)
                print(y1)
            elif len(x2) < 20:
                x2.append(a[0])
                y2.append(a[1])
                print(x2)
                print(y2)
            elif len(x3) < 20:
                x3.append(a[0])
                y3.append(a[1])
                print(x3)
                print(y3)
    print(x1, y1)
    print(x2, y2)
    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.plot(x3, y3)
    plt.title(
        "Effect of changing parameters of Elephant population on Optimal Percent Darted")
    #This label is changed based on which parameter you are changing
    plt.xlabel("Adult Survival Probability")
    plt.ylabel("Optimal Percent Darted")
    plt.show()


if __name__ == "__main__":
    x1 = []
    y1 = [] 
    y2 = []

    x3 = []
    y3 = []

    x4 = []
    y4 = []

    x5 = []
    y5 = []

    # adult survival
    results = evalParameterEffect(elephant.IDXProb_AdultSurvival, 0.98,1.0, 0.001, verbose=True)

    for result in results:
        x1.append(result[0])
        y1.append(result[1])

    plt.plot(x1, y1)
    plt.show()
    plt.close()

    # calf survival prob
    results = evalParameterEffect(elephant.IDXProb_CalfSurvival, 0.80, 0.90, 0.01, verbose=True)

    for result in results:
        x2.append(result[0])
        y2.append(result[1])

    plt.plot(x2, y2)
    plt.show()
    plt.close()


    # senior survival prob
    results = evalParameterEffect(elephant.IDXProb_SeniorSurvival, 0.1, 0.5, 0.05, verbose=True)

    for result in results:
        x3.append(result[0])
        y3.append(result[1])

    plt.plot(x3, y3)
    plt.show()
    plt.close()

    # calving interval
    results = evalParameterEffect(elephant.IDXCalvingInterval, 3, 3.4, 0.05, verbose=True)

    for result in results:
        x4.append(result[0])
        y4.append(result[1])

    plt.plot(x4, y4)
    plt.show()
    plt.close()

    # max age
    results = evalParameterEffect(elephant.IDXMaxAge, 56, 66, 2, verbose=True)

    for result in results:
        x5.append(result[0])
        y5.append(result[1])

    plt.plot(x5, y5)
    plt.show()
    plt.close()          
