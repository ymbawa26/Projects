"""
Yazan Bawaqna
CS152 B
Project-03
This program will define several functions to calculate the sum, mean, max, min and variance of the entry parameter.
"""



def sum1(data):
    """This function will calculate the sum for the item lists in numbers"""
    total = 0.0
    #Go over all the items in data
    for i in data:
    #Add the item to the total value
      total += i
    return total

def my_mean(data):
    """This function will calculate the mean for the item lists in numbers"""
    # Count the number of items in data
    items_count = len(data)
    #The mean of the list is equal to the sum of the list divided by the number of items in the list
    my_mean = sum1(data)/items_count
    #return the value of the mean
    return my_mean
         
def my_min(data):
    """This function will identify the minimum valuefor the item lists in numbers"""
    minimum = 1000
    for i in data:
        #if the value of the data item is lower than the minimum value, it will be assigned the minimum value
        if minimum > i: 
            minimum = i
    #return the value of minimum
    return minimum

def my_max(data):
    """This function will calculate the maximum value for the item lists in numbers"""

    #assign the vlaue of maximum the value -10000
    maximum = -1000
    #for all the item in data list:
    for i in data: 
        #if the value of maximum is less than i, then assign i the maximum
        if maximum < i:
            maximum = i
    #return the value my_max
    return maximum

def my_variance(data):
    """This function will calculate the variance for the item lists in numbers"""

    #assigning m for the mean function created earlier
    m = my_mean(data)
    #result is assigned the value of the caluclated variance using the variance equation
    result = sum((float(i)-m) **2 for i in data) / (len(data)-1)
    #return the value of result
    return result

# #testing the program
# data = [2, 4, 5, 9]

# #printing tha called functions using the defined parameter "data"
# print(sum1(data))
# print(my_mean(data))
# print(my_min(data))
# print(my_max(data))
# print(my_variance(data))
# import matplotlib.pyplot as plt
# x=[1,3,5,7]
# y=[2,4,6,1]
# plt.plot(x,y)
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title("A simple line graph")
# plt.show()