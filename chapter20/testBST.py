from BST import BST

# Test program
bst = BST()
elements = [10, 5, 15, 3, 7, 12, 20, 2, 4, 6, 8, 11, 13, 17, 25]

# Insert elements into the BST
for element in elements:
    bst.insert(element)

# Search for an element
searchKey = 7
result = bst.search(searchKey)
if result is not None:
    print(f"Found {searchKey} in the BST.")
else:
    print(f"{searchKey} not found in the BST.")

# Delete an element
deleteKey = 15
bst.delete(deleteKey)
print(f"Deleted {deleteKey} from the BST.")

# Check if the tree is balanced
if bst.isBalanced():
    print("The BST is balanced.")
else:
    print("The BST is not balanced.")
