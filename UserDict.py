# UserDict
# UserDict is a dictionary-like container that acts as a wrapper around the dictionary objects. This container is used when someone wants to create their own dictionary with some modified or new functionality



from collections import UserDict, UserList, UserString


class MyDict(UserDict):
    def __init__(self):
        super().__init__()
    
    def __setitem__(self, key, value):
        if key in self.data:
            print(f"Updating value for key '{key}'")
        else:
            print(f"Adding new key '{key}' with value '{value}'")
        super().__setitem__(key, value)

# Example usage
my_dict = MyDict()
my_dict['a'] = 1
my_dict['b'] = 2
my_dict['a'] = 3  # This will trigger the update message

# UserList
# UserList is a list like container that acts as a wrapper around the list objects. This is useful when someone wants to create their own list with some modified or additional functionality.

print("-----------------------------UserList-------------------------")
# Creating a list where deletion is not allowed
class MyList(UserList): 
      
    # Prevents using remove() on list
    def remove(self, s=None): 
        raise RuntimeError("Deletion not allowed") 
          
    # Prevents using pop() on list
    def pop(self, s=None): 
        raise RuntimeError("Deletion not allowed") 
      
# Create an instance of MyList
L = MyList([1, 2, 3, 4]) 
print("Original List") 

# Append 5 to the list
L.append(5) 
print("After Insertion") 
print(L) 
# Attempt to remove an item (will raise error)
# L.remove()  


# UserString
# UserString is a string like container and just like UserDict and UserList it acts as a wrapper around string objects. It is used when someone wants to create their own strings with some modified or additional functionality. 
print("-----------------------------UserString-------------------------")

   
# Creating a Mutable String 
class Mystring(UserString): 
      
    # Function to append to string
    def append(self, s): 
        self.data += s 
          
    # Function to remove from string 
    def remove(self, s): 
        self.data = self.data.replace(s, "") 
      
# Driver's code 
s1 = Mystring("Geeks") 
print("Original String:", s1.data) 
  
# Appending to string 
s1.append("s") 
print("String After Appending:", s1.data) 
  
# Removing from string 
s1.remove("e") 
print("String after Removing:", s1.data)