# Exercise 3: Get Only unique items from two sets
# Write a Python program to return a new set with unique items from both sets by removing duplicates.

# Note: set is unordered, so not necessary this will be the order of the item.

# Show Hint
# Use the union() method of a set.

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.union(set2))