
Lab6+Project6
Due Nov 1, 11:59 PM
Material
Project 5: Missing Testing Python File
Edited Oct 19
Completed Assignment
Lab5+Project5
Due Oct 25, 11:59 PM
Posted Oct 19
Graded

CS 152 SP22 Project 5 Simulating Elephant Population Management.docx
Word

CS 152 SP22 Lab Exercise 5 Representing Elephants as Lists.docx
Word

test_calcSurvival.py
Text

test_calcResults.py
Text

test_controlPopulation.py
Text

test_simulateYear.py
Text

test_simulateMonth.py
Text

test_dartElephants.py
Text

elephant.png
Image

Yazan Bawaqna - Project 05 Rubric
Google Sheets
Material
Project Schedule
Posted Sep 11
Material
Report Writing Guidelines
Posted Sep 13
Material
Sample Grading Rubric
Posted Sep 13
Material
Official Project Report Template
Posted Sep 21
Completed Assignment
Project 04 (Lab 04 Posted Separately)
Due Oct 18, 11:59 PM
Week 1 (Sep. 7-9)
Week 1 (Sep. 7-9)
Material
Lecture 01
Posted Sep 7
Material
Lecture 02
Posted Sep 12
Week 2 (Sep. 12-16)
Week 2 (Sep. 12-16)
Material
Socratica: Functions
Posted Sep 22
Material
Lecture 03: Functions
Posted Sep 12
Week 3 (Sep. 19-23)
Week 3 (Sep. 19-23)
Material
Socratica: Conditionals
Edited Sep 22
Material
Lecture 6: Conditionals
Posted Sep 19
Week 4 (Sep. 26-30)
Week 4 (Sep. 26-30)
Assignment
Colaboratory: Lists
No due date
Material
Lecture 9: Lists
Posted Sep 26
Material
Socratica: Lists
Edited Sep 22
Week 5 (Oct. 3-7)
Week 5 (Oct. 3-7)
Material
Socratica: Tuples
Posted Sep 29
Week 8 (Oct. 24-28)
Week 8 (Oct. 24-28)
Material
10-24 Inheritance Slide Deck
Posted Oct 24
Material
Search and Optimization Collaboratory
Posted Oct 24
# Stephanie Taylor
# Fall 2015 CS151 (Science)
# Project 5
# This module tests the controlPopulation function in elephant.py
# Call it like this:
#    python3 test_controlPopulation.py
#
#
#                                                                                                                                     
# NOTE: The following statistics were calculated in Python2, which seems to have had a slightly different                             
# random number generator. Your results will be close to the following, but will likely not match exactly.                      
#         
#
#
# Because I have seeded the random number generator, the output will be identical every time you run it. You should see:
# Test 1
# Out of 5144 adult female elephants, 2587 are darted, leading to a percentage of 0.503. It should be 0.500
#
# Test 2
# 100 should have been culled and 100 were
# 
# Test 3
# Out of 5036 adult female elephants, 5036 are darted, leading to a percentage of 1.000. It should be 1.000
# 
# Test 4
# We needed to cull 1000 elephants and 1000 elephants were culled
# Out of 1000 calves before culling, approximately 909 should remain after culling. 913 remain.
# 
# Test 5
# We needed to cull 0 elephants and 0 elephants were culled
# Out of 0 calves before culling, approximately 0 should remain after culling. 0 remain.
# 
# Test 6
# We needed to cull 10000 elephants and 10000 elephants were culled
# Out of 10000 calves before culling, approximately 5000 should remain after culling. 5015 remain.
# If you would like it to change from run to run, then comment out the call to random.seed.

import elephant
import random

def testDarting( pcnt_darted ):
    calving_interval = 3.1
    juvenile_age = 12
    max_age = 60
    p_calf_survival = 0.85
    p_adult_survival = 0.996
    p_senior_survival = 0.2
    carrying_capacity = 10000
    num_over = 100

    params = [calving_interval, pcnt_darted, juvenile_age, max_age, p_calf_survival, p_adult_survival, p_senior_survival, carrying_capacity]

    # Create a new, undarted population, and make it too big. It should remain too big if
    # the pcnt_darted > 0
    pop = []
    for i in range( carrying_capacity+num_over ):
        # Create a new adult elephant. 
        pop.append( [random.choice(['m','f']), random.randint(juvenile_age+1, max_age ), 0, 0] )
    (pop, numCulled) = elephant.controlPopulation( params, pop )

    if pcnt_darted > 0.0:
        numF = 0
        numDarted = 0
        for e in pop:
            if e[0] == 'f':
                numF += 1
                if e[3] == 22:
                    numDarted += 1
        print("Out of %d adult female elephants, %d are darted, leading to a percentage of %0.3f. It should be %0.3f" % (numF, numDarted, float(numDarted)/numF,pcnt_darted))
    else:
        print("%d should have been culled and %d were" % (num_over, numCulled))

def testCulling( population_overrun ):
    calving_interval = 3.1
    juvenile_age = 12
    max_age = 60
    p_calf_survival = 0.85
    p_adult_survival = 0.996
    p_senior_survival = 0.2
    carrying_capacity = 10000
    pcnt_darted = 0.0

    params = [calving_interval, pcnt_darted, juvenile_age, max_age, p_calf_survival, p_adult_survival, p_senior_survival, carrying_capacity]

    # Create a new, undarted population
    pop = []
    for i in range( carrying_capacity ):
        # Create a new adult elephant. 
        pop.append( [random.choice(['m','f']), random.randint(juvenile_age+1, max_age ), 0, 0] )
    for i in range( population_overrun ):
        # Create a new calf.
        pop.append( [random.choice(['m','f']), 1, 0, 0] )
    (pop,numCulled) = elephant.controlPopulation( params, pop )

    print("We needed to cull %d elephants and %d elephants were culled" % (population_overrun, numCulled))
    
    # If the population has been properly culled, there will still be calves.
    numCalves = 0
    for e in pop:
        if e[1] == 1:
            numCalves += 1
    print("Out of %d calves before culling, approximately %d should remain after culling. %d remain." % (population_overrun, int((1-float(population_overrun)/(carrying_capacity+population_overrun))*population_overrun), numCalves))

def main():
    random.seed( 0 )

    # Test the function with a darting percentage of 50%
    print("Test 1")
    testDarting( 0.5 )

    # Test the function with a darting percentage of 0%
    print("\nTest 2")
    testDarting( 0.0 )

    # Test the function with a darting percentage of 100%
    print("\nTest 3")
    testDarting( 1.0 )

    # Test the function with a population overrun of 1000
    print("\nTest 4")
    testCulling( 1000 )

    # Test the function with a population overrun of 0
    print("\nTest 5")
    testCulling( 0 )

    # Test the function with a population overrun of 10000
    print("\nTest 6")
    testCulling( 10000 )
    
if __name__ == '__main__':
    main()