# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Implement Map using open addressing with double hashing) Implement Map
using open addressing with double probing. For simplicity, use f(key) - key % size
as the hash function, where size is he  hash-table size. Initially, the hash-table
size is 4. The table size is doubled whenever the load factor exceeds
the threshold(0.5)'''

from Map import Map


def main():
    # Create a map
    map = Map()

    # Add key-value pairs to the map
    map.put("apple", 5)
    map.put("banana", 10)
    map.put("orange", 7)
    map.put("grape", 3)

    # Print the size of the map
    print("Size of the map:", map.getSize())

    # Check if the map is empty
    print("Is the map empty?", map.isEmpty())

    # Get values for specific keys
    print("Value for 'apple':", map.get("apple"))
    print("Value for 'orange':", map.get("orange"))

    # Update values for existing keys
    map.put("apple", 8)
    map.put("orange", 12)

    # Remove a key-value pair
    map.remove("banana")

    # Check if a key exists in the map
    print("Does 'grape' exist in the map?", map.containsKey("grape"))
    print("Does 'banana' exist in the map?", map.containsKey("banana"))

    # Check if a value exists in the map
    print("Does the map contain value '7'?", map.containsValue(7))
    print("Does the map contain value '10'?", map.containsValue(10))

    # Print all the keys and values in the map
    print("Keys in the map:", map.keys())
    print("Values in the map:", map.values())

    # Clear the map
    map.clear()

    # Print the size of the map after clearing
    print("Size of the map after clearing:", map.getSize())

    # Check if the map is empty after clearing
    print("Is the map empty after clearing?", map.isEmpty())


main()
