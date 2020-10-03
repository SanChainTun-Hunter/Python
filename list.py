mylist = [1,2,3,4,5,6,7,8,9,10]       #creating list number
print(mylist)                         #print list number

animals = ["ants","birds","cows","dogs","elephants"]      #creating animal list array
print(animals)							# print animal list array
animals.append("fish")						# append fish to animals list 
print(animals)
animals.append("goats")						# append fish to animals list 
print(animals)


#indexing of list
print(animals[0] , animals[3] , animals [5])			#indexing to animal list >> index[0] = ants , index[1] = birds ,etc...

#slicing list

print(animals[1:5])             # print index1 to index4 output >>> ['birds', 'cows', 'dogs', 'elephants']
