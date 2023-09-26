person = ('Angus', 'McGurk', 33)
print(person)
dir(person)       			# Tuples don't have many methods
age = person[2]			# Works, but not good style
print(age)				# Just to prove it worked
(first, last, age) = person 		# Parallel assignment and the preferred way to do the assignment.
print(first, last, age)  		# Just to prove it works
person[2] = 34    			# Tuples are immutable
point = (10, 20)     		# Can use a tuple for cartesian coordinates
print(point)          		# Looks nice when printed
>> (x_coord, y_coord) = point           # Again, parallel assignment to extract coords
>> print(x_coord, y_coord)
>> point[1] = 4		   		# This shouldn't surprise you
>> point_2 = [100, 200]   		# Can also use lists for points
>> print(point_2)          		# Printing doesn't look quite so nice though
>> point_2[1] = 30        		# Why does this work when it didn't with tuples?
>> (x_coord, y_coord) = point_2         # Parallel assignments works with lists, too
>> print(x_coord, y_coord)        	# Proof
>> [x_coord, y_coord] = point_2         # And LHS can be written as a list
>> print(x_coord, y_coord)              # Proof 