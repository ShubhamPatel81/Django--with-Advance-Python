from collections import Counter,OrderedDict, defaultdict,ChainMap, deque ,namedtuple
import collection
# Counters  
print("-----------------------------Counter-------------------------")
print(Counter(['a','b','c','a','c','b','a','c','a']))

# Creating Counter from a dictionary
print(Counter({'A':3, 'B':5, 'C':2}))


# OrderedDict - 

# OrderedDict also offers extra features like moving re-inserted keys to the end making it useful for order-sensitive operations.

print("-----------------------------OrderDict-------------------------")
print("This is Dictionary : ")
d ={}
d['a'] =1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['f'] = 5
print("Dictionary is : ",d)

#using for loop
for key, value in d.items():
  print(key, value)

print("\nThis is an Ordered Dict:\n") 
od = OrderedDict();
od['a'] =1
od['b'] = 2
od['c'] = 3
od['d'] = 4
od['e'] = 5
od['f'] = 6
for key, value in od.items():
  print(key,value)
 

 # Inserting and deleting in Ordered Dict
print("-----------------------------OrderDict(Inserting and Deleting)-------------------------")
od = OrderedDict() 
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
  
print('Before Deleting')
for key, value in od.items(): 
    print(key, value) 
    
# deleting element
od.pop('a')

# Re-inserting the same
od['a'] = 1

print('\nAfter re-inserting')
for key, value in od.items(): 
    print(key, value)


    # DefaultDict
print ("-----------------DefaultDict---------------------")
# Creating a defaultdict with default value of 0 (int)
d = defaultdict(int) 
L = [1, 2, 3, 4, 2, 4, 1, 2] 

# Counting occurrences of each element in the list
for i in L: 
    d[i] += 1  # No need to check key existence; default is 0

print(d)


# ChainMap
# A ChainMap encapsulates many dictionaries into a single unit and returns a list of dictionaries.


print("-----------------------------ChainMap-------------------------")
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

# Defining the chainmap 
c = ChainMap(d1, d2, d3) 
print(c)

print("-----------------------------ChainMap(new_child())-------------------------")

dict1 = {'a':1, 'b':2}
dict2 = {'c':3,'d':4}
dict3 ={'f':5}
chain = collection.ChainMap(dict1,dict2)

# printing chainMap 
print ("All the ChainMap contents are: ") 
print (chain) 

# using new_child() to add new dictionary 
chain1 = chain.new_child(dict3)

# printing chainMap
print ("Displaying new ChainMap : ") 
print (chain1)

# NamedTuple
print("-----------------------------NamedTuple-------------------------")

Student = namedtuple('Student',['Name', 'Age','DOB'])

#Adding values
S = Student("Shubh",23,'08/07/2005')
print(S)
  
# Access using index 
print ("The Student age using index is : ",end ="") 
print (S[1]) 
  
# Access using name  
print ("The Student name using keyname is : ",end ="") 
print (S.Name)

# Deque(Double-ended Queue)
print("-----------------------------Deque(Double-ended Queue)-------------------------")
# Declaring deque
queue = deque(['name','age','DOB']) 
print(queue)
# Initialize deque with initial values
de = deque([6, 1, 2, 3, 4])

# Delete element from the right end (removes 4)
de.pop()

# Print deque after deletion from the right
print("The deque after deleting from right is :") 
print(de)

# Delete element from the left end (removes 6)
de.popleft()

# Print deque after deletion from the left
print("The deque after deleting from left is :") 
print(de)
